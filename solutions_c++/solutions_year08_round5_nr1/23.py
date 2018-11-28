#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define NAME "A-large"
#define N 7000

string a;

const int dx[4] = {1,0,-1,0};
const int dy[4] = {0,1,0,-1};

VI byx[N],byy[N];
VPII points;
bool matr[N][N];

int main()
{
	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	REP(tst,tests)
	{
		int l;
		scanf("%d",&l);
		CLEAR(matr);
		a="";
		REP(i,l)
		{
			char buf[100];
			int cnt;
			scanf("%s %d",buf,&cnt);
			string str(buf);
			REP(j,cnt)
				a+=str;
		}
		//fprintf(stderr,"%s\n",a.data());
		int x = N/2, y=N/2;
		int dir=0;
		REP(i,N)
		{
			byx[i].clear();
			byy[i].clear();
		}
		REP(i,a.length())
		{
			if (a[i]=='L')
				dir = (dir+1)%4;
			else if (a[i]=='R')
				dir = (dir+3)%4;
			else
			{
				if (dir == 0)
					byx[x].pb(y);
				else if (dir == 1)
					byy[y].pb(x);
				x += dx[dir];
				y += dy[dir];
				if (dir == 2)
					byx[x].pb(y);
				else if (dir == 3)
					byy[y].pb(x);
			}
		}
		if (!(x==(N/2) && y==(N/2)))
			fprintf(stderr,"Error!");
		REP(x,N)
		{
			SORT(byx[x]);
			for (int i = SZ(byx[x])-3; i>=0; i-=2)
				for (int y = byx[x][i+1]-1; y >= byx[x][i]; y--)
					matr[x][y]=true;
		}
		REP(y,N)
		{
			SORT(byy[y]);
			for (int i = SZ(byy[y])-3; i>=0; i-=2)
				for (int x = byy[y][i+1]-1; x >= byy[y][i]; x--)
					matr[x][y]=true;
		}
		int res=0;
		REP(i,N) REP(j,N)
			if (matr[i][j])
				res++;
		printf("Case #%d: %d\n",tst+1,res);
		fprintf(stderr,"*");
	}
	return 0;
}
