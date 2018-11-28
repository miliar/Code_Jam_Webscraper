#include <cstdio>
#include <algorithm>
using namespace std;

int max(int a, int b) {
	return a < b ? b : a;
}

int T, n, m, sn, mk[10000][27], p[10000], mx, mp, c;
char s[256], o[256], d[10000][16];

bool cmp(int a, int b) {
	return mk[a][c] < mk[b][c];
}

void tt(int l, int s, int a, int b) {
//	printf("%d %d %d %d %d\n", l, s, a, b, p[a]);
	if (a + 1 == b) {
		if (mx < s || mx == s && p[a] < mp)
			mx = s, mp = p[a];
		return;
	}
	c = l;
	if (l)
		c = o[l - 1]&31;
	sort(p + a, p + b, cmp);
	int t = a, cc = c;
	for (int i = a + 1; i < b; ++i)
		if (mk[p[i - 1]][cc] != mk[p[i]][cc])
			tt(l + 1, s + !mk[p[t]][cc], t, i), t = i;
	tt(l + 1, s, t, b);
}

int main() {
	scanf("%d", &T);
	for (int r = 0; r < T; ) {
		printf("Case #%d:", ++r);
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			scanf("%s", d[i]);
			sn = -1;
			while (d[i][++sn]);
			mk[i][0] = sn;
			for (int j = 'a'; j <= 'z'; ++j) {
				mk[i][j&31] = 0;
				for (int k = 0; k < sn; ++k)
					if (d[i][k] == j)
						mk[i][j&31] |= 1 << k;
			}
		}
		/*
		puts("");
		for (int i = 0; i < n; ++i) {
			for (int j = 'a'; j <= 'z'; ++j)
				printf("%c%3d", j, mk[i][j&31]);
			puts("");
		}
		*/
		for (int i = 0; i < n; ++i)
			p[i] = i;
		for (int i = 0; i < m; ++i) {
			scanf("%s", o);
			mx = 0;
			tt(0, 0, 0, n);
			printf(" %s", d[mp]);
		}
		puts("");
	}
	return 0;
}
