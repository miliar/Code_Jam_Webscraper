#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

bool b[35][15][2];
int a[105][2];
int T;
int n,s,p;
int f[105][105];

void init()
{
	for(int i=0;i<=10;i++)
		for(int j=i;j<=i+2;j++)
			for(int k=j;k<=i+2;k++)
			{
				if(k-i==2)
					b[i+j+k][k][1]=true;
				else
					b[i+j+k][k][0]=true;
			}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	init();
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		scanf("%d%d%d",&n,&s,&p);
		memset(a,0,sizeof(a));
		for(int i=0;i<n;i++)
		{
			int tmp;
			scanf("%d",&tmp);
			for(int j=p;j<=10;j++)
			{
				a[i+1][0]|=b[tmp][j][0];
				a[i+1][1]|=b[tmp][j][1];
			}
		}
		for(int i=1;i<=n;i++)
			for(int j=0;j<=s;j++)
			{
				if(j)
					f[i][j]=max(f[i-1][j]+a[i][0],f[i-1][j-1]+a[i][1]);
				else
					f[i][j]=f[i-1][j]+a[i][0];
			}
		printf("Case #%d: %d\n",test,f[n][s]);
	}
	return 0;
}

