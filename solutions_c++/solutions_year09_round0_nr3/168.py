#include <cstdio>
#include <cstring>

char s0[25]="\0welcome to code jam",now[505];
int f[505][25];
int main()
{
	int N,i,j;
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d\n",&N);
	int len2=strlen(s0+1);
	for (int T=1;T<=N;++T)
	{
		gets(now+1);
		memset(f,0,sizeof(f));
		int len1=strlen(now+1);
		for (i=0;i<=len1;++i)
			f[i][0]=1;
		for (i=1;i<=len1;++i)
		for (j=1;j<=len2;++j)
		if (now[i]==s0[j])
			f[i][j]=(f[i-1][j-1]+f[i-1][j])%10000;
		else 
			f[i][j]=f[i-1][j];
		printf("Case #%d: %04d\n",T,f[len1][len2]);
	}
	return 0;
}
			
