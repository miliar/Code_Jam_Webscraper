#include <stdio.h>
#define MN 50
int N, K, B, T, r;
int X[MN], V[MN];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txT","w",stdout);
	int t, asdf, i, j;

	scanf("%d",&asdf);
	for (t = 1; t <= asdf; t++) {
		printf("Case #%d: ",t);
		scanf("%d%d%d%d",&N,&K,&B,&T);
		for (i = 0; i < N; i++) scanf("%d",&X[i]);
		for (i = 0; i < N; i++) scanf("%d",&V[i]);
		r = 0; j = 0;
		for (i = N-1; i >= 0; i--) {
			if (X[i]+V[i]*T < B) ++j;
			else r += j;
			if (N-i-j == K) {
				printf("%d\n",r);
				break;
			}
		}
		if (i < 0) printf("IMPOSSIBLE\n");
	}
	return 0;
}