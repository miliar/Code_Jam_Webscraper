#include <cstdio>
#include <cstring>
using namespace std;
const char *s="welcome to code jam";
const int m=19;
const int maxn=510;
int f[maxn][m+1];
int solve()
{
	static char t[maxn];
	gets(t);
	int n=strlen(t);
	memset(f,0,sizeof(f));
	for(int i=0;i<=n;i++) f[i][0]=1;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			if(t[i-1]==s[j-1])
			{
				f[i][j]=(f[i-1][j]+f[i-1][j-1])%10000;
			}
			else
			{
				f[i][j]=f[i-1][j];
			}
	return f[n][m];
}
int main()
{
	int t;
	scanf("%d\n",&t);
	for(int i=1;i<=t;i++)
		printf("Case #%d: %04d\n",i,solve());
	return 0;
}
