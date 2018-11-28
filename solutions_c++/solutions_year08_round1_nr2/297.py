#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

//#define PRINT_DEBUG

struct VoidStream {};

template<typename T>
inline VoidStream & operator<<(VoidStream &v, T t) {
	return v;
}


#ifdef PRINT_DEBUG
	#define OUT_DEBUG std::cout
#else
	VoidStream _vs_;
	#define OUT_DEBUG _vs_
#endif



struct Milkshake {
	unsigned int type;
	unsigned int melted;
};
typedef std::vector<Milkshake> Choice;
typedef std::vector<Choice*> AllChoices;

Choice * readChoice(std::ifstream &in) {
	Choice * pv = new Choice;
	unsigned int n;
	in >> n;

	for (unsigned int i = 0; i < n; i++) {
		Milkshake m;
		in >> m.type >> m.melted;
		m.type--;
		pv->push_back(m);
	}

	return pv;
}

void debugAllData(AllChoices &ac) {
	for (unsigned int i = 0;  i < ac.size(); i++) {
		OUT_DEBUG << i << ": ";
		Choice &ch = *(ac[i]);
		for (unsigned int j = 0; j < ch.size(); j ++) {
			OUT_DEBUG << '[' << ch[j].type << ' ' << ch[j].melted << "] ";
		}
		OUT_DEBUG << '\n';
	}
}

void doCase(std::ifstream &in) {
	unsigned int N, M;
	in >> N >> M;

	// first, read the data
	AllChoices ac;
	for (unsigned int i = 0; i < M; i ++) {
		ac.push_back(readChoice(in));
	}
	debugAllData(ac);

	// at the beginning, all milkshakes are "0"
	std::vector<int> res;
	for(unsigned int i = 0; i < N; i++)
		res.push_back(0);

	// change only required preferences to "MELTED"
	bool wasChanged = false;
	int iter = 0;

	do {
		iter++;
		//std::cout << "iteration " << iter << '\n';
		wasChanged = false;
		for (unsigned int i = 0;  i < ac.size(); i++) {
			Choice &ch = *(ac[i]);
			bool foundOK = false;
			int myMelted = -1;
			for (unsigned int j = 0; j < ch.size(); j ++) {
				if (ch[j].melted == res[ch[j].type]) {
					// found one which is OK
					foundOK = true;
					break;
				} else if (ch[j].melted == 1)
					myMelted = ch[j].type;
			}
			if (!foundOK) {
				if (myMelted == (-1)) {
					std::cout << "IMPOSSIBLE";
					return;
				} else {
					if (res[myMelted] == 1)
						std::cout << "BUG!\n";
					res[myMelted] = 1;
					wasChanged = true;
				}
			}
		}
	} while(wasChanged);

	for(unsigned int i = 0; i < N; i++) {
		if (i>0) std::cout << ' ';
		std::cout << res[i];
	}
}



int main(int argc, char *argv[]) {
	OUT_DEBUG << "reading from file \"" << argv[1] << "\"\n";
	std::ifstream in(argv[1]);

	unsigned int num_cases;
	in >> num_cases;
	OUT_DEBUG << "num of cases: " << num_cases << '\n';

	for (unsigned int i = 1; i <= num_cases; i++) {
		OUT_DEBUG << "STARTING CASE " << i << '\n';
		std::cout << "Case #" << i << ": ";
		doCase(in);
		std::cout << '\n';
	}

	return 0;
}