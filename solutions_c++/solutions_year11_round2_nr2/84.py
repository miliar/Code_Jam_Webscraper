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

pair<int, int> input[247]; //position / number

void Solve(int tc)
{
	int C, D, sum = 0;
	cin >> C >> D;
	FOR(i, 0, C)
	{
		cin >> input[i].first >> input[i].second;
		sum += input[i].second;
	}

	double be = 0.0, en = (double)D * (double)(sum+2);
	while (en-be > 1e-8 && en/be > 1.00000000000001)
	{
		double m = (be+en) / 2.0;
		bool ok = true;

		double last = -1e12;
		FOR(i, 0, C)
		{
			double pos = input[i].first;

			last = max(last+D, pos-m) + (double)(input[i].second-1) * (double)D;
			if (fabs(last-pos) > m)
			{
				ok = false;
				goto finish;
			}
		}

finish:

		if (ok) en = m;
		else be = m;
	}
	
	printf("Case #%d: %.12lf\n", tc, be);
}

int main()
{
	int T;
	cin >> T;
	FOR(step, 0, T)
		Solve(step+1);

	return 0;
}