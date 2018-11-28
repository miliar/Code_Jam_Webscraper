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

int main()
{
    int T;
    cin >> T;

    fori(cas, T)
    {
        int N, a, b;
        cin >> N;

		vector< pair<int, int> > v( N );
		
		fori(i,N)
		{
			cin >> a >> b;
			v[i] = make_pair(a, b);
		}

		int asw = 0;
		fori(i,N)
		{
			forr(j,i+1,N-1)
			{
				if ( ( v[i].first < v[j].first && v[i].second > v[j].second ) || ( v[i].first > v[j].first && v[i].second < v[j].second ) )
				{
					++asw;
				}
			}
		}
		
        cout << "Case #" << cas+1 << ": ";
        cout << asw << endl;
    }

    return 0;
}
