#include <stdio.h>
#include <iostream>
#define maxm 20200
using namespace std;
int m,V,t;
int g[maxm];
int c[maxm];
int v[maxm];
int op[maxm][2];
void readin(void)
{
	scanf("%d%d",&m,&V);
	for (int i = 1;i <= (m - 1) / 2;i++) scanf("%d%d",&g[i],&c[i]);
	for (i = (m - 1) / 2 + 1;i <= m;i++) scanf("%d",&v[i]);
}
int Change(int a,int b,int G)
{
	if (G == 1) {return a & b;} else {return a | b;}
}
void work(void)
{
	memset(op,-1,sizeof(op));
	for (int i = (m - 1) / 2 + 1;i <= m;i++) op[i][v[i]] = 0;
	for (i = (m - 1) / 2;i >= 1;i--)
	{
		for (int k1 = 0;k1 < 2;k1++) if (op[i * 2][k1] != -1)
		for (int k2 = 0;k2 < 2;k2++) if (op[i * 2 + 1][k2] != -1)
		{
			int next = Change(k1,k2,g[i]);
			int D = op[i * 2][k1] + op[i * 2 + 1][k2];
			if (op[i][next] == -1 || op[i][next] > D) op[i][next] = D;
		}
		if (c[i] == 1)
		{
			for (int k1 = 0;k1 < 2;k1++) if (op[i * 2][k1] != -1)
			for (int k2 = 0;k2 < 2;k2++) if (op[i * 2 + 1][k2] != -1)
			{
				int next = Change(k1,k2,1 - g[i]);
				int D = op[i * 2][k1] + op[i * 2 + 1][k2] + 1;
				if (op[i][next] == -1 || op[i][next] > D) op[i][next] = D;
			}
		}
	}
}
int main(void)
{
	freopen("a.in.txt","r",stdin);
	freopen("a.out","w",stdout);
	int n;
	scanf("%d",&n);
	for (t = 1;t <= n;t++)
	{
		readin();
		work();
		printf("Case #%d: ",t);
		if (op[1][V] == -1) {printf("IMPOSSIBLE\n");} else {printf("%d\n",op[1][V]);}
	}
	return 0;
}
