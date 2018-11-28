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

void change( vector< string > & v )
{
	int n = v.sz;
	fori(i,n)
	{
		int pos_ponto = -1, pos_letra = -1;
		ford(j,n-1,0)
		{
			if ( v[i][j] == '.' )
			{
				pos_ponto = j;
				break;
			}
		}
		for( int j = pos_ponto - 1; j >= 0; --j )
		{
			if ( v[i][j] != '.' )
			{
				pos_letra = j;
				break;
			}
		}
		if ( pos_letra != -1 && pos_ponto != -1 )
		{
			swap( v[i][pos_letra], v[i][pos_ponto] );
			--i;
		}
	}
}

string check( vector< string> & v, int K )
{
	int maxR = 0, maxB = 0;

	int n = v.sz;

	// horizontal
	// R
	fori(i,n)
	{
		int aux = 0;
		fori(j,n)
		{
			if( v[i][j] == 'R' )
			{
				aux++;
				maxR = max( maxR, aux );
			}
			else
			{
				aux = 0;
			}
		}
	}

	// B
	fori(i,n)
	{
		int aux = 0;
		fori(j,n)
		{
			if( v[i][j] == 'B' )
			{
				aux++;
				maxB = max( maxB, aux );
			}
			else
			{
				aux = 0;
			}
		}
	}

	// vertical
	// R
	fori(i,n)
	{
		int aux = 0;
		fori(j,n)
		{
			if( v[j][i] == 'R' )
			{
				aux++;
				maxR = max( maxR, aux );
			}
			else
			{
				aux = 0;
			}
		}
	}

	// B
	fori(i,n)
	{
		int aux = 0;
		fori(j,n)
		{
			if( v[j][i] == 'B' )
			{
				aux++;
				maxB = max( maxB, aux );
			}
			else
			{
				aux = 0;
			}
		}
	}

	// diagonal principal
	// R
	fori(i,n)
	{
		fori(j,n)
		{
			int aux = 0;
			for( int k1 = i, k2 = j; k1 < n && k2 < n; ++k1, ++k2 )
			{
				if( v[k1][k2] == 'R' )
				{
					aux++;
					maxR = max( maxR, aux );
				}
				else
				{
					aux = 0;
				}
			}
		}
	}

	// B
	fori(i,n)
	{
		fori(j,n)
		{
			int aux = 0;
			for( int k1 = i, k2 = j; k1 < n && k2 < n; ++k1, ++k2 )
			{
				if( v[k1][k2] == 'B' )
				{
					aux++;
					maxB = max( maxB, aux );
				}
				else
				{
					aux = 0;
				}
			}
		}
	}

	// diagonal principal
	// R
	fori(i,n)
	{
		fori(j,n)
		{
			int aux = 0;
			for( int k1 = i, k2 = j; k1 >= 0 && k2 < n; --k1, ++k2 )
			{
				if( v[k1][k2] == 'R' )
				{
					aux++;
					maxR = max( maxR, aux );
				}
				else
				{
					aux = 0;
				}
			}
		}
	}

	// B
	fori(i,n)
	{
		fori(j,n)
		{
			int aux = 0;
			for( int k1 = i, k2 = j; k1 >= 0 && k2 < n; --k1, ++k2 )
			{
				if( v[k1][k2] == 'B' )
				{
					aux++;
					maxB = max( maxB, aux );
				}
				else
				{
					aux = 0;
				}
			}
		}
	}

	if ( maxR >= K && maxB >= K )
	{
		return "Both";
	}
	if ( maxR >= K )
	{
		return "Red";
	}
	if ( maxB >= K )
	{
		return "Blue";
	}
	return "Neither";
}

int main()
{
    int T;
    cin >> T;

    fori(cas, T)
    {
        int N, K;

        cin >> N >> K;
		string s, asw = "r";
		vector< string > v( N );
		
		fori(i,N)
		{
			cin >> s;
			v[i] = s;
		}

		change( v );

		asw = check( v, K );

        cout << "Case #" << cas+1 << ": ";
        cout << asw << endl;
    }

    return 0;
}
