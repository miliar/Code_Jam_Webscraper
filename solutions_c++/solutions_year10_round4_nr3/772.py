#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long int64;
int64 toInt64(string s){int64 r=0;istringstream sin(s);sin>>r;return r;}
#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
const int dx[]={-1,0,1,0,-1,-1,1,1};
const int dy[]={0,-1,0,1,1,-1,1,-1};
int grid[150][150];
bool check()
{
	for(int i=1;i<=100;i++)
			for(int j=1;j<=100;j++)
				if(grid[i][j])
					return false;
	return true;
}
int main()
{
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	//freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);

	//freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	//freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	//freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int cases;
	scanf("%d",&cases);
	for(int cas=1;cas<=cases;cas++)
	{
		int n;
		scanf("%d",&n);
		memset(grid,0,sizeof(grid));
		for(int i=0;i<n;i++)
		{
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(int i=y1;i<=y2;i++)
				for(int j=x1;j<=x2;j++)
					grid[i][j]=1;
		}
		int cnt=0;
		while(!check())
		{
			cnt++;
			int tmp[150][150];
			for(int i=1;i<=100;i++)
				for(int j=1;j<=100;j++)
				{
					if(i==1||j==1)tmp[i][j]=0;
					else if(grid[i-1][j]==0&&grid[i][j-1]==0)tmp[i][j]=0;
					else if(grid[i-1][j]==1&&grid[i][j-1]==1)tmp[i][j]=1;
					else tmp[i][j]=grid[i][j];
				}
			memcpy(grid,tmp,sizeof(tmp));
		}
		printf("Case #%d: %d\n",cas,cnt);
	}
}

