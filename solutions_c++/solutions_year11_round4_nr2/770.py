/* AnilKishore ( RedAnt ) */

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <algorithm>
#include <string>

#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PI;

#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define F first
#define S second
#define SET(v,x) memset(v,x,sizeof v)
#define FOR(i,a,b) for(int _n(b),i(a);i<_n;i++) 
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(ALL(v))
#define SZ(v) int(v.size())
#define SI ({int x;scanf("%d",&x);x;})
#define SQ(x) ((x)*(x))

#define MX 100005

int R, C, D;
LL w[505][505];
char g[505][505];

double dis(double x1,double y1,double x2,double y2)
{
	return sqrt(SQ(x2-x1)+SQ(y2-y1));	
}

bool ok(int x1,int y1,int x2,int y2)
{
	double cx = x1+(x2-x1+1)/2.0, cy = y1+(y2-y1+1)/2.0;
	double sum = 0.0;
	double sx = 0.0, sy = 0.0;
	for(int i=x1;i<=x2;i++) for(int j=y1;j<=y2;j++)
	{
		if(i==x1&&(j==y1||j==y2)) continue;
		if(i==x2&&(j==y1||j==y2)) continue;
		double x = i+.5, y = j+.5;
		//sum+=dis(x,y,cx,cy)*(D+w[i][j]);
		sx+=(x-cx)*(D+w[i][j]);
		sy+=(y-cy)*(D+w[i][j]);
	}

	//printf("(%d,%d) --> (%d,%d) : (%lf,%lf) -->> %lf\n",x1,y1,x2,y2,cx,cy,sum);
	//printf("(%d,%d) --> (%d,%d) : (%lf,%lf) -->> %lf,%lf\n",x1,y1,x2,y2,cx,cy,sx,sy);

	//return abs(sum) < 1e-9;
	return abs(sx) < 1e-9 && abs(sy) < 1e-9;
}

void solve()
{
	R=SI, C=SI, D=SI;
	REP(i,R) scanf(" %s",g[i]);
	REP(i,R) REP(j,C) w[i][j] = g[i][j]-'0';
	int ans = -1;

	for(int k=min(R,C);k>=3 && ans==-1;k--)
	{
		for(int i=0;i+k<=R && ans==-1;i++) for(int j=0;j+k<=C;j++)
			if(ok(i,j,i+k-1,j+k-1)){ ans=k; break; }
	}

	if(ans==-1) puts("IMPOSSIBLE");
	else printf("%d\n",ans);
}

void run()
{
	for(int kase=1,kases=SI;kase<=kases;kase++)
	{
		printf("Case #%d: ",kase);
		solve();
		//puts("");
	}	
}


int main(int argc, char **argv)
{
	if(argc==2)
	{
		if(argv[1][0]=='s' || argv[1][0]=='S')
		{
			freopen("./../B-small-attempt0.in","r",stdin);
			freopen("B-small-output.out","w",stdout);
		}
	
		if(argv[1][0]=='l' || argv[1][0]=='L')
		{
			freopen("./../B-large.in","r",stdin);
			freopen("B-large-output.out","w",stdout);
		}
	}

	run();
					
	return 0;
}
