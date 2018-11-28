#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cmath>
using namespace std;

const int MAXN = 100 + 10;
const int MAXM = 1000 + 10;

int n, m;
string s[MAXN];
bool match[MAXN][MAXM];
int f[MAXN][MAXM];

inline void init()
{
	scanf("%d", &n);
	char line[200];
	cin.getline(line, 200);
	for (int i = 0; i < n; ++i) {
		cin.getline(line, 200);
		s[i] = line;
		//printf("%d: %s\n", i, s[i].c_str());
	}
	scanf("%d", &m);
	cin.getline(line, 200);
	memset(match, 0, sizeof(match));
	for (int i = 0; i < m; ++i) {
		cin.getline(line, 200);
		string cur = line;
		for (int j = 0; j < n; ++j) if (cur == s[j]) match[j][i] = true;
	}
}

inline void doit()
{
	for (int i = 0; i < n; i++) if (match[i][0]) f[i][0] = -1; else f[i][0] = 0;
	for (int i = 1; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (match[j][i]) {
				f[j][i] = -1;
			} else {
				f[j][i] = f[j][i - 1];
				for (int k = 0; k < n; k++) if (k != j) {
					if (f[k][i - 1] != -1 && (f[j][i] == -1 || f[k][i - 1] + 1 < f[j][i])) {
						f[j][i] = f[k][i - 1] + 1;
					}
				}
			}
		}
	}
	int ans = -1;
	for (int i = 0; i < n; i++) if (f[i][m - 1] != -1 && (ans == -1 || f[i][m - 1] < ans)) ans = f[i][m - 1];
	printf("%d\n", ans);
}

int main()
{
	int nTest, ttt;
	scanf("%d", &ttt);
	for (nTest = 1; nTest <= ttt; ++nTest) {
		init();
		printf("Case #%d: ", nTest);
		doit();
	}
	return 0;
}
