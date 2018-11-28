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

struct Average
{
	double sum, num;
	Average(): sum(0.0), num(0.0) { }

	void Update(double val) { num += 1.0; sum += val; }
	double Get() { return sum / num; }
	void Clear() { sum = num = 0.0; }
};

const int MAX = 147;
string input[MAX];

Average wp[MAX], owp[MAX], oowp[MAX];

void Solve(int tc)
{
	int N;
	cin >> N;
	FOR(i, 0, N) cin >> input[i];

	FOR(i, 0, N)
	{
		wp[i].Clear();
		owp[i].Clear();
		oowp[i].Clear();
	}

	//wp
	FOR(i, 0, N)
	{
		FOR(j, 0, N)
		{
			if (input[i][j] == '1')
				wp[i].Update(1.0);
			else if (input[i][j] == '0')
				wp[i].Update(0.0);
		}
	}

	//owp
	FOR(i, 0, N)
	{
		FOR(j, 0, N)
		{
			if (input[i][j] == '.') continue;
			Average temp;
			FOR(k, 0, N)
				if (k != i)
				{
					if (input[j][k] == '1') temp.Update(1.0);
					else if (input[j][k] == '0') temp.Update(0.0);
				}
			owp[i].Update(temp.Get());
		}
	}

	//oowp
	FOR(i, 0, N)
	{
		FOR(j, 0, N)
			if (input[i][j] != '.')
				oowp[i].Update(owp[j].Get());
	}

	printf("Case #%d:\n", tc);
	FOR(i, 0, N)
		printf("%.12lf\n", 0.25 * wp[i].Get() + 0.5 * owp[i].Get() + 0.25 * oowp[i].Get());
}

int main()
{
	int T;
	cin >> T;
	FOR(step, 0, T)
		Solve(step+1);

	return 0;
}