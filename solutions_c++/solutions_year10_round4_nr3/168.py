#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;
typedef long long LL;
#define oo 1005
bool f[2][oo][oo];
int N,M=100;

inline void Readin()
{
	memset(f,0,sizeof f);

	scanf("%d",&N);
	int x1,y1,x2,y2;
	for (int i=1;i<=N;++i)
	{
		scanf("%d%d%d%d",&y1,&x1,&y2,&x2);
		for (int j=x1;j<=x2;++j)
			for (int k=y1;k<=y2;++k)
				f[0][j][k]=true;
	}
}

inline void Solve()
{
	int K=0;
	while (true)
	{
		bool flag=false;
		int c=K+1&1,b=K&1;
		++K;
		for (int i=1;i<=M;++i)
			for (int j=1;j<=M;++j)
				if (f[b][i][j])
				if (f[b][i-1][j] || f[b][i][j-1]) f[c][i][j]=flag=true;
		for (int i=1;i<=M;++i)
			for (int j=1;j<=M;++j)
				if (!f[b][i][j])
				if (f[b][i-1][j] && f[b][i][j-1]) f[c][i][j]=flag=true;
		for (int i=1;i<=M;++i)
			for (int j=1;j<=M;++j)
				if (f[b][i][j]) f[b][i][j]=false;
		
		if (!flag) break;
	}
	
	printf("%d\n",K);
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
