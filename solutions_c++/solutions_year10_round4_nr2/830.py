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
struct node
{
	int x,y;
};
node v[2000];
bool cmp(const node &A,const node &B)
{
	return A.x>B.x;
}
int grid[2000][20],cost[2000];
bool buy[2000];
int main()
{
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
	//freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);

	//freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	//freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	//freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int cases;
	scanf("%d",&cases);
	for(int cas=1;cas<=cases;cas++)
	{
		int n,r;
		memset(buy,0,sizeof(buy));
		scanf("%d",&r);
		n=1<<r;
		for(int i=0;i<n;i++)
		{
			scanf("%d",&v[i].x);
			if(v[i].x>r)v[i].x=r;
			v[i].x=r-v[i].x;
			v[i].y=i;
		}
		for(int i=0;i<n-1;i++)
			scanf("%d",&cost[i]);
		int pt=2;
		for(int ct=0,i=0;i<r;i++)
		{
			for(int j=0;j<n;j+=pt)
			{
				for(int k=0;k<pt;k++)
					grid[k+j][i]=ct;
				ct++;
			}
			pt*=2;
		}
		sort(v,v+n,cmp);
		int ans=0;
		for(int i=0;i<n;i++)
		{
			for(int j=r-1;v[i].x&&j>=0;j--)
				if(buy[grid[v[i].y][j]])v[i].x--;
				else
				{
					v[i].x--;
					ans+=cost[grid[v[i].y][j]];
					buy[grid[v[i].y][j]]=true;
				}
		}
		printf("Case #%d: %d\n",cas,ans);

	}
}

