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

const int MAX = 201;
int M, F, N;
pair<ll, ll> in[MAX];

void Solve(int tc)
{
	cin >> M >> F >> N;
	REP(i, N) cin >> in[i].second >> in[i].first;

	REP(i, N)
	{
		bool ok = true;
		REP(j, N)
			if (i != j && in[i].first <= in[j].first && in[i].second >= in[j].second)
				ok = false;
		if (!ok)
		{
			swap(in[i], in[N-1]);
			--N;
			--i;
		}
	}
	sort(in, in+N);

	printf("Case #%d: ", tc);
	int result = 0;
	for (int f = 1; f*F <= M; ++f)
	{
		int m = M - f*F, act = 0, last = -1;
		REP(i, N)
		{
			ll n1 = (ll)(in[i].first-last)*f, n2 = m / in[i].second;
			if (n2 <= n1)
			{
				act += n2;
				break;
			}
			else
			{
				act += n1;
				m -= n1 * in[i].second;
			}
			last = in[i].first;
		}
		chmax(result, act);
	}
	printf("%d\n", result);
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) Solve(tc);

	return 0;
}