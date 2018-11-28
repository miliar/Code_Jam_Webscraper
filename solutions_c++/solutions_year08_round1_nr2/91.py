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

typedef long double ldouble;
struct Numb
{
	ldouble x0;
	ldouble x1;
	Numb()
	{
		x1 = 0.0;
		x0 = 3+sqrtl(5);
	}
};
int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w+", stdout);
	int t;
	cin >> t;
	REP(it,t)
	{
		int n;
		cin >> n;
		ldouble x = 3.0+sqrt((ldouble)5.0);
		ostringstream out;
		out << pow(x,(ldouble)n);
		string s = out.str();
		cout << s << endl;
		/*ldouble pow = log((ldouble)1000.0)/log(x);
		cout << pow << endl;*/
	}
}
