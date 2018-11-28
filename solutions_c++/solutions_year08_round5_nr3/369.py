#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int f[11][2100];
int a[11][11];
int n, m;

int main() {
	ifstream fin("inputc.txt");
	ofstream fout("output.txt");
	int cases;
	fin >> cases;

	memset(a, 0, sizeof(a));
	for (int testcase = 1; testcase <= cases; testcase++) {
		fin >> n >> m;
		memset(a, 0, sizeof(a));
		for (int i = 0; i < n; i++) {
			for (int j= 0; j < m; j++) {
				char ch;
				fin >> ch;
				if (ch == 'x')
					a[i][j] = 1;
			}
		}
		memset(f, 0, sizeof(f));
		for (int i = 0; i < n; i++) {
			for (int st = 0; st < (1 << m); st++) {
				bool ok = true;
				for (int j = 0; j < m; j++) {
					if ( ((st >> j) & 1) && (a[i][j] == 1 || ((st >> (j+1)) & 1)) ) {
						ok = false;
						break;
					}
				}
				if (!ok) continue;
				for (int la = 0; la < (1 << m); la++) {
					ok = true;
					int num = 0;
					for (int j = 0; j < m; j++) {
						if ((st >> j) & 1) {
							num++;
							if ((j > 0 && ((la >> (j-1)) & 1)) || ((la >> (j+1)) & 1)) {
								ok = false;
								break;
							}
						}
					}
					if (ok) {
						if (f[i+1][st] < f[i][la] + num)
							f[i+1][st] = f[i][la] + num;
					}
				}
			}
		}
		int ans = 0;
		for (int i = 0; i < (1 << m); i++) {
			if (ans < f[n][i])
				ans = f[n][i];
		}
		fout << "Case #" << testcase << ": " << ans << endl;
	}
	return 0;
}
