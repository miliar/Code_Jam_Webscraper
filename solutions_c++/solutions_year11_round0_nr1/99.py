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

#define TRACE(x...)
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

int main()
{
	int t, x, n;
	char c;
	cin >> t;
	forr(cas,1,t)
	{
		vector<int> o, b, v;
		cin >> n;
		fori(i,n)
		{
			cin >> c >> x;
			if ( c == 'O' ) 
			{
				o.pb(x);
				v.pb(1);
			}
			else 
			{
				b.pb(x);
				v.pb(2);
			}
		}
		int pos1 = 1, pos2 = 1, cnt1 = 0, cnt2 = 0, dist1, dist2, tempo = 0;
		fori(i,n)
		{
			if ( cnt1 >= o.sz ) break;
			if ( cnt2 >= b.sz ) break;
			
			dist1 = abs(o[cnt1] - pos1);
			dist2 = abs(b[cnt2] - pos2);

			if ( v[i] == 1 )
			{
				tempo += dist1 + 1;
				pos1 = o[cnt1];
				if( dist2 <= dist1 + 1 ) pos2 = b[cnt2];
				else
				{
					if ( pos2 > b[cnt2] ) pos2 -= (dist1+1);
					else pos2 += (dist1+1);
				}
				cnt1++;
			}
			else
			{
				tempo += dist2 + 1;
				pos2 = b[cnt2];
				if( dist1 <= dist2 + 1 ) pos1 = o[cnt1];
				else
				{
					if ( pos1 > o[cnt1] ) pos1 -= (dist2+1);
					else pos1 += (dist2+1);
				}
				cnt2++;
			}
		}
		
		while ( cnt1 < o.sz ) 
		{
			dist1 = abs(o[cnt1] - pos1);
			tempo += dist1 + 1;
			pos1 = o[cnt1];
			cnt1++;
		}
		while ( cnt2 < b.sz )
		{
			dist2 = abs(b[cnt2] - pos2);
			tempo += dist2 + 1;
			pos2 = b[cnt2];
			cnt2++;
		}
		
		cout << "Case #" << cas << ": " << tempo << endl;
	}
	return 0;
}

