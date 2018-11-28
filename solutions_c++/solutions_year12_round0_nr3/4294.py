#include <iostream>
#include <map>
#include <fstream>
#include <vector>
#include <sstream>

template <class T, class U>
T cast(const U& in) {
	std::stringstream ss;
	ss << in;
	T out;
	ss >> out;
	return out;
}

std::string read_line(std::ifstream& in) {
	std::string s;
	std::getline(in, s);
	return s;
}

int read_int(std::ifstream& in) {
	int i;
	in >> i;
	return i;
}

struct Case {
	int A, B;
};

void read_cases(const std::string& from, std::vector<Case>& to) {
	std::ifstream inp(from);
	int cases = cast<int>(read_line(inp));
	//
	for (int i = 0; i < cases; i++) {
		Case c;
		c.A = read_int(inp);
		c.B = read_int(inp);
		to.push_back(c);
	}
	//
	inp.close();
}

int pow10[] = {
	1,
	10,
	100,
	1000,
	10000,
	100000,
	1000000,
	10000000,
	100000000,
	1000000000,
};

int is_recycled(int a, int b) {
	std::string n = cast<std::string>(a);
	int len = n.length();
	//
	for (int st = 1; st <= len; ++st) {
		int p = pow10[st];
		int modif = ((b/p) + (b%p)*pow10[len-st]);
		if (a == modif) {
			return 1;
		}
	}
	//
	return 0;
}

__int8 cache[1000][1000] = {0};

int main(int argc, char* argv[]) {
	std::vector<Case> a;
	read_cases(argv[1], a);

	for (int i = 0; i < 1000; ++i)
		for (int j = 0; j < 1000; ++j)
			cache[i][j] = -1;

	std::ofstream out("problemc.out");
	for (int i = 0; i < a.size(); i++) {
		out << "Case #" << (i+1) << ": ";
		auto d = a[i];
		int count = 0;
		//std::cout << "case: " << i << "\n";
		//
		for (int i = d.A; i <= d.B; ++i) {
			for (int j = i+1; j <= d.B; ++j) {
				if (cache[i][j] == -1) { 
					auto res = is_recycled(i, j);
					cache[i][j] = res;
					count += res;
				} else {
					count += cache[i][j];
				}
			}
		}
		//
		out << count;
		out << "\n";
	}
	out.close();
	std::cout << "done!\n";

	return 0;
}