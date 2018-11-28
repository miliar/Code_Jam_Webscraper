#include<iostream>
#include<vector>
#include<algorithm>
#include<functional>
#include<queue>
using namespace std;

#define M 10000

char s[505],w[20]="welcome to code jam";
int f[505][20];

int main()
{
	int t,c,i,j,k,n;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	getchar();
	for(c=1;c<=t;c++)
	{
		gets(s);
		n=strlen(s);
		memset(f,0,sizeof(f));
		for(i=0;i<n;i++)
			for(j=0;j<19;j++)
			{
				if(s[i]!=w[j])
					continue;
				if(j==0)
				{
					f[i][0]=1;
					continue;
				}
				for(k=0;k<i;k++)
					f[i][j]=(f[i][j]+f[k][j-1])%M;
			}
		int ans=0;
		for(i=0;i<n;i++)
			ans=(ans+f[i][18])%M;
		printf("Case #%d: %04d\n",c,ans);
	}
}