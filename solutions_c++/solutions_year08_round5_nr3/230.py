#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>

using namespace std;

const int maxn=15;
int a[maxn][1<<11];
char s[maxn][maxn];
bool b[maxn][maxn];
int n,m;

void dp(int x,int y,int q,int p,int value)
{
	bool ff=true;
	if(p>=m)
	{
		if(a[x][y]<value)
			a[x][y]=value;
		return;
	}
	if(p<m-1)
	{
		if(!b[x-1][p+1]!='x'&&(q&(1<<(p+1)))
			||p-1>=0&&!b[x-1][p-1]&&(q&(1<<(p-1)))
			||p-1>=0&&!b[x][p-1]&&(y&(1<<(p-1))))
		ff=false;
	}
	if(ff)
	{
		if(!b[x][p])
			dp(x,y|(1<<p),q,p+2,value+1);
		dp(x,y,q,p+1,value);
	}
	else
		dp(x,y,q,p+1,value);
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	int ii,i,j,maxm,t;
	int nn;
	scanf("%d",&nn);
	for(ii=1;ii<=nn;ii++)
	{
		memset(a,0,sizeof(a));
		scanf("%d%d",&n,&m);
		memset(b,0,sizeof(b));
		for(i=1;i<=n;i++)
		{
			scanf("%s",&s[i]);
			for(j=0;j<m;j++)
			{
				if(s[i][j]=='x')
					b[i][j]=true;
				else
					b[i][j]=false;
			}
		}
		t=(1<<m);
		for(i=0;i<n;i++)
			for(j=0;j<t;j++)
				dp(i+1,0,j,0,a[i][j]);
		maxm=0;
		for(i=0;i<t;i++)
		{
			if(maxm<a[n][i])
				maxm=a[n][i];
		}
		printf("Case #%d: %d\n",ii,maxm);
	}
	return 0;
}