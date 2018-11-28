#include<cstdio>
#include<cstring>
#define base 10000
char s[550];
int test,n,m,F[50][550];
int main()
{
	freopen("code.in","r",stdin);
	freopen("code.out","w",stdout);
	char std[50]=" welcome to code jam";
	n=strlen(std)-1;
	scanf("%d\n",&test);
	int cnt=1;
	for (;test;--test,++cnt)
	{
		printf("Case #%d: ",cnt);
		gets(s+1);
		m=strlen(s+1);
		memset(F,0,sizeof(F));
		for (int i=0;i<=m;++i) F[0][i]=1;
		for (int i=1;i<=n;++i)
		for (int j=1;j<=m;++j)
		if (std[i]==s[j]) F[i][j]=(F[i][j-1]+F[i-1][j-1])%base;
			else F[i][j]=F[i][j-1];
		printf("%.4d\n",F[n][m]);
	}
	return 0;
}
