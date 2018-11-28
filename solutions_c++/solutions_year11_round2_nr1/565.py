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

struct team
{
	int j, v, d;
	double wp, owp, oowp, rpi;
};

int main()
{
	int t, n;
	cin >> t;
	
	forr(cas,1,t)
	{
		cin >> n;
		vector<string> v(n);
		fori(i,n) cin >> v[i];
		vector< team > times(n);
		fori(i,n)
		{
			times[i].j = times[i].v = times[i].d = 0;
			fori(j,n)
			{
				if ( v[i][j] != '.' )
				{
					times[i].j++;
					if ( v[i][j] == '1' ) times[i].v++;
					else times[i].d++;
				}
			}
		}
		
		fori(i,n) 
		{
			times[i].wp = (double) times[i].v / times[i].j;
		} 
		
		fori(k,n)
		{
			double owp = 0, cnt = 0;
			fori(i,n) if ( i != k && v[k][i] != '.' )
			{
				int jo = 0, vi = 0;
				fori(j,n) if ( j != k )
				{
					if ( v[i][j] != '.' )
					{
						jo++;
						if ( v[i][j] == '1' ) vi++;
					}
				}
				owp += (double) vi / jo;
				cnt++;
			}
			
			owp /= cnt;
			times[k].owp = owp;
		}
		
		fori(i,n)
		{
			times[i].oowp = 0;
			fori(j,n)
			{
				if ( v[i][j] != '.' )
				{
					times[i].oowp += times[j].owp;
				}
			}
			times[i].oowp /= times[i].j;
		}
		
		fori(i,n) times[i].rpi = 0.25 * times[i].wp + 0.50 * times[i].owp + 0.25 * times[i].oowp;
		
		cout << "Case #" << cas << ":" << endl;
		fori(i,n) printf("%.9lf\n", times[i].rpi);
	}
	return 0;
}

