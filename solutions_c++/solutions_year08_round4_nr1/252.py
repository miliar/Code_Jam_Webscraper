#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
const int MAXN = 10010;

int n, m;
int g[MAXN];
int c[MAXN];
int v[MAXN];
int f[MAXN][2];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int cas;
	scanf("%d", &cas);
	for (int kth=1; kth<=cas; kth++)
	{
		scanf("%d%d", &n, &m);
		for (int i=1; i<=(n-1)/2; i++)
			scanf("%d%d", &g[i], &c[i]);
		for (int i=(n+1)/2; i<=n; i++)
			scanf("%d", &v[i]);
		
		memset(f, -1, sizeof(f));
		for (int i=(n+1)/2; i<=n; i++)
			f[i][v[i]] = 0;
		for (int i=(n-1)/2; i>=1; i--)
		{
			int left = 2*i, right = 2*i+1;
			for (int j=0; j<=1; j++)
				if (f[left][j] != -1)
					for (int k=0; k<=1; k++)
						if (f[right][k] != -1)
						{
							if (g[i] == 1)
							{
								int t = j&k;
								if (f[i][t] == -1)
									f[i][t] = f[left][j]+f[right][k];
								else
									f[i][t] = min(f[i][t], f[left][j]+f[right][k]);	
								if (c[i] == 1)
								{
									//t = !t;
									t = j|k;
									if (f[i][t] == -1)
										f[i][t] = f[left][j]+f[right][k]+1;
									else
										f[i][t] = min(f[i][t], f[left][j]+f[right][k]+1);	
								}
							}
							else{
								int t = j|k;
								if (f[i][t] == -1)
									f[i][t] = f[left][j]+f[right][k];
								else
									f[i][t] = min(f[i][t], f[left][j]+f[right][k]);
								if (c[i] == 1)
								{
									t = j&k;
									if (f[i][t] == -1)
										f[i][t] = f[left][j]+f[right][k]+1;
									else
										f[i][t] = min(f[i][t], f[left][j]+f[right][k]+1);	
								}
							}	
						}
		}
		
		printf("Case #%d: ", kth);
		if (f[1][m] == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", f[1][m]);	
	}	
	return 0;
}
