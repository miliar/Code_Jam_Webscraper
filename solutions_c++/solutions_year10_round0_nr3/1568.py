#include <stdio.h>

__int64 g[1000][3], ans, prev;

int main() {
	__int64 t, ti, r, k, n, i, j;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%I64d", &t);
	for(ti=0;ti<t;ti++) {
		scanf("%I64d %I64d %I64d", &r, &k, &n);
		for(i=0;i<n;i++) scanf("%I64d", &g[i][0]);

		for(i=0;i<n;i++) {
			g[i][1]=g[i][0], j=i+1;
			if(j>=n) j-=n;
			while(1) {
				if(g[i][1]+g[j][0]>k || i==j) {
					g[i][2]=j;
					break;
				}
				g[i][1]+=g[j][0], j++;
				if(j>=n) j-=n;
			}
		}

		ans=0, prev=0;
		for(i=0;i<r;i++) ans+=g[prev][1], prev=g[prev][2];
		
		printf("Case #%I64d: %I64d\n", ti+1, ans);

	}
	return 0;
}