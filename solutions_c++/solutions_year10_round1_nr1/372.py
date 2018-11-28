#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ofstream fout("D:\\out");
	ifstream fin("D:\\in");
	int t, n, kk;
	fin >> t;
	for (int i = 0; i < t; ++i) {
		fin >> n >> kk;
		int data[55][55];
		char line[55];
		memset(&data[0][0], 0, sizeof(data));
		fin.getline(line, 54);
		for (int j = 0; j < n; ++j) {
			fin.getline(line, 54);
			int ptr = 0;
			for (int k = n - 1; k >= 0; --k) {
				if (line[k] == 'R') data[j][ptr++] = 1;
				else if (line[k] == 'B') data[j][ptr++] = 2;
			}
		}

		bool rwin = false, bwin = false;
		int h[55][55], v[55][55], d[55][55];
		for (int j = 0; j < n; ++j) {
			for (int k = 0; k < n; ++k) {
				if (data[j][k] == 0) continue;
				if (j > 0) {
					v[j][k] = data[j][k] == data[j - 1][k] ? v[j - 1][k] + 1 : 1;
				} else {
					v[j][k] = 1;
				}

				if (k > 0) {
					h[j][k] = data[j][k] == data[j][k - 1] ? h[j][k - 1] + 1 : 1;
				} else {
					h[j][k] = 1;
				}

				if (j > 0 && k > 0) {
					d[j][k] = data[j][k] == data[j - 1][k - 1] ? d[j - 1][k - 1] + 1 : 1;
				} else {
					d[j][k] = 1;
				}

				if (h[j][k] >= kk || v[j][k] >= kk || d[j][k] >= kk) {
					if (data[j][k] == 1) rwin = true;
					else bwin = true;
				}
			}
		}

		for (int j = 0; j < n; ++j) {
			int rseq = 1, bseq = 1;
			for (int k = 1; j - k >= 0; ++k) {
				if (data[k][j - k] == 0) {
					rseq = bseq = 0;
				} else if (data[k][j - k] == 1) {
					if (data[k - 1][j - k + 1] == 1) {
						++rseq;
					} else {
						rseq = 1;
					}
					 bseq = 0;
				} else {
					if (data[k - 1][j - k + 1] == 2) {
						++bseq;
					} else {
						bseq = 1;
					}
					 rseq = 0;
				}
				if (rseq >= kk)
					rwin = true;
				if (bseq >= kk)
					bwin = true;
			}
		}

		if (rwin && bwin) {
			fout << "Case #" << i + 1 << ": Both" << endl;
		} else if (rwin && !bwin) {
			fout << "Case #" << i + 1 << ": Red" << endl;
		} else if (bwin && !rwin) {
			fout << "Case #" << i + 1 << ": Blue" << endl;
		} else {
			fout << "Case #" << i + 1 << ": Neither" << endl;
		}
	}

	return 0;
}

