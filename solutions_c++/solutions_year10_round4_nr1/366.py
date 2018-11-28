#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
	int t;
	ofstream fout("D:\\out");
	ifstream fin("D:\\in");
	fin >> t;
	for (int testcase = 0; testcase < t; ++testcase) {
		int k, diamond[55][55];
		fin >> k;
		for (int i = 0; i < 2 * k - 1; ++i) {
			for (int j = 0; j < k - abs(k - i - 1); ++j) {
				if (i < k)
					fin >> diamond[i - j][j];
				else
					fin >> diamond[k - 1 - j][i - k + j + 1];
			}
		}
		int hsym[110], vsym[110];
		memset(hsym, 0, sizeof(hsym));
		memset(vsym, 0, sizeof(vsym));

		for (int h = 0; h < 2 * k - 1; ++h) {
			hsym[h] = 1;
			for (int i = 0; i < k; ++i) {
				for (int j = 0; j < k; ++j) {
					if (h - i < 0 || h - i >= k || h - j < 0 || h - j >= k)
						continue;
					if (diamond[i][j] != diamond[h - j][h - i]) {
						hsym[h] = 0;
						goto HSYM_OUT;
					}
				}
			}
HSYM_OUT:
			;
		}

		for (int v = 0; v < 2 * k - 1; ++v) {
			vsym[v] = 1;
			for (int i = 0; i < k; ++i) {
				for (int j = 0; j < k; ++j) {
					if (k - 1 - v + i < 0 || k - 1 - v + i >= k || j - (k - 1 - v) < 0 || j - (k - 1 - v) >= k)
						continue;
					if (diamond[j][i] != diamond[k - 1 - v + i][j - (k - 1 - v)]) {
						vsym[v] = 0;
						goto VSYM_OUT;
					}
				}
			}
VSYM_OUT:
			;
		}

		int result = 1000000000;
		for (int i = 0; i < 2 * k - 1; ++i) {
			if (!hsym[i])
				continue;
			for (int j = 0; j < 2 * k - 1; ++j) {
				if (!vsym[j])
					continue;
				int d = k + abs(k - 1 - i) + abs(k - 1 - j);
				result = min(result, d * d - k * k);
			}
		}
		fout << "Case #" << testcase + 1 << ": " << result << endl;
	}

	return 0;
}

