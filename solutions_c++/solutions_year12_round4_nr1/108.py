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

const int MAX = 10007;
int N, d[MAX], l[MAX], D, dp[MAX];

void Solve(int tc)
{
	scanf("%d", &N);
	REP(i, N) scanf("%d%d", &d[i], &l[i]);
	scanf("%d", &D);

	memset(dp, 0, sizeof(dp));
	dp[0] = d[0];
	priority_queue<pair<int, int> > manage;
	manage.push(make_pair(dp[0], 0));
	while (!manage.empty())
	{
		int act = manage.top().first, i = manage.top().second;
		manage.pop();
		if (act != dp[i]) continue;
		for (int j = i-1; j >= 0 && d[i]-d[j] <= dp[i]; --j)
		{
			int act2 = min(d[i]-d[j], l[j]);
			if (act2 > dp[j])
			{
				dp[j] = act2;
				manage.push(make_pair(act2, j));
			}
		}
		for (int j = i+1; j < N && d[j]-d[i] <= dp[i]; ++j)
		{
			int act2 = min(d[j]-d[i], l[j]);
			if (act2 > dp[j])
			{
				dp[j] = act2;
				manage.push(make_pair(act2, j));
			}
		}
	}

	bool ok = false;
	REP(i, N)
		if (dp[i] >= D-d[i]) ok = true;
	printf("Case #%d: %s\n", tc, ok ? "YES" : "NO");
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) Solve(tc);

	return 0;
}