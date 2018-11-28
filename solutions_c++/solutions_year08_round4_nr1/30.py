#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

const int inf = 1000000;
const int maxn = 30000;

int min(int a, int b) {
	return a > b?b:a;
}
int max(int a, int b) {
	return a > b?a:b;
}

int g[maxn], c[maxn];
int f[maxn][2];

int main() {
	ifstream fin("a-large.txt");
	ofstream fout("outputa-large.txt");
	int cases;
	fin >> cases;

	int m, v;
	for (int testcase = 1; testcase <= cases; testcase++) {
		fin >> m >> v;
		memset(g, 0, sizeof(g));
		memset(c, 0, sizeof(c));
		memset(f, 0, sizeof(f));
		for (int i = 1; i <= (m-1)/2; i++) {
			fin >> g[i] >> c[i];
		}
		memset(f, 0xff, sizeof(f));
		int x;
		for (int i = (m-1)/2+1; i <= m; i++) {
			fin >> x;
			f[i][x] = 0;
			f[i][1-x] = inf;
		}
		for (int i = (m-1)/2; i >= 1; i--) {
			if (g[i] == 0) {
				f[i][0] = f[i*2][0] + f[i*2+1][0];
				if (f[i][0] > inf)
					f[i][0] = inf;
				f[i][1] = min(f[i*2][1] + min(f[i*2+1][0], f[i*2+1][1]), min(f[i*2][0], f[i*2][1]) + f[i*2+1][1]);
				if (f[i][1] > inf)
					f[i][1] = inf;
			}
			else {
				f[i][1] = f[i*2][1] + f[i*2+1][1];
				if (f[i][1] > inf)
					f[i][1] = inf;
				f[i][0] = min(f[i*2][0] + min(f[i*2+1][0], f[i*2+1][1]), min(f[i*2][0], f[i*2][1]) + f[i*2+1][0]);
				if (f[i][0] > inf)
					f[i][0] = inf;
			}
			if (c[i] == 1) {
				if (g[i] == 1) {
					f[i][0] = min(f[i][0], f[i*2][0] + f[i*2+1][0]+1);
					if (f[i][0] > inf)
						f[i][0] = inf;
					f[i][1] = min(f[i][1], min(f[i*2][1] + min(f[i*2+1][0], f[i*2+1][1]), min(f[i*2][0], f[i*2][1]) + f[i*2+1][1])+1);
					if (f[i][1] > inf)
						f[i][1] = inf;
				}
				else {
					f[i][1] = min(f[i][1], f[i*2][1] + f[i*2+1][1]+1);
					if (f[i][1] > inf)
						f[i][1] = inf;
					f[i][0] = min(f[i][0], min(f[i*2][0] + min(f[i*2+1][0], f[i*2+1][1]), min(f[i*2][0], f[i*2][1]) + f[i*2+1][0])+1);
					if (f[i][0] > inf)
						f[i][0] = inf;
				}
			}
		}
		if (f[1][v] >= inf)
			fout << "Case #" << testcase << ": IMPOSSIBLE" << endl;
		else
			fout << "Case #" << testcase << ": " << f[1][v] << endl;
	}
	return 0;
}
