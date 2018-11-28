#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
	ofstream fout("D:\\out");
	ifstream fin("D:\\in");
	int testcase, t, d, i, m, n;
	int data[200], dpres[200][256];
	fin >> t;
	for (int testcase = 0; testcase < t; ++testcase) {
		fin >> d >> i >> m >> n;
		for (int j = 0; j < n; ++j) {
			fin >> data[j];
		}

		memset(&dpres[0][0], 0, sizeof(dpres));
		for (int j = 0; j < n; ++j) {
			for (int k1 = 0; k1 < 256; ++k1) {
				int mincost = 100000000;
				if (k1 == data[j]) {
					for (int k2 = 0; k2 < 256; ++k2) {
						if (k1 == k2) {
							mincost = min(mincost, dpres[j][k2]);
						} else {
							if (m != 0) {
								mincost = min(mincost, dpres[j][k2] + i * ((abs(k1 - k2) + m - 1) / m - 1));
							} else {
								mincost = min(mincost, 100000000);
							}
						}
					}
				} else {
					for (int k2 = 0; k2 < 256; ++k2) {
						if (k1 == k2) {
							mincost = min(mincost, dpres[j][k2] + d);
							mincost = min(mincost, dpres[j][k2] + abs(data[j] - k1));
						} else {
							if (m != 0) {
								mincost = min(mincost, dpres[j][k2] + d + i + i * ((abs(k1 - k2) + m - 1) / m - 1));
								mincost = min(mincost, dpres[j][k2] + abs(data[j] - k1) + i * ((abs(k1 - k2) + m - 1) / m - 1));
							} else {
								mincost = min(mincost, 100000000);
							}
						}
					}
				}
				dpres[j + 1][k1] = mincost;
			}
		}
		int result = 100000000;
		for (int j = 0; j < 256; ++j) {
			result = min(result, dpres[n][j]);
		}
		fout << "Case #" << testcase + 1 << ": " << result << endl;
	}

	return 0;
}

