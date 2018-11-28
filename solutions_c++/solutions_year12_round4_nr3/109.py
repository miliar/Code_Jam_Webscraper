#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1<<29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

const int MAX = 2000;
int N, x[MAX];
ll y[MAX];

void Solve(int tc)
{
	scanf("%d", &N);
	REP(i, N-1)
	{
		scanf("%d", &x[i]);
		--x[i];
	}
	printf("Case #%d: ", tc);

	bool bad = false;
	REP(i, N-1)
	{
		if (x[i] <= i)
		{
			bad = true;
			break;
		}
		FOR(j,i+1,x[i]-1)
			if (x[j] > x[i])
				bad = true;
		if (bad) break;
	}
	if (bad) { printf("Impossible\n"); return; }

	REP(i, N) y[i] = 1000000000;
	FORD(i, N-2, 0)
	{
		FOR(j, x[i]+1, N-1)
		{
			ll dx = j-x[i], dy = y[j]-y[x[i]], dx2 = x[i]-i;
			if (dy <= 0) continue;
			chmin(y[i], y[x[i]] - (dy*dx2+dx-1)/dx);
		}
		ll shift = 0;
		FOR(j, i+1, x[i]-1)
		{
			ll dx = j-i, dy = y[j]-y[i], dy2 = y[j]-y[i], dx2 = x[i]-i;
			chmax(shift, dy-(dy2*dx+dx2-1)/dx2+1);
		}
		FOR(j, i+1, x[i]-1) y[j] -= shift;
		if (shift) i = x[i]-1;
	}

	REP(i, N) printf("%lld ", y[i]);
	printf("\n");
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) Solve(tc);

	return 0;
}