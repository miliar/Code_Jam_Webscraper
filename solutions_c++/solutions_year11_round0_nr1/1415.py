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
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
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

void Solve(int tc)
{
	int N;
	cin >> N;

	char c; int n;
	int t = 0, p1 = 1, t1 = 0, p2 = 1, t2 = 0;
	FOR(i, 0, N)
	{
		cin >> c >> n;
		
		if (c == 'O')
		{
			int dist = abs(p1-n);
			t1 += dist+1;
			t1 = max(t1, t+1);
			t = t1;
			p1 = n;
		}
		else
		{
			int dist = abs(p2-n);
			t2 += dist+1;
			t2 = max(t2, t+1);
			t = t2;
			p2 = n;
		}
	}

	printf("Case #%d: %d\n", tc, t);
}

int main()
{
	int T;
	cin >> T;
	FOR(step, 0, T)
		Solve(step+1);

	return 0;
}
