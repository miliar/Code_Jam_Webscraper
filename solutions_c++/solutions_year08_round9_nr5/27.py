#define _CRT_SECURE_NO_WARNINGS
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
#define MP make_pair
#define PB push_back
#define M_PI       3.14159265358979323846
#define eps 1.0e-11

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;



#define N 16
int n,m;
char d[N][N];
int bitcnt[1<<16],maskcost[1<<16];
int a[N][N][1<<16];
int fx[N],var[N];

#define NAME "E-small-attempt2"

int main()
{
	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	REP(tst,tests)
	{
		fprintf(stderr,"Test #%d\n",tst+1);

		scanf("%d%d",&n,&m);
		REP(i,n) REP(j,m)
		{
			char c;
			do c = getc(stdin);
			while (c!='#'&&c!='?'&&c!='.');
			d[i][j]=c;
		}
		REP(i,n)
		{
			fx[i]=var[i]=0;
			REP(j,m)
			{
				if (d[i][j]=='#')
					fx[i] |= 1<<j;
				if (d[i][j]=='?')
					var[i] |= 1<<j;
			}
		}
		REP(i,1<<16)
		{
			int x=i;
			bitcnt[i]=0;
			for (; x!=0; x&=x-1)
				bitcnt[i]++;
		}
		REP(i,1<<m)
		{
			maskcost[i]=0;
			REP(j,m)
			{
				if (i&(1<<j))
					maskcost[i]+=4;
				if ((i&(1<<j))!=0  && (i&(1<<(j+1)))!=0)
					maskcost[i]-=2;
			}
		}
		CLEAR(a);
		/*if (d[i][j]!='.')
			a[0][0][1]=4;*/
		REP(i,n) REP(j,m) REP(mm,1<<m)
		{
			int ii=i,jj=j;
			jj++;
			if (jj==m)
			{
				jj=0;
				ii++;
			}
			REP(c,2) if (c==0&&d[i][j]=='.' || c==1&&d[i][j]=='#' || d[i][j]=='?')
			{
				int mmm = (mm & ~ (1<<j)) | (c<<j);
				int delta=0;
				if (c==1)
				{
					delta+=4;
					if (mm&(1<<j)) delta-=2;
					if (j>0 && ((mm&(1<<(j-1)))!=0)) delta-=2;
				}
				a[ii][jj][mmm] = max(a[ii][jj][mmm],a[i][j][mm]+delta);
			}
		}
/*		REP(i,n) { fprintf(stderr,"*");
			REP(m1,1<<m)
				for (int mm2 = var[i]; mm2<=var[i]; mm2 = (mm2-1)&(var[i]|1048576))
				{
					int m2 = mm2|fx[i];
					a[i+1][m2] = max(a[i+1][m2],a[i][m1]+maskcost[m2]-2*bitcnt[m2&m1]);
				}
		}*/
		int res=0;
		REP(mm,1<<m)
			res=max(res,a[n][0][mm]);

		printf("Case #%d: %d\n",tst+1,res);
	}
	return 0;
}
