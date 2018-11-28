#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


int main() {
	vector<string> wd;
	string pat, s;
	long l, d, n, sol, i, j, k, ok;
	long b[16];

	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("out.txt");

	fin >> l >> d >> n;
	for (i = 0; i < d; i++) {
		fin >> s;
		wd.push_back(s);
	}
	for (i = 0; i < n; i++) {
		sol = 0;
		fin >> pat;
		for (j = 0; j < 16; j++) b[j] = 0;
		for (j = 0, k = 0, ok = 1; j < pat.length(); ) {
			if (pat[j] == '(') j++, ok = 0;
			else if (pat[j] == ')') j++, ok = 1, k++;
			else {
				b[k] |= (long) (1 << (int) (pat[j] - 'a'));
				j++;
				k += ok;
			}
		}
		for (j = 0; j < d; j++) {
			ok = 1;
			for (k = 0; k < l; k++) {
				ok = ( (long) (1 << (int) (wd[j][k] - 'a')) & b[k] ) ? ok : 0;
				ok = ok;
			}
			sol += ok;
		}
		fout << "Case #" << i + 1 << ": " << sol << "\n"; 
	}
	fin.close();
	fout.close();
	return 0;
}