#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
#define oo 600
char s[oo][oo];
int c[oo][oo];
int f[oo][oo];
int Test,Case;
int ans[oo];
int N,M,K;

inline int val(char ch)
{
	if (ch<='9') return ch-'0';
	return ch-'A'+10;
}

inline void Readin()
{
	scanf("%d%d",&N,&M);
	memset(c,-1,sizeof c);
	for (int i=1;i<=N;++i)
	{
		scanf("%s",s[i]+1);
		for (int j=1;j<=M/4;++j)
		{
			c[i][j*4-0]=(bool)(val(s[i][j])&1);
			c[i][j*4-1]=(bool)(val(s[i][j])&2);
			c[i][j*4-2]=(bool)(val(s[i][j])&4);
			c[i][j*4-3]=(bool)(val(s[i][j])&8);
		}
	}
}

inline void Solve()
{
	memset(ans,0,sizeof ans);
	
	K=0;
	while (true)
	{
		int Max=0;
		memset(f,0,sizeof f);
		for (int i=1;i<=N;++i)
			for (int j=1;j<=M;++j)
			if (c[i][j]>=0)
			{
				f[i][j]=1;
				if (c[i-1][j]==(!c[i][j]) && c[i][j-1]==(!c[i][j]))
				{
					int k=min(f[i-1][j],f[i][j-1]);
					if (c[i-k][j-k]==c[i][j])
						++k;
					f[i][j]>?=k;
				}
				Max>?=f[i][j];
			}
		
		if (Max==0) break;
		
		for (int i=1;i<=N;++i)
			for (int j=1;j<=M;++j)
				if (f[i][j]==Max)
				{
					for (int k=i-Max+1;k<=i;++k)
						for (int l=j-Max+1;l<=j;++l)
							if (c[k][l]==-1) goto BK;
					
					for (int k=i-Max+1;k<=i;++k)
						for (int l=j-Max+1;l<=j;++l)
							c[k][l]=-1;
					ans[Max]++;
					BK:;
				}
		K++;
	}
	
	printf("%d\n",K);
	for (int i=N;i>0;--i)
		if (ans[i]) printf("%d %d\n",i,ans[i]);
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
