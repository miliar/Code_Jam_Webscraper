#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <complex>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()

#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()

typedef long long lint;
typedef vector<lint> VI;
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w+", stdout);
	int t;
	cin >> t;
	REP(it,t)
	{
		int n;
		cin >> n;
		VI A(n), B(n);
		REP(i,n)
			cin >> A[i];
		REP(i,n)
			cin >> B[i];
		sort(ALL(A));
		sort(ALL(B));
		reverse(ALL(B));
		lint ans = 0;
		REP(i,n)
			ans += A[i]*B[i];
		cout << "Case #" << it+1 << ": " << ans << endl;
	}
}
