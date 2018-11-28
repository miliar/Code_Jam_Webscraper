#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
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

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

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
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define NAME "C-small-attempt0"

#define N 128
char a[2][N+1][N+1];

int main()
{
	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	REP(tst,tests)
	{
		fprintf(stderr,"Test #%d\n",tst+1);

		memset(a,'0',sizeof a);
		REP(i,N)
			a[0][i][N]=a[1][i][N]=0;
		int m;
		scanf("%d",&m);
		REP(i,m)
		{
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&y1,&x1,&y2,&x2);
			FOR(x,x1,x2) FOR(y,y1,y2)
				a[0][x][y]='1';
		}
		int cur=0,nw=1;
		int res=0;
		for (; ; res++)
		{
			//REP(i,N) fprintf(stderr,"%s\n",a[cur][i]); fprintf(stderr,"\n");
			bool was = false;
			REP(i,N) REP(j,N)
			{
				a[nw][i][j]=a[cur][i][j];
				if (a[cur][i][j]=='1')
					was=true;
				if (a[cur][i][j] == '1' && (i==0 || a[cur][i-1][j]=='0') && (j==0 || a[cur][i][j-1]=='0'))
					a[nw][i][j]='0';
				if (a[cur][i][j] == '0' && i>0 && a[cur][i-1][j]=='1' && j>0 && a[cur][i][j-1]=='1')
					a[nw][i][j]='1';
			}
			swap(cur,nw);
			if (!was)
				break;
		}
		printf("Case #%d: %d\n",tst+1,res);
	}
	return 0;
}