#include <cstdio>
#include <cstring>
typedef long long LL;

LL R, k, N;
LL g[1024], a[1024][2];
int main() {
	int T; scanf("%d", &T);
	for (int cas=0;cas<T;++cas) {
		memset(a, -1, sizeof(a));
		LL ret = 0;
		scanf("%d%d%d", &R, &k, &N);
		for (int i=0;i<N;++i) scanf("%d", g+i);
		LL m = 0, gp = 0;
		for (LL i=1;i<=R;++i) {
			a[gp][0] = ret;
			a[gp][1] = i;
			LL j = gp;
			for (m=0,j=gp;m+g[j]<=k;) {
				m+=g[j];
				++j; if (j>=N) j=0;
				if (j==gp) break;
			}
			gp = j;
			ret += m;
			if (a[gp][1] != -1) {
				LL tmp = ret - a[gp][0];
				LL rnd = i - a[gp][1] + 1;
				ret += tmp * ((R - i) / rnd);
				i += (R - i) / rnd * rnd;
			}
		}
		printf("Case #%d: %lld\n", cas+1, ret);
	}
	return 0;
}
