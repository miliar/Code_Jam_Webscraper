#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
short f[2000][2000];
bool ok[2100];
int one[2100], t[2100];
int ans[2100];
int l[2100];

int main() {
	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	int c;
	fin >> c;
	
	for (int ti = 1; ti <= c; ti++) {
		int n, m;
		int x, y;
		fin >> n >> m;
		memset(ok, 0, sizeof(ok));
		memset(f, 0xff, sizeof(f));
		memset(one, 0xff, sizeof(one));
		int op = 0;
		int cl = -1;
		for (int i = 0; i < m; i++) {
			fin >> t[i];
			for (int j = 0; j < t[i]; j++) {
				fin >> x >> y;
				x--;
				if (f[i][x] != -1 && f[i][x] != y)
					ok[i] = 1;
				f[i][x] = y;
				if (y == 1) {
					one[i] = x;
				}
			}
			if (t[i] == 1 && one[i] != -1) {
				l[++cl] = i;
			}
		}
		memset(ans, 0, sizeof(ans));
		bool imp = false;
		while (op <= cl) {
			int x = one[l[op]];
			ans[x] = 1;
			for (int i = 0; i < m; i++) {
				if (ok[i])
					continue;
				if (one[i] == x) {
					ok[i] = true;
					continue;
				}
				if (f[i][x] == 0) {
					t[i]--;
					if (t[i] == 0) {
						imp = true;
						break;
					}
					if (t[i] == 1 && one[i] != -1) {
						ok[i] = true;
						l[++cl] = i;
					}
				}
			}
			if (imp)
				break;
			op++;
		}
		fout << "Case #" << ti << ":";
		if (imp) {
			fout << " IMPOSSIBLE\n";
		}
		else {
			for (int i = 0; i < n; i++) {
				fout << ' ' << ans[i];
			}
			fout << endl;
		}
		cout << "Case " << ti << " Complete" << endl;
	}
	return 0;
}
