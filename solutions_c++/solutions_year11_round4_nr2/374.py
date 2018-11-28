#include <algorithm>
#include <stdio.h>
#include <string.h>
using namespace std;

const double ZERO = 1E-8;

int a[555][555];
int fl[555][555], fr[555][555];
int x, n, m, w;

char s[5555];
int i, j, k, l, p, q, ans, _, __;

inline bool cc(const int x, const int y, const int len) {
	int i, j, x1 = x-len, y1=y-len, x2=x+len,y2=y+len, p, q;
	int fx = 0, fy = 0;
	if (x1<1||y1<1||x2>n||y2>m)return false;
	for (i = -len; i <= len; ++i)
		for (j = -len; j <= len; ++j) {
			p = x + i, q = y + j;
			if ((p==x1||p==x2)&&(q==y1||q==y2)) continue;
			fx += a[p][q] * i ;
			fy += a[p][q] * j;
		}
return !fx && !fy;
}

inline void check(const int len) {
	int tt = len * 2 + 1;
	if (tt > n || tt > m) return ;
	for (i = 1; i <= n; ++i) {
		for (j = 1; j <= m; ++j)
			if (cc(i, j, len)) {
				ans = len * 2 + 1;
				return ;
			}
	}
}

inline bool cc2(const int x, const int y, const int len) {
	int i, j, x1 = x-len +1, y1=y-len+1, x2=x+len,y2=y+len, p, q;
	int fx = 0, fy = 0;
	if (x1<1||y1<1||x2>n||y2>m)return false;
	for (i = -len; i <= len; ++i)
		for (j = -len; j <= len; ++j) {
			p = x + i, q = y + j;
			if(!i||!j)continue;
			if (i<0)++p;
			if(j<0)++q;
			if ((p==x1||p==x2)&&(q==y1||q==y2)) continue;
			fx += a[p][q] * i ;
			fy += a[p][q] * j;
		}
return !fx && !fy;
}

inline void check2(const int len) {
	int tt = len * 2;
	if (tt > n || tt > m) return ;
	for (i = 1; i <= n; ++i) {
		for (j = 1; j <= m; ++j)
			if (cc2(i, j, len)) {
				ans = len * 2;
				return ;
			}
	}
}

int main() {
	scanf("%d", &__);
for (_ = 1; _ <= __; ++_) {
	printf("Case #%d: ", _);
	scanf("%d%d%d", &n, &m, &i);
	for (i = 1; i <= n; ++i) {
		scanf("%s", s + 1);
		for (j = 1; j <= m; ++j) a[i][j] = s[j] - '0';
	}

	ans = -1;
	int pp;
	for (pp = 1; pp <= n && pp <= m; pp += 1) check(pp);
	for (pp = 2; pp <= n && pp <= m; pp += 1) check2(pp);

	if (ans < 3) puts("IMPOSSIBLE");
	else printf("%d\n", ans);
}
	return 0;
}