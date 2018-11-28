#include<stdio.h>

#define MOD 10007

int a[111][111], n, m, D[111][111];
int K;

int main(void)
{
	int T;
	int l0, l1, l2, l3, l4;
	int t1, t2;

	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %d %d",&n,&m,&K);

		for(l1=1;l1<=n;l1++) for(l2=1;l2<=m;l2++) a[l1][l2] = D[l1][l2] = 0;
		D[1][1] = 1;
		for(l1=0;l1<K;l1++)
		{
			scanf("%d %d",&t1,&t2);
			a[t1][t2] = 1;
		}

		for(l1=1;l1<=n;l1++)
		{
			for(l2=1;l2<=m;l2++)
			{
				if(a[l1][l2]) continue;
				l3 = l1 - 1;
				l4 = l2 - 2;
				if(1 <= l3 && 1 <= l4) D[l1][l2] = (D[l1][l2] + D[l3][l4]) % MOD;

				l3 = l1 - 2;
				l4 = l2 - 1;
				if(1 <= l3 && 1 <= l4) D[l1][l2] = (D[l1][l2] + D[l3][l4]) % MOD;
			}
		}

		printf("Case #%d: %d\n",l0,D[n][m]);
	}

	return 0;
}