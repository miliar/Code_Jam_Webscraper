#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	int t, l, i, j, k, p;
	string s;
	int v[25] = {0};
	int ap[10] = {0};
	ifstream fin ("B-large.in");
	ofstream fout ("test.out");

	fin >> t;
	
	for (i = 1; i <= t; i++) {
		fout << "Case #" << i << ": ";
		fin >> s;
		l = s.length();
		for (j = 0; j < l; j++) v[j] = (int) (s[j] - '0');
		for (j = 0; j < 10; j++) ap[j] = 0;
		for (j = l - 1; j >= 0; j--) {
			for (k = v[j] + 1; k < 10; k++) 
				if (ap[k] > 0) 
					break;
			if (k == 10) {
				ap[v[j]]++;
				continue;
			}
			for (p = 0; p < j; p++) fout << v[p];
			fout << k; ap[k]--; ap[v[j]]++;
			for (p = 0; p < 10; p++) {
				while (ap[p] != 0) {
					fout << p;
					ap[p]--;
				}
			}
			fout << "\n";
			break;
		}
		if (j < 0) {
			p = 1;
			while (p < 10) {
				if (ap[p] != 0) break;
				else p++;
			}
			fout << p;
			ap[p]--;
			fout << "0";
			for (p = 0; p < 10; p++) {
				while (ap[p] != 0) {
					fout << p;
					ap[p]--;
				}
			}
			fout << "\n";
		}
	}
	fin.close();
	fout.close();
	return 0;
}