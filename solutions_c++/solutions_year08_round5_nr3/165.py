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
#include <algorithm>
using namespace std; 

#define DEBUG(x) cerr << '>' << #x << ':' << x << endl;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
const int INF = 1 << 29;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n)
{
	int res = 0;
	while (n) { ++res; n -= last_bit(n); }
	return res;
}
#ifdef WIN32
typedef __int64 ll;
#else
typedef long long ll;
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////// 

ifstream fin("input.in");
ofstream fout("output.out");
//FILE *fin  = fopen ("input.in", "r");
//FILE *fout = fopen ("output.out", "w");

int R, C;
char board[100][100];

int dp[2][3000];

bool check(int n, int row)
{
	FOR(i, 0, C)
		if (test(n, i) && ((i && test(n, i-1)) || board[row][i] == 'x'))
			return false;
	return true;
}

bool check2(int n1, int n2)
{
	FOR(i, 0, C)
	{
		if (test(n1, i) && ((i && test(n2, i-1)) || (i < C-1 && test(n2, i+1))))
			return false;
		if (test(n2, i) && ((i && test(n1, i-1)) || (i < C-1 && test(n1, i+1))))
			return false;
	}
	return true;
}

int main()
{
	int T;
	fin >> T;

	FOR(step, 0, T)
	{
		fin >> R >> C;

		FOR(i, 0, R)
			fin >> board[i];

		memset(dp, 0, sizeof(dp));
		int res = 0;
		FOR(i, 0, two(C))
			if (check(i, 0))
			{
				dp[0][i] = ones(i);
				res = max(res, dp[0][i]);
			}

		int act = 0;
		FOR(r, 1, R)
		{
			FOR(i, 0, two(C))
				dp[1-act][i] = 0;

			FOR(n1, 0, two(C))
				if (check(n1, r-1))
				{
					FOR(n2, 0, two(C))
						if (check(n2, r) && check2(n1, n2))
						{
							dp[1-act][n2] = max(dp[1-act][n2], dp[act][n1] + ones(n2));
							res = max(res, dp[1-act][n2]);
						}
				}
			act = 1-act;
		}
		fout << "Case #" << step+1 << ": " << res << endl;
	}

	return 0;
}
