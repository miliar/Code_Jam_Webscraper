#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int f[200][200], a[200][200];


int main() {
	ifstream fin("inputd.txt");
	ofstream fout("output.txt");
	int cases;
	fin >> cases;

	int h, w, r, x, y;

	for (int testcase = 1; testcase <= cases; testcase++) {
		fin >> h >> w >> r;
		memset(a, 0, sizeof(a));
		for (int i = 0; i < r; i++) {
			fin >> x >> y;
			a[x-1][y-1] = 1;
		}
		memset(f, 0, sizeof(f));
		f[0][0] = 1;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (a[i][j] == 1)
					continue;
				if (i >= 2 && j >= 1)
					f[i][j] += f[i-2][j-1];
				if (i >= 1 && j >= 2)
					f[i][j] += f[i-1][j-2];
				f[i][j] = f[i][j] % 10007;
			}
		}
		fout << "Case #" << testcase << ": " << f[h-1][w-1] << endl;
	}
	return 0;
}
