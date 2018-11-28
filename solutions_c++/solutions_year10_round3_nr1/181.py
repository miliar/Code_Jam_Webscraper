#include <cstdio>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)

int t, ans, n;
const int M = 10000;
int a[M], b[M];

int sign(int x) { return x > 0 ? 1 : -1; }

int main() {
	scanf("%d", &t);
	FOR(zz,1,t+1) {
		ans = 0;
		scanf("%d", &n);
		FOR(i,0,n) scanf("%d%d", a+i,b+i);
		FOR(i,0,n) FOR(j,i+1,n) {
			if (sign(a[i]-a[j]) != sign(b[i]-b[j]))
				ans++;
		}
		printf("Case #%d: %d\n", zz, ans);
	}
}
