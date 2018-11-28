#include <cstdio>
#include <cstring>

int opt[2000][19];

char bz[]=" welcome to code jam";
char st[2000];
int i,j,k,I,T;

main()
{
	scanf("%d\n",&T);
	for (I=1;I<=T;++I)
	{
		gets(st);
		memset(opt,0,sizeof opt);
		opt[0][0]=1;
		for (i=0;i<strlen(st);++i)
			for (j=1;j<=19;++j)
				if (bz[j]==st[i])
				    for (k=0;k<=i;++k)
					{
				        opt[i+1][j]+=opt[k][j-1];
				        opt[i+1][j]%=10000;
					}
		int ans=0;
		for (i=0;i<=strlen(st);++i)
		    ans+=opt[i][19];
		ans%=10000;
		printf("Case #%d: %04d\n",I,ans);
	}
	return 0;
}
