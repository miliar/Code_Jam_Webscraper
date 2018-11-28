// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

const int MAXN = 200;

int dv, iv, n, m;
int a[MAXN];
int f[MAXN][300];

void init()
{
	int i;

	scanf("%d%d%d%d", &dv, &iv, &m, &n);
	for (i=0; i<n; i++)
		scanf("%d", &a[i]);
}

void work()
{
	int i, j, k, best;

	memset(f, 0xff, sizeof(f));
	for (i=0; i<=255; i++)
		f[0][i] = abs(a[0]-i);
	for (i=1; i<n; i++)
		for (j=0; j<=255; j++){
			for (k=0; k<=255; k++){
				if (abs(j-k)<=m){
					if (f[i][j]==-1 || f[i][j]>f[i-1][k]+abs(a[i]-j))
						f[i][j] = f[i-1][k]+abs(a[i]-j);
					if (i>1 && (f[i][j]==-1 || f[i][j]>f[i-2][k]+abs(a[i]-j)+dv))
						f[i][j] = f[i-2][k]+abs(a[i]-j)+dv;					
				}
				if (i==1 && (f[i][j]==-1 || f[i][j]>dv+abs(a[i]-j)))
					f[i][j] = dv+abs(a[i]-j);					
				if (m!=0){
				int tp = abs(j-k);
				if (tp!=0 && tp % m == 0)
					tp = tp/m - 1;
				else
					tp = tp/m;
				if  (f[i][j]==-1 || f[i][j]>f[i-1][k]+abs(a[i]-j)+iv*tp)
					f[i][j] = f[i-1][k]+abs(a[i]-j)+iv*tp;
				}
			}
			//printf("%d %d %d\n", i, j, f[i][j]);
		}
	best = -1;
	for (i=0; i<=255; i++)
		if (f[n-1][i]!=-1 && (best==-1 || f[n-1][i]<best))
			best = f[n-1][i];
	printf("%d\n", best);

}

int main()
{
	int t, i;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	i = 0;
	while (t--){
		printf("Case #%d: ", (++i));
		init();
		work();
	}

	return 0;
}
