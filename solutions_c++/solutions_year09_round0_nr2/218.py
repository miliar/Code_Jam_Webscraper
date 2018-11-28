#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <complex>
#include <queue>
#include <complex>
#include <ctime>
#include <ext/numeric>

using namespace std;
using namespace __gnu_cxx;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (int)(n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
int n,m,cur;
int a[105][105];
int vis[105][105];

void ff(int x,int y)
{
	int mi=-1,mx=199999999;
	rep(i,0,4)
	{
		int nx = x+dx[i];
		int ny = y+dy[i];
		if(nx<0||ny<0||nx>=n||ny>=m)
			continue;
		if(a[x][y]>a[nx][ny])
			if(mx>a[nx][ny])
				mx=a[nx][ny],mi=i;
	}
	if(mi == -1)
	{
		if(vis[x][y]==-1)
			vis[x][y]=cur++;
		return;
	}
	ff(x+dx[mi],y+dy[mi]);
	vis[x][y] = vis[x+dx[mi]][y+dy[mi]];
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("b.in","rt",stdin);
	freopen("b.out","wt",stdout);
#endif
	int t;
	scanf("%d",&t);
	rep(tt,0,t)
	{
		printf("Case #%d:\n",tt+1);
		scanf("%d %d",&n,&m);
		rep(i,0,n)
			rep(j,0,m)
				scanf("%d",&a[i][j]);
		cur = 0;
		memset(vis,-1,sizeof(vis));
		rep(i,0,n)
			rep(j,0,m)
				if(vis[i][j]==-1)
					ff(i,j);
		rep(i,0,n)
		{
			char*s="";
			rep(j,0,m)
				printf("%s%c",s,(char)vis[i][j]+'a'),s=" ";
			printf("\n");
		}
	}
	return 0;
}