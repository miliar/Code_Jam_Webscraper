#include <set>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

inline int f(char ch) {
 	return (int(ch)-int('a'));
}

int main() {

	int i, j, k;

	int t, p, q;

	int T, A, B;

	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small.out");

	int n;
	string str;

	fin >> T;
	getline(fin, str, '\n');

	for (int I = 0; I < T; I++) {
		n=0;
		fin >> A >> B;
		for (j = A; j < B; j++) {
			set<int> m;
			t=j;
			k=0;
			p=1;
			while(t) {
				t=t/10;
				if(t)	p *= 10;
				k++;
			}
			int P=10*p;
			t=j;
			while(k>0) {
				q = j/p;
				if(q) {

					t = j - q*p;
					t = (P/p)*t + q;
					if (t>j && t<=B) {
						m.insert(t);
					}
				}
				p=p/10;

				//else cout << j << " " << q << endl;

				k--;

			}
			n += m.size();

/*
			stringstream out;
			out << j;
			string s = out.str();
			string t;
			int len = s.length();

			for (i = 1; i < len; i++) {
				t = s.substr(len-i, i) + s.substr(0, len-i);
				//cout << s.substr(len-i, i) << " " << s.substr(0, len-i) << " " << t << endl;
				sscanf(t.c_str(), "%d", &k);
				cout << j << " " << k << endl;
				if (k>j && k<=B) {
					m.insert(k);
					cout << j << " matches " << k << endl;
					//break;
				}
			}*/
		}

		getline(fin, str, '\n');

		fout << "Case #" << I+1 << ": " << n << endl;
		cout << "Case #" << I+1 << ": " << n << endl;

	}
	fin.close();
	fout.close();

	return 0;
}
