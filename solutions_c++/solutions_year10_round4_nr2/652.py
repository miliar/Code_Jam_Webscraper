#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <list>
#include <functional>
#include <cctype>
#include <cstring>
#include <boost/typeof/typeof.hpp>

using namespace std;

#define REP(i_, n_)		for( unsigned i_ = 0; i_ != n_; ++i_ )
#define FOR(i_, a_, b_)	for( BOOST_TYPEOF(a_) i_ = a_; i_ != (b_); ++i_ )
#define ALL(c)			(c).begin(), (c).end()

int const P = 10;
int const INF = 1<<29;

int left(int i)  { return 2*i + 1; }
int right(int i) { return 2*i + 2; }

int p;
int mx[1<<P];		// constraints
int cs[P+1][1<<P];	// game cost
int dp[1<<P][P+1];
long long mem[1<<P][P+1];

long long solve(int i, int m, int l)
{
// 	       0
// 	   1       2
// 	 3   4   5   6
// 	7 8 9 A B C D E

	if( l == p )
	{
		int j = i - (1<<p) + 1;
		return INF * (m > mx[j]);
	}

	long long& rv = mem[i][m];
	if( rv != -1 )
		return rv;
	rv = cs[l][i-(1<<l)+1] + solve(left(i), m, l+1) + solve(right(i), m, l+1);
	rv = min(rv, solve(left(i), m+1, l+1) + solve(right(i), m+1, l+1));

	return rv;
}

int main()
{
	int T;
	cin >> T;
	for( int C = 1; C <= T; ++C )
	{
		cin >> p;
		REP(i, (1<<p))
			cin >> mx[i];
		REP(i, p) REP(j, (1<<(p-i-1)))
			cin >> cs[p-i-1][j];

		memset(mem, -1, sizeof(mem));
		long long rv = solve(0, 0, 0);
		cout << "Case #" << C << ": " << rv << endl;
	}
	return 0;
}

