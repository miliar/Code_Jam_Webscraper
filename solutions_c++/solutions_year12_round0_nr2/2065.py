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

	int T, N, S, p;

	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small.out");

	int n=0, best;
	string str;
	fin >> T;
	getline(fin, str, '\n');

	for (i = 0; i < T; i++) {
		n=0;
		fin >> N >> S >> p;
		for (j = 0; j < N; j++) {
			fin >> k;
			if (k%3==0) {
				best = k/3;
			 	if(best>=p) n++;
				else if(S && best>0 && best+1 >= p && best<10) {
				 	n++;
					S--;
				}
			}
			else if (k%3==2) {
				best=1+(k/3);
				if(best >= p)	n++;
				else if(S && best+1 >= p && best<10) {

					n++;
					S--;

				}
			}
			else {
			 	best = 1+(k/3);
				if(best >= p)	n++;
			}
		}

		getline(fin, str, '\n');

		fout << "Case #" << i+1 << ": " << n << endl;
		cout << "Case #" << i+1 << ": " << n << endl;

	}
	fin.close();
	fout.close();

	return 0;
}
