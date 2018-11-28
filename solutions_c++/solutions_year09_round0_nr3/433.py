#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>

using namespace std;

#define MAXN 510

const int P=10000;
const string pat="welcome to code jam";

int n,len,ans,f[20][MAXN];
char s[MAXN];

void dp(int i,int j)
{
	if (i>=19)
	{
		f[i][j]=1;
		return;
	}
	if (j>=len)
	{
		f[i][j]=0;
		return;
	}
	if (f[i][j+1]==-1)
		dp(i,j+1);
	f[i][j]=f[i][j+1];
	if (pat[i]==s[j])
	{
		if (f[i+1][j+1]==-1)
			dp(i+1,j+1);
		f[i][j]+=f[i+1][j+1];
	}
	f[i][j]%=P;
}

void run()
{
	dp(0,0);
	ans=f[0][0]%P;
}

void ini()
{
	int i;
	scanf("%d",&n);
	for (i=1;i<=n;i++)
	{
		scanf("\n");
		gets(s);
		len=strlen(s);
		memset(f,-1,sizeof(f));
		run();
		printf("Case #%d: %04d\n",i,ans);
	}
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	ini();
	return 0;
}
