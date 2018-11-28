#include <stdio.h>
#include <string.h>
#define MAXN 110

char marked[MAXN][MAXN];
int a[MAXN][MAXN];
int X, Y, r;
int mod=10007;

int main () {
	int i, j, v, u;
	int t, c;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	for (scanf("%d", &t), c=1; c<=t; c++) {
		printf("Case #%d: ", c);
		scanf("%d%d",&X, &Y);
		memset(marked,0,sizeof(marked));		
		for (scanf("%d", &r); r>0; r--) {
			scanf("%d%d", &v, &u);
			marked[v][u]=1;
		}
		memset(a,0,sizeof(a));
		a[1][1]=1;
		for (i=1; i<=X; i++)
			for (j=1; j<=Y; j++) 
				if (!marked[i][j])	{
					if (i>1 && j>2) 
						a[i][j]=(a[i][j]+a[i-1][j-2])%mod;
					if (i>2 && j>1) 
						a[i][j]=(a[i][j]+a[i-2][j-1])%mod;				
				}
		printf("%d\n", a[X][Y]);
	}
	return 0;
}