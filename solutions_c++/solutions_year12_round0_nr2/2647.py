#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int a[1005],dp[105][15];
bool flag[105][15];
int calc1(int x)
{
	int tmp=-1;
	for (int a=0;a<=10;a++)
		for (int b=a;b<=10;b++)
			for (int c=b;c<=10;c++)
				if (a+b+c==x && c-a<=1 && b-a<=1)
					tmp=max(tmp,c);
	return tmp;
}
int calc2(int x)
{
	int tmp=-1;
	for (int a=0;a<=10;a++)
		for (int b=a;b<=10;b++)
			for (int c=b;c<=10;c++)
				if (a+b+c==x && b-a<=2 && c-a==2)
					tmp=max(tmp,c);
	return tmp;
}
int main()
{
	freopen("B-small.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas=1;cas<=T;cas++)
	{
		int n,S,p;
		scanf("%d%d%d",&n,&S,&p);
		for (int i=1;i<=n;i++) scanf("%d",&a[i]);
		memset(dp,0,sizeof(dp));
		memset(flag,false,sizeof(flag));
		flag[0][0]=true;
		for (int i=1;i<=n;i++)
			for (int j=0;j<=S;j++)
			{
				if (!flag[i-1][j]) continue;
				int t1=calc1(a[i]),t2=calc2(a[i]);
				int x=0,y=0;
				if (t1>=p) x=1;
				if (t2>=p) y=1;
				dp[i][j]=max(dp[i][j],dp[i-1][j]+x);
				flag[i][j]=true;
				if (t2!=-1 && j<S)
				{
					flag[i][j+1]=true;
					dp[i][j+1]=max(dp[i][j+1],dp[i-1][j]+y);
				}
			}
		printf("Case #%d: %d\n",cas,dp[n][S]);
	}
}
