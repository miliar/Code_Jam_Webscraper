#include <cstdio>
#include <cstring>
#define n 1005

char s[n][n],res[n][n];
bool mk[n][n];
int T,N,M;
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for (int Te=1;Te<=T;++Te)
	{
		scanf("%d%d",&N,&M);
		for (int i=0;i<N;++i)
			scanf("%s",&s[i]);
		
		printf("Case #%d:\n",Te);
		memset(mk,0,sizeof(mk));
		memset(res,0,sizeof(res));
		for (int i=0;i<N;++i)
		for (int j=0;j<M;++j)
		if (s[i][j]=='#')	mk[i][j]=1;
		
		int ret=0;
		for (int i=0;i<N-1;++i)
		for (int j=0;j<M-1;++j)
		if (mk[i][j])
		{
			if (mk[i+1][j] && mk[i][j+1] && mk[i+1][j+1])
			{
				res[i][j]=res[i+1][j+1]='/';
				res[i][j+1]=res[i+1][j]='\\';
				mk[i][j]=mk[i+1][j]=mk[i][j+1]=mk[i+1][j+1]=0;
			}
			else	ret=1;
		}
		for (int i=0;i<N;++i)
		for (int j=0;j<M;++j)
		if (mk[i][j])	ret=1;
		if (ret)	puts("Impossible");
		else
		for (int i=0;i<N;++i,puts(""))
		for (int j=0;j<M;++j)
		if (!res[i][j])	putchar('.');
		else	putchar(res[i][j]);
	}
	return 0;
}
