// ConsoleApplication2.cpp : 定义控制台应用程序的入口点。
//
/*
#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <utility>
#include <cstring>
#include <cstdio>

using namespace std;

int tot;
typedef long long LL;
typedef pair<LL, LL> PLL;

PLL c[20005];
LL ans[10005];
bool v[10005];

char s[20];
bool ispalin(LL t) {
	memset(s, 0, sizeof(s));
	sprintf(s, "%lld", t);
	int l = strlen(s);
	for (int i = 0; i + i < l; ++i)
		if (s[i] != s[l - 1 - i]) return false;
	return true;
}


int _tmain(int argc, _TCHAR* argv[])
{
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);
	scanf("%d", &tot);
	long long a, b;
	int n = 0;
	for (int i = 0; i < tot; ++i) {
		cin >> a >> b;
		c[n++] = make_pair(a - 1, i);
		c[n++] = make_pair(b, i);
	}
	sort(c, c + n);
	
	memset(v, 0, sizeof(v));
	long long x = 0, cnt = 0;
	for (int i = 0; i < n; ++i) {
		while (1) {
			long long t = (x + 1) * (x + 1);
			if (t > c[i].first) break;
			++x;
			if (ispalin(x) && ispalin(t)) ++cnt;
		}
		int t = c[i].second;
		if (!v[t]) ans[t] = cnt, v[t] = 1;
		else ans[t] = cnt - ans[t];
	}
	for (int i = 0; i < tot; ++i) cout << "Case #" << i + 1 << ':' << ' ' << ans[i] << '\n';
}

*/
#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <utility>
#include <cstring>
#include <cstdio>

using namespace std;

bool xwon(char c[5][5]) {
	bool f;
	for (int j = 0; j < 4; ++j) {
		f = 1;
		for (int i = 0; i < 4; ++i) if (c[i][j] != 'T' && c[i][j] != 'X'){ f = 0; break; }
		if (f) return 1;
		f = 1;
		for (int i = 0; i < 4; ++i) if (c[j][i] != 'T' && c[j][i] != 'X'){ f = 0; break; }
		if (f) return 1;
	}
	f = 1;
	for (int i = 0; i < 4; ++i) if (c[i][i] != 'T' && c[i][i] != 'X'){ f = 0; break; }
	if (f) return 1;
	f = 1;
	for (int i = 0; i < 4; ++i) if (c[i][3 - i] != 'T' && c[i][3 - i] != 'X'){ f = 0; break; }
	if (f) return 1;
	return 0;
}

bool owon(char c[5][5]) {
	bool f;
	for (int j = 0; j < 4; ++j) {
		f = 1;
		for (int i = 0; i < 4; ++i) if (c[i][j] != 'T' && c[i][j] != 'O'){ f = 0; break; }
		if (f) return 1;
		f = 1;
		for (int i = 0; i < 4; ++i) if (c[j][i] != 'T' && c[j][i] != 'O'){ f = 0; break; }
		if (f) return 1;
	}
	f = 1;
	for (int i = 0; i < 4; ++i) if (c[i][i] != 'T' && c[i][i] != 'O'){ f = 0; break; }
	if (f) return 1;
	f = 1;
	for (int i = 0; i < 4; ++i) if (c[i][3 - i] != 'T' && c[i][3 - i] != 'O'){ f = 0; break; }
	if (f) return 1;
	return 0;
}

bool draw(char c[5][5]) {
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j) if (c[i][j] == '.') return 0;
	return 1;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);
	char c[5][5];
	int tot;
	scanf("%d", &tot);
	for (int i = 0; i < tot; ++i) {
		memset(c, 0, sizeof(c));
		scanf("%s%s%s%s", c[0], c[1], c[2], c[3]);
		cout << "Case #" << i + 1 << ": ";
		if (xwon(c))
			cout << "X won\n";
		else if (owon(c))
			cout << "O won\n";
		else if (draw(c))
			cout << "Draw\n";
		else
			cout << "Game has not completed\n";
	}
}