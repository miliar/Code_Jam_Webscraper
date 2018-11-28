#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream fin("Asmall.in");
	ofstream fout("Asmall.out");
	int caseNum, a[1000];
	fin >> caseNum;
	for (int cases = 1; cases <= caseNum; cases++) {
		int n;
		fin >> n;
		char * s = new char[255];
		for (int i = 1; i <= n; i++) {
			fin >> s;
			a[i] = 0;
			for (int j = n - 1; j >= 0; j--) {
				if (s[j] == '1') {
					a[i] = j + 1;
					break;
				}
			}
		}
		int ans = 0;
		while (1) {
			//find
			int max = -1, pos = -1;
			for (int i = n; i > 0; i--) {
				if (a[i] > i) {
					if (a[i] > max) {
						max = a[i];
						pos = i;
					}
				}
			}
			if (max < 0) break;
			while (a[pos] > pos) {
				if (a[pos + 1] <= pos) {
					swap(a[pos], a[pos+1]);
					ans ++;
					pos ++;
				} else {
					int i;
					for (i = pos + 1; i <= n; i++)
						if (a[i] <= pos) break;
					if (i > n || a[i] > pos) cout << "no answer!" << endl;
					ans += (i - pos);
					for (int j = i; j > pos; j--)
						swap(a[j], a[j-1]);

					pos ++;
				}
			}

		}
		fout << "Case #" << cases << ": " << ans << endl;

	}
	fin.close();
	fout.close();
}