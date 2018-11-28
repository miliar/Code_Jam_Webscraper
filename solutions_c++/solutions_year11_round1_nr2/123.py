#include <iostream>
#include <cstdio>
#include <math.h>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
const int maxn = 10000+5;
string d[maxn], w[maxn], stw;
bool mark[maxn];
bool map[maxn][26];
int g[100];
int n, m;

int calc()
{
	bool ind, inall, bj;
	int ans = -1, s = 0;
	int tmp;
	int round, r;
	for (int i = 0; i != n; ++i) {
		tmp = 0;
		round = d[i].length();
		for (int j = 0; j != n; ++j)
			if (d[j].length() != round) mark[j] = false;
			else mark[j] = true;
		for (int t = 1; t <= stw.length(); ++t) {
			inall = false;
			for (int j = 0; j != n; ++j)
				if (mark[j] && map[j][stw[t-1]-'a']) {
					inall = true;
					break;
				}
			if (! inall) continue;
			if (! map[i][stw[t-1]-'a']) {
				++tmp;
				for (int j = 0; j != n; ++j)
					if (map[j][stw[t-1]-'a']) mark[j] = false;
			} else {
				g[0] = 0;
				for (int j = 0; j != d[i].length(); ++j)
					if (d[i][j] == stw[t-1]) g[++g[0]] = j;
				for (int k = 0; k != n; ++k)
					if (mark[k] && map[k][stw[t-1]-'a']) {
						bj = true;
						r = 0;
						for (int j = 0; j != d[k].length(); ++j)
							if (d[k][j] == stw[t-1]) {
								++r;
								if (r>g[0] || g[r]!=j) {
									bj = false; break;
								}
							}
						if (r!=g[0]) bj = false;
						mark[k] = bj;
					} else mark[k] = false;
			}
		}
		if (tmp>ans) {
			ans = tmp;
			s = i;
		}
	}
	return s;
}

void init()
{
	memset(map,0,sizeof(map));
	cin >> n >> m;
	for (int i = 0; i != n; ++i) {
		cin >> d[i];
		for (int j = 0; j != d[i].length(); ++j) 
			map[i][d[i][j]-'a'] = true;
	}
	for (int i = 0; i != m; ++i) cin >> w[i];
}

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B.out","w",stdout);

	long TextNum, Tnum = 0, na;
	cin >> TextNum;
	while (TextNum--) {
		cout << "Case #" << ++Tnum << ":";
		init();
		for (int i = 0; i != m; ++i) {
			stw = w[i];
			na = calc();
			cout<< " ";
			for (int i = 0; i != d[na].length(); ++i) cout << d[na][i];
		}
		cout << endl;
	}
	return 0;
}