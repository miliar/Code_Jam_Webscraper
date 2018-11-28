#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <sstream>
#include <map>
#include <assert.h>
using namespace std;
const int mod=10007;
int table[1001][1001];
bool rock[1001][1001];
int main()
{
	int t,ca=1;
	for(scanf("%d",&t);t--;)
	{
		int n,m,r;
		scanf("%d %d %d",&n,&m,&r);
		for(int x=0;x<n;x++)
		for(int y=0;y<m;y++)
			rock[x][y]=false,table[x][y]=0;
		for(int i=0;i<r;i++)
		{
			int x,y;
			scanf("%d %d",&x,&y);
			assert(1<=x&&x<=n);
			assert(1<=y&&y<=m);
			rock[x-1][y-1]=true;
		}
		table[0][0]=1;
		for(int x=0;x<n;x++)
		for(int y=0;y<m;y++)
		{
			if(table[x][y]==0)continue;
			int v=table[x][y];
			for(int dx=1;dx<=2;dx++)
			for(int dy=1;dy<=2;dy++)
			{
				//if(dx+dy==0)continue;
				if(dx*dx+dy*dy!=5)continue;
				int nx=dx+x;
				int ny=dy+y;
				if(nx<n&&ny<m&&!rock[nx][ny])
					table[nx][ny]+=v,table[nx][ny]%=mod;
			}
		}
		printf("Case #%d: %d\n",ca++,table[n-1][m-1]);
	}
	return 0;
}
