#include <cstdio>
#include <cstdlib>
#include <cstring>
#define oo 105
#define nn 260
int Case,Test;
int f[oo][nn];
int I,D,M,N;
int a[oo];

inline void Readin()
{
	scanf("%d%d%d%d",&D,&I,&M,&N);
	for (int i=1;i<=N;++i)
		scanf("%d",a+i);
}

inline void Shortest(int f[])
{
	bool mk[nn]={};
	
	while (true)
	{
		int u=-1;
		for (int j=0;j<=255;++j)
			if (!mk[j] && (u<0 || f[u]>f[j]))
				u=j;
		if (u<0) break;
		
		mk[u]=true;
		for (int j=0;j<=255;++j)
			if (u-M<=j && j<=u+M)
			f[j]<?=f[u]+I;
	}
}

inline void Solve()
{
	memset(f,63,sizeof f);
	for (int i=0;i<=255;++i)
		f[1][i]=0;
	for (int i=1;i<=N;++i)
	{
		for (int j=0;j<=255;++j)
			f[i][j]+=abs(a[i]-j);
		Shortest(f[i]);
		
		if (i>1)
		for (int j=0;j<=255;++j)
			f[i][j]<?=f[i-1][j]+D;
		
		if (i<N)
		for (int j=0;j<=255;++j)
			for (int k=0;k<=255;++k)
				if (k>=j-M && k<=j+M)
					f[i+1][k]<?=f[i][j];
	}
	
	int Ans=1<<30;
	for (int i=0;i<=255;++i)
		Ans<?=f[N][i];
	
	printf("%d\n",Ans);
}

int main()
{
	//freopen("i.txt","r",stdin);
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
