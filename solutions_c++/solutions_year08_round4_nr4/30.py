#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

const int maxm = (1 << 16);

int st[20][20], mid[20][20];
int f[maxm][20];

int main() {
	ifstream fin("D-large.txt");
	ofstream fout("outputd-large.txt");
	int cases;
	fin >> cases;

	int k;
	string str;

	int list[20];

	for (int testcase = 1; testcase <= cases; testcase++) {
		fin >> k;
		fin >> str;

		int l = str.length();
		memset(st, 0, sizeof(st));
		memset(mid, 0, sizeof(mid));
		for (int i = 0; i < k; i++) {
			for (int j = 0; j < k; j++) {
				if (i == j)
					continue;
				for (int x = 0; x < (l / k); x++) {
					if (str[x*k+i] != str[x*k+j])
						mid[i][j]++;
					if (x > 0 && str[x*k+i] != str[(x-1)*k+j])
						st[i][j]++;
				}
			}
		}
		int ans = -1;
		for (int s = 0; s < k; s++) {
			memset(f, 0xff, sizeof(f));
			f[(1 << s)][s] = 0;
			for (int m = 0; m < (1 << k); m++) {
				if (!((m >> s) & 1) || m == s)
					continue;
				int count = 0;
				for (int i = 0; i < k; i++) {
					if ((m >> i) & 1) {
						list[count++] = i;
					}
				}
				for (int xlast = 0; xlast < count; xlast++) {
					int last = list[xlast];
					if (last == s)
						continue;
					for (int xlast2 = 0; xlast2 < count; xlast2++) {
						int last2 = list[xlast2];
						if (last2 == last || (last2 == s && count > 2))
							continue;
						int x = f[m ^ (1 << last)][last2];
						if (x == -1) {
							cout << "here\n";
						}
						x += mid[last2][last];
						if (m == ((1 << k) - 1)) {
							x += st[s][last];
						}
						if (f[m][last] == -1 || x < f[m][last])
							f[m][last] = x;
					}
				}
			}
			for (int t = 0; t < k; t++) {
				if (t == s)
					continue;
				if (ans == -1 || f[(1 << k) - 1][t] < ans)
					ans = f[(1 << k)-1][t];
			}
		}
		fout << "Case #" << testcase << ": " << ans+1 << endl;
		cout << "Case #" << testcase << ": " << ans+1 << endl;
	}
	return 0;
}
