#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<string>
#include<queue>
using namespace std;
int n,m,d;
char mp[505][505];
bool ck(int x,int y,int k)
{
	int dx=0,dy=0;
	int ct=k-1;
	for(int i=0;i<k;i++)
	{
		for(int j=0;j<k;j++)
		{
			if(i==0&&j==0) continue;
			if(i==0&&j==k-1) continue;
			if(i==k-1&&j==0) continue;
			if(i==k-1&&j==k-1) continue;
			int w=mp[i+x][j+y]-'0';
			dx+=(2*i-ct)*w;
			dy+=(2*j-ct)*w;
		}
	}
	//printf("%d %d\n",dx,dy);
	return dx==0&&dy==0;
}
int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int _,cas=0;
	scanf("%d",&_);
	while(_--)
	{
		scanf("%d%d%d",&n,&m,&d);
		for(int i=0;i<n;i++) scanf("%s",mp[i]);
		printf("Case #%d: ",++cas);
		bool flag=false;
		for(int k=n;k>=3&&!flag;k--)
		{
			for(int i=0;i+k<=n&&!flag;i++)
				for(int j=0;j+k<=m&&!flag;j++)
				{
					if(ck(i,j,k))
					{
						printf("%d\n",k);
						flag=true;
					}
				}
		}
		if(!flag) puts("IMPOSSIBLE");
	}
}
