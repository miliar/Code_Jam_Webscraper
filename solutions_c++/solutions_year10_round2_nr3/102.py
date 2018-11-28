#include <stdio.h>
#define MN 501
#define MOD 100003
int nck[MN][MN], c[MN][MN];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txT","w",stdout);
	int t, T, i, j, k;

	for (i = 0; i < MN; i++) {
		nck[i][0] = 1;
		for (j = 1; j <= i; j++)
			nck[i][j] = (nck[i-1][j-1]+nck[i-1][j])%MOD;
	}
	for (i = 2; i < MN; i++) {
		c[i][1] = 1;
		for (j = 2; j <= i-1; j++) {
			for (k = 1; k <= j-1; k++)
				c[i][j] = (c[i][j]+(long long)c[j][k]*nck[i-j-1][j-k-1])%MOD;
		}
	}
	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ",t);
		scanf("%d",&i);
		k = 0; for (j = 1; j <= i-1; j++) k = (k+c[i][j])%MOD;
		printf("%d\n",k);
	}
	return 0;
}