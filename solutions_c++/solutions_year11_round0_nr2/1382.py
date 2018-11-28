#include <iostream>
#include <fstream>
#include <list>

using namespace std;

int main(int argc, char** argv) {
	fstream in;
	fstream out;

    in.open(argv[1], ios::in);
	out.open(argv[2], ios::out);

	int T, C, D, N;
	char last;
	char cur;

	int comb[26][26];
	bool oppo[26][26];
	bool invoked[26];
	list<char> n;

    in >> T;
	
	for(int i=1; i<=T; i++) {
		n.clear();
		for(int j=0; j<26; j++) {
			for(int k=0; k<26; k++) {
				comb[j][k] = -1;
				oppo[j][k] = false;
			}
			invoked[j] = false;
		}
		in >> C;
		char c[4];

		for(int j=0; j<C; j++) {
			in >> c;
			comb[c[0]-65][c[1]-65] = c[2]-65;
			comb[c[1]-65][c[0]-65] = c[2]-65;
		}

		in >> D;
		char d[3];

		for(int j=0; j<D; j++) {
			in >> d;
			oppo[d[0]-65][d[1]-65] = true;
			oppo[d[1]-65][d[0]-65] = true;
		}

		in >> N;
		cur = -1;
		
		for(int j=0; j<N; j++) {
			last = cur;
			in >> cur;
			cur -= 65;

			if(last != -1 && comb[last][cur] != -1) {
				n.push_back(comb[last][cur]);
				cur = -1;
			} else {
				if(last != -1) {
					n.push_back(last);
					invoked[last] = true;
				}
			}

			for(int k=0; k<26; k++) {
				if(cur != -1 && oppo[cur][k] && invoked[k]) {
					last = cur = -1;
					n.clear();
					for(int m=0; m<26; m++) invoked[m] = false;
				}
			}
		}

		if(cur != -1) n.push_back(cur);

		out << "Case #" << i << ": [";
		int h = n.size();
		for(list<char>::iterator l=n.begin(); l!=n.end(); ++l) {
			h--;
			out << (char)((*l) + 65);
			if(h != 0) out << ", ";
		}
		out << "]" << endl;
	}

    in.close();
	out.close();
}