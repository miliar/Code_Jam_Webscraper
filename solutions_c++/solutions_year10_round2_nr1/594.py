#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
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
using namespace std;

#define TRACE(x...) x
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")

#define fori(i, n) for ( typeof(n) i = 0; i < (n); ++i )
#define forr(i, a, b) for ( typeof(a) i = (a); i <= (b); ++i )
#define ford(i, a, b) for ( typeof(a) i = (a); i >= (b); --i )
#define tr(T, i) for ( typeof(T.begin()) i = T.begin(); i != T.end(); ++i )
#define sz size()
#define all(x) (x).begin(),(x).end()
#define _sort(x) sort(all(x))

template<class T> string a2s(T x) { ostringstream o; o << x; return o.str(); }
template<class T> T s2a(string s) { istringstream i(s); T x; i >> x; return x; }

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;

const double EPS = 1e-9;

int cmp( double x, double y = 0, double tol = EPS )
{
    return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

vector< string > divide( string s )
{
	vector< string > v;
	forr(i,1,s.sz-1)
	{
		if ( s[i] == '/' )
		{
			v.push_back( s.substr( 0, i ) );
		}
		else if ( i == s.sz-1 )
		{
			v.push_back( s.substr( 0, i + 1 ) );
		}
	}
	return v;
}

int main()
{
    int T;
    cin >> T;

    fori(cas, T)
    {
        int N, M;
		int asw = 0;
		
        cin >> N >> M;

		set< string > exist, put;
		string s;

		fori(i,N)
		{
			cin >> s;
			vector< string > vs = divide( s );
			exist.insert( all(vs) );
		}

		fori(i,M)
		{
			cin >> s;
			vector< string > vs = divide( s );
			put.insert( all(vs) );
		}

		tr(put,it)
		{
			if ( exist.find( *it ) == exist.end() )
			{
				++asw;
			}
		}

        cout << "Case #" << cas+1 << ": ";
        cout << asw << endl;
    }

    return 0;
}
