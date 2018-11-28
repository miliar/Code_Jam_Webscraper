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

int v[1010];
char visited[1010];

int main()
{
	int t, a, n;
	cin >> t;
	forr(cas,1,t)
	{
		cin >> n;
		fori(i,n) 
		{
			cin >> a;
			v[i] = a-1;
			visited[i] = 0;
		}
		int asw = 0, pos;
		fori(i,n)
		{
			pos = i;
			if ( !visited[pos] )
			{
				int cycle_size = 0;
				while ( !visited[pos] )
				{
					cycle_size++;
					visited[pos] = 1;
					pos = v[pos];
				}
				asw += cycle_size == 1 ? 0 : cycle_size;
			}
		}
		cout << "Case #" << cas << ": " << asw << endl;
	}
	return 0;
}
