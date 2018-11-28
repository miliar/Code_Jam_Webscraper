#include <iostream>
#include <fstream>
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
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1 << 29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=last_bit(n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

int P;
int input[1047];
int prices[11][1047];
int dp[11][11][1047];

int go(int seen, int layer, int match)
{
	int & res = dp[seen][layer][match];
	if (res != -1) return res;

	if (layer == P)
	{
		if (P-seen <= input[match]) res = 0;
		else res = 1000000000;
	}
	else
	{
		res = 1000000000;
		//buy
		res = min(res, go(seen+1, layer+1, 2*match) + go(seen+1, layer+1, 2*match+1) + prices[layer][match]);
		//not buy
		res = min(res, go(seen, layer+1, 2*match) + go(seen, layer+1, 2*match+1));
	}
	
	return res;
}

void Solve(int tc)
{	
	cin >> P;
	FOR(i, 0, two(P)) cin >> input[i];
	FOR2(i, P-1, -1)
		FOR(j, 0, two(i))
			cin >> prices[i][j];
	memset(dp, -1, sizeof(dp));
	cout << "Case #" << tc << ": " << go(0, 0, 0) << endl;
}

int main()
{
	int T;
	cin >> T;
	FOR(step, 0, T) Solve(step+1);

	return 0;
}