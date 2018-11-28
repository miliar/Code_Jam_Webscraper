#include <algorithm>
#include <iostream>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define sz(a) int((a).size())
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define UN(v) sort(all(v)),(v).erase(unique((v).begin(),(v).end()),(v).end())
#define CL(a,b) memset(a,b,sizeof a)
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int h=111, h2=h*2;

struct P
{
	int x1,x2,y1,y2;
	void inp() { scanf("%d%d%d%d", &y1, &x1, &y2, &x2); }
} a[h];

int r;
bool u[h][h], v[h][h];

int main()
{
#ifdef LocalHost
freopen("c-small-attempt1.in", "r", stdin);//-small-attempt
freopen("c-small-attempt1.out", "w", stdout);//-large
#endif
	int T;
	scanf("%d", &T);
REP(it, T)
{
	scanf("%d", &r);
	REP(i, r) a[i].inp();
	CL(u, 0);
	REP(i, r) FOR(x, a[i].x1, a[i].x2+1) FOR(y, a[i].y1, a[i].y2+1)
		u[x][y]=1;
	int t=0;
	while(1)
	{
		int k=0;
		REP(x, h) REP(y, h) k+=u[x][y];
		if(k==0) break;
		REP(x, h) REP(y, h)
		{
			if(u[x][y])
			{
				if((x==0 || !u[x-1][y]) && (y==0 || !u[x][y-1])) v[x][y]=0;
				else v[x][y]=1;
			}
			else
			{
				if((x!=0 && u[x-1][y]) && (y!=0 && u[x][y-1])) v[x][y]=1;
				else v[x][y]=0;
			}
		}
		REP(x, h) REP(y, h) u[x][y] = v[x][y];
		++t;
	}
	printf("Case #%d: %d\n", it+1, t);
}
	return 0;
}
