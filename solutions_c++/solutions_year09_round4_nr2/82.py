#include <stdio.h>
#include <algorithm>
#include <map>

using namespace std;

#define INF 1000000
int r,c,f;
char s[10][10];
int a[10];

bool seen[10][6][1<<6][1<<6][100];

int code(int i) {
	if (i == r) return 0;
	int r = 0;
	for (int j = 0; j < c; ++j) if (s[i][j] == '#')
		r |= 1 << j;
	return r;
}

void go(int l, int i, int v) {
	if (seen[l][i][code(l)][code(l+1)][v]) return;
	seen[l][i][code(l)][code(l+1)][v] = true;
	if (i > 0) { // left
		if (s[l][i-1] != '#') {
			int cl = l;
			while (cl + 1 < r && s[cl+1][i-1] == '.') ++cl;
			if (cl - l <= f) go(cl, i-1, v);
		}
	}
	if (i + 1 < c) { // right
		if (s[l][i+1] != '#') {
			int cl = l;
			while (cl + 1 < r && s[cl+1][i+1] == '.') ++cl;
			if (cl - l <= f) go(cl, i+1, v);
		}
	}
	if (i > 0 && l + 1 < r) {
		if (s[l][i-1] != '#' && s[l+1][i-1] == '#') {
			 s[l+1][i-1] = '.';
			 go(l, i, v + 1);
			 s[l+1][i-1] = '#';
		}
	}
	if (i + 1 < c && l + 1 < r) {
		if (s[l][i+1] != '#' && s[l+1][i+1] == '#') {
			 s[l+1][i+1] = '.';
			 go(l, i, v + 1);
			 s[l+1][i+1] = '#';
		}
	}
}
int solve() {
	scanf("%d%d%d\n", &r, &c, &f);
	for (int i = 0; i < r; ++i) gets(s[i]);
	memset(seen, false, sizeof(seen));
	go(0, 0, 0);
	int res = INF;
	for (int i = 0; i < c; ++i)
		for (int m = 0; m < (1<<c); ++m)
			for (int v = 0; v < 100; ++v)
				if (seen[r-1][i][m][0][v])
					res = min(res, v);
	return res == INF ? -1 : res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		int r = solve();
		if (r != -1) 
			printf("Case #%d: Yes %d\n", i+1, r);
		else
			printf("Case #%d: No\n", i+1);
	}
}