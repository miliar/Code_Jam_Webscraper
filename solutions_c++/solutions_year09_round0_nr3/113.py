#include<cstdio>
#include<algorithm>
using namespace std;

const int maxn=500+10;
const char st[]=" welcome to code jam";
const int mod=10000;

char s[maxn];
int f[maxn][maxn];
int test,cases;

int main()
{
	freopen("input.txt","r",stdin);
	
	for (scanf("%d\n",&test);test;test--)
	{
		gets(s+1);
		int n=strlen(s+1);
		for (int i=0;i<=n;i++)
		for (int j=0;j<20;j++)
			f[i][j]=0;
		f[0][0]=1;
		for (int i=0;i<=n;i++)
		for (int j=0;j<20;j++)
		if (f[i][j])
		{
			for (int k=i+1;k<=n;k++)
			if (s[k]==st[j+1])
			{
				f[k][j+1]+=f[i][j];
				if (f[k][j+1]>=mod) f[k][j+1]-=mod;
			}
		}
		int res=0;
		for (int i=0;i<=n;i++)
		{
			res+=f[i][19];
			if (res>=mod) res-=mod;
		}
		printf("Case #%d: %.4d\n",++cases,res);
	}
}
