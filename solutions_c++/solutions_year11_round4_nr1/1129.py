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

struct rec
{
	int b, e, w;

	bool operator<(const rec & r) const
	{
		return b < r.b;
	}
} input[10000];

bool Comp(rec r1, rec r2)
{
	return r1.w < r2.w;
}

void Solve(int tc)
{
	int X, S, R, N;
	double t;
	cin >> X >> S >> R >> t >> N;
	FOR(i, 0, N)
	{
		cin >> input[i].b >> input[i].e >> input[i].w;
		input[i].w += S;
	}
	sort(input, input+N);

	int NN = N, pos = 0;
	FOR(i, 0, N)
	{
		if (pos < input[i].b)
		{
			input[NN].b = pos;
			input[NN].e = input[i].b;
			input[NN].w = S;
			++NN;
		}
		pos = input[i].e;
	}
	if (pos < X)
	{
		input[NN].b = pos;
		input[NN].e = X;
		input[NN].w = S;
		++NN;
	}

	sort(input, input+NN, Comp);
	double res = 0.0;

	FOR(i, 0, NN)
	{
		double runTime = (double)(input[i].e-input[i].b)/(input[i].w+R-S);
		if (runTime <= t)
		{
			res += runTime;
			t -= runTime;
		}
		else
		{
			double d = t*(input[i].w+R-S);
			res += t + (input[i].e-input[i].b-d)/input[i].w;
			t = 0.0;
		}
	}

	printf("Case #%d: %.9lf\n", tc, res);
}

int main()
{
	int T;
	cin >> T;
	FOR(step, 0, T)
		Solve(step+1);

	return 0;
}