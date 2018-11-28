// short limit: 32767
// int limit  : 2147483647

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <iterator>
#include <sstream>
#include <list>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <ctime>
#include <climits>
#include <cassert>
#include <cstring>

using namespace std;

#define FOR(i,n) for(int i=0; i<(n); i++)
#define FORAB(i,a,b) for(int i=(a); i<=(b); i++)
#define RFOR(i,n) for(int i=(n)-1; i>=0; i--)
#define RFORAB(i,a,b) for(int i=(a); i>=(b); i--)

#define FOR64(i,n) for(long long i=0; i<(n); i++)
#define FORAB64(i,a,b) for(long long i=(a); i<=(b); i++)
#define RFOR64(i,n) for(long long i=(n)-1; i>=0; i--)
#define RFORAB64(i,a,b) for(long long i=(a); i>=(b); i--)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REVERSE(c) (reverse(ALL(c)))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define SIZE(c) ((int)(c).size())
#define MP(X,Y) make_pair(X,Y)
#define PB push_back

#define EQ(E, F) (fabs((E)-(F))<=eps)

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
typedef unsigned long long ULL;

const double eps = 1e-11;
const double pi = acos(-1.0);

int N, W, L;
VI r;
VPII coord;

template<class T> inline T sqr(T x){return x*x;}

inline double dist(double x1,double y1,double x2,double y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}

void solve()
{
	r.clear();
	coord.clear();

	scanf("%d %d %d\n", &N, &W, &L);
	FOR(i, N)
	{
		int rad;
		scanf("%d", &rad);
		r.PB(rad);
	}

	//SORT(r);
	//REVERSE(r);

	FOR(i, SIZE(r))
	{
		int x = 0;
		int y = 0;
start:;
		FOR(j, i)
		{
			while (((double) r[i] + (double) r[j]) > (dist((double) coord[j].first, (double) coord[j].second, (double) x, (double) y) + eps))
			{
				int px = coord[j].first + r[j] + r[i];
				int py = coord[j].second + r[j] + r[i];

				if (x > px || y > py)
				{
					cerr << endl << "SICTIK 1: " << x << " " << y << " " << px << " " << py << endl;
					break;
				}

				if (px < py && px <= W)
				{
					x = px;
				}
				else if (py <= L)
				{
					y = py;
				}
				else if (px <= W)
				{
					x = px;
				}
				else
				{
					cerr << endl << "SICTIK 2: " << W << " " << L << " " << px << " " << py << endl;
					break;
				}
			}
		}
		FOR(j, i)
		{
			if (((double) r[i] + (double) r[j]) > (dist((double) coord[j].first, (double) coord[j].second, (double) x, (double) y) + eps))
			{
				goto start;
			}
		}

		coord.PB(MP(x,y));

		printf(" %d %d", x, y);
	}

	FOR(i, SIZE(r))
	{
		FOR(j, i)
		{
			if (((double) r[i] + (double) r[j]) > (dist((double) coord[j].first, (double) coord[j].second, (double) coord[i].first, (double) coord[i].second) + eps))
			{
				cerr << "ABOOO" << endl;
			}
		}
	}



	//assert(scanf("%[a-z ]\n", str) == 1);
}

int main()
{
	//freopen(".in","r",stdin);
	//freopen(__FILE__ ".out","w",stdout);

	int tests;
	assert(scanf("%d\n",&tests) == 1);

	FOR(test, tests)
	{
		printf("Case #%d:", test+1);
		solve();
		printf("\n");
	}

	return 0;
}

