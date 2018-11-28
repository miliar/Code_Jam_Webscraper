#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <list>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cstdio>
#include <ctime>
#include <queue>
#include <tr1/unordered_map>
#include <tr1/unordered_set>

using namespace std;
using namespace tr1;

#define fori(i, n) for ( int i = 0; i < (n); ++i )
#define forr(i, a, b) for ( int i = (a); i <= (b); ++i )
#define ford(i, a, b) for ( int i = (a); i >= (b); --i )
#define tr(T, i) for (typeof(T.begin()) i = T.begin(); i != T.end(); ++i )
#define sz size()
#define all(x) (x).begin(),(x).end()
#define _sort(x) sort(all(x))
#define pb push_back

#define TRACE(x...) x
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")

template<class T> string a2s(T x) { ostringstream o; o << x; return o.str(); }
template<class T> T s2a(string s) { istringstream i(s); T x; i >> x; return x; }

const double EPS = 1e-9;
const int INF = 0x3F3F3F3F;

int cmpD(double x, double y = 0, double tol = EPS)
{
    return ( x <= y + tol ) ? ( x + tol < y ) ? -1 : 0 : 1;
}

bool ok( const vector< int > & v, double t, int d )
{
	int n = v.sz;
	vector< pair< double, double > > interval(n);
	fori(i,n)
	{
		interval[i].first = v[i] - t;
		interval[i].second = v[i] + t;
	}
	
	double pos = interval[0].first;
	
	forr(i,1,n-1)
	{
		if ( cmpD( pos + d, interval[i].second ) <= 0 )
		{
			pos = max( pos + d, interval[i].first );
		}
		else return false;
	}
	
	return true;
}

int main()
{
	int t, c, d, p, v;
	cin >> t;
	
	forr(cas,1,t)
	{
		cin >> c >> d;
		vector< int > init_pos;
		fori(i,c)
		{
			cin >> p >> v;
			fori(j,v) init_pos.pb(p);
		}
		
		double esq = 0, dir = 1e10, m, asw;
		while ( cmpD( esq, dir ) < 0 )
		{
			m = esq+(dir-esq)/2;
			if ( ok( init_pos, m, d ) )
			{
				dir = m;
				asw = m;
			}
			else esq = m;
		}
		
		cout << "Case #" << cas << ": ";
		printf("%.9lf\n", asw);
	}
	return 0;
}

