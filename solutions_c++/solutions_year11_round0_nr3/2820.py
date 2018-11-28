#include <iostream>
#include <algorithm>
#include <queue>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("out.txt");

	int caseNo = 0;
	int cn;
	for (fin>>cn; cn>0; --cn) {
		int n;
		fin >> n;

		int in[20];
		for (int i=0; i < n; ++i) {
			fin >> in[i];
		}

		int ans = -1;
		for (int i=1; i < (1<<n)-1; ++i) {
			int a = 0;
			int b = 0;
			int sum = 0;
			for (int j=0; j < n; ++j) {
				if (i & (1<<j)) {
					a ^= in[j];
					sum += in[j];
				}
				else {
					b ^= in[j];
				}
			}
			if (a == b) {
				ans = max(ans, sum);
			}
		}

		fout << "Case #" << ++caseNo << ": ";
		if (ans != -1) fout << ans << endl;
		else fout << "NO" << endl;
	}

	fin.close();
	fout.close();

	return 0;
}
