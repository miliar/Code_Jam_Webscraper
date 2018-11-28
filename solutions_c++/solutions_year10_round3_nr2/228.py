#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <climits>
#include <cmath>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <iterator>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define ALL(c) (c).begin(), (c).end()
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _b(b), i(a); i < _b; i++)
#define FOR1(i,a,b) for (int _b(b), i(a); i <= _b; i++)
#define BFOR(i,a,b) for(int i=(a),_b=(b);i>_b;--i)
#define BFOR1(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define REP1(i,n) FOR1(i,1,n)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define SZ(c) (c).size()
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define FILL(a,b) memset(a,b,sizeof a)
#define SORT(c) sort(ALL(c))
#define GETLINE(str,line) string str; getline(cin,str); stringstream line(str);
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define gcd(a,b) __gcd(a,b)
#define pi M_PI

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int _Tnum(0);
	cin >> _Tnum;
	REP1(_Tcur,_Tnum)
	{
		long long P,L,C;
		cin >> P >> L >> C;
		P*=C;

		long long num(0);
		long long answ(0);

		while(P<L) { num++; P*=C; }
		while(num>0) { num>>=1; answ++; }

		cout << "Case #" << _Tcur << ": " << answ << endl;
	}

	return 0;
}
