#include<cstdio>
#include<algorithm>
#include<string>
#include<cmath>
#include<vector>
#include<list>
#include<queue>
#include<utility>
using namespace std;
#define ST first
#define ND second
#define PB push_back
#define MP make_pair
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
const int OO=(1<<30);
const bool dbg=1;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); ––x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define MAXN 100
#define P 10007
int w,h,r;
bool fre[MAXN][MAXN];
int way[MAXN][MAXN];
void init()
{
	for(int x=0;x<w;x++)
		for(int y=0;y<h;y++)
		{
			fre[x][y]=1;
			way[x][y]=0;
		}
}
bool onBoard(int x,int y)
{return (x>=0 && y>=0 && x<w && y<h);}
void readCase()
{
	scanf("%d%d%d",&h,&w,&r);
	init();
	for(int i=0;i<r;i++)
	{
		int r,c;
		scanf("%d%d",&r,&c);
		r--;
		c--;
		fre[c][r]=0;
	}
}

void computeCase(int cas)
{
	way[0][0]=1;
	for(int y=0;y<h;y++)
	for(int x=0;x<w;x++)
	{
		if(!fre[x][y]){way[x][y]=0;continue;}
		way[x][y]%=P;
		int xp=x+1,yp=y+2;
		if(onBoard(xp,yp))
		{
			way[xp][yp]+=way[x][y];
		}
		xp=x+2;yp=y+1;
		if(onBoard(xp,yp))
		{
			way[xp][yp]+=way[x][y];
		}
	}
	printf("Case #%d: %d\n",cas,way[w-1][h-1]);
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		readCase();
		computeCase(i+1);
	}
	return 0;
}

