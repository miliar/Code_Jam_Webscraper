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

#define NAME "A-large"

#define N 55
int n,k;
char a[N][N];
const int dx[4] = {1,0,1,1};
const int dy[4] = {0,1,-1,1};

const char * ans[4] = {"Neither","Red","Blue","Both"};

int main()
{
	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		fprintf(stderr,"Case %d: \n",test);
		scanf("%d%d",&n,&k);
		REP(i,n) REP(j,n)
		{
			char c;
			do c = getc(stdin);
			while (c!='.'&&c!='R'&&c!='B');
			a[j][n-1-i]=c;
		}
		REP(j,n)
		{
			int ii = n;
			REPD(i,n)
			{
				ii--;
				while (ii>=0&&a[ii][j]=='.')
					ii--;
				if (ii>=0)
					swap(a[i][j],a[ii][j]);
			}
		}
		bool b[2];
		CLEAR(b);
		REP(i,n) REP(j,n) if (a[i][j]!='.') REP(dir,4)
		{
			int p = 0;
			while (p<k)
			{
				int xx = i+p*dx[dir];
				int yy = j+p*dy[dir];
				if (0<=xx&&xx<n&&0<=yy&&yy<n&&a[xx][yy]==a[i][j])
					p++;
				else
					break;
			}
			if (p==k)
				b[a[i][j]=='B']++;
		}
		printf("Case #%d: %s\n",test,ans[b[0]+b[1]*2]);
	}
	return 0;
}