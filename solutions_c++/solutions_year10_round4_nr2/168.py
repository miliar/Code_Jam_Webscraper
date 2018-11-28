#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;
typedef long long LL;
#define oo 2005
int a[oo];
int f[oo][15][15];
int c[15][oo];
int N;

inline void Readin()
{
	scanf("%d",&N);
	for (int i=0;i<(1<<N);++i)
		scanf("%d",a+i);
	for (int i=N-1;i>=0;--i)
		for (int j=0;j<(1<<i);++j)
			scanf("%d",c[i]+j);
}

inline void Solve()
{
	memset(f,63,sizeof f);

	for (int i=0;i<(1<<N);++i)
		for (int j=N-a[i];j<=N;++j)
			f[i][N][j]=0;
	
	for (int i=N-1;i>=0;--i)
		for (int j=0;j<(1<<i);++j)
			for (int k=0;k<=N;++k)
			{
				if (k)
				f[j][i][k]<?=f[j][i][k-1];
				for (int l=1;l>=0;--l)
				{
					f[j][i][k]<?=f[j*2][i+1][k+l]+f[j*2+1][i+1][k+l]+l*c[i][j];
				}
			}
	
	printf("%d\n",f[0][0][0]);
}

int main()
{
	//freopen("i.txt","r",stdin);
	
	int Test,Case=0;
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
