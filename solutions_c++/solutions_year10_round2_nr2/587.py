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

struct chicken
{
	int x, v;
	double t;
	bool ok;
};

int main()
{
    int C;
    cin >> C;

    fori(cas, C)
    {
        int N, K, B, T;
		
        cin >> N >> K >> B >> T;

		vector< chicken > vv( N );

		fori(i,N)
		{
			cin >> vv[i].x;
			vv[i].ok = false;
		}

		fori(i,N) cin >> vv[i].v;
		
		fori(i,N)
		{
			vv[i].t = (double) ( B - vv[i].x ) / vv[i].v;
			if ( cmp( vv[i].t, T ) <= 0 )
			{
				vv[i].ok = true;
			}
		}

		int cnt = 0, asw = 0, pos1, pos2;
		ford(i,N-1,0)
		{
			if ( vv[i].ok )
			{
				++cnt;
			}
			else
			{
				pos1 = -1;
				pos2 = i;

				ford(j,pos2-1,0)
				{
					if ( vv[j].ok )
					{
						pos1 = j;
						break;
					}
				}
				
				if ( pos1 != -1 )
				{
					swap( vv[pos1], vv[pos2] );
					asw += pos2 - pos1;
					++i;
				}
			}

			if ( cnt == K ) break;
		}
		
		if ( cnt < K )
		{
			cout << "Case #" << cas+1 << ": ";
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << "Case #" << cas+1 << ": ";
			cout << asw << endl;
		}
    }

    return 0;
}
