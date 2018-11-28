#include <cstdio>
#include <iostream>
#include <memory.h>
#include <cassert>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <cmath>

#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (decltype((x).begin()) it = (x).begin(); it != (x).end(); it++)
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

double run()
{
	int x,s,r,t,n;
	x=ni();
	r=ni();
	s=ni();
	t=ni();
	n=ni();
	vector<pair<pair<int,int>, int> > speedup;
	vector<pair<int, pair<int,int> > > speedup2;
	forn(i,n) {
		int start = ni();
		int stop = ni();
		int w = ni();
		speedup.pb(make_pair(make_pair(start,stop),w));
		speedup2.pb(make_pair(w,make_pair(start,stop)));
	}
	sort(all(speedup)); sort(all(speedup2));
	speedup.pb(make_pair(make_pair(x,x),0));
	int pos = 0;
	double ret = 0.0;
	double slow = 0.0;
	fori(it,speedup) {
		double tleft = t - ret;
		double tadd = (double)(it->first.first - pos)/s;
		ret += min(tleft,tadd);
		if (tadd > tleft)
			slow += (double)(it->first.first - (pos + s*tleft))/r;
		pos = it->first.second;
	}
	
	fori(it,speedup2) {
		double tleft = t - ret;
		double tadd = (double)(it->second.second - it->second.first)/(s+it->first);
		ret += min(tleft,tadd);
		if (tadd > tleft)
			slow += (double)(it->second.second - (it->second.first + (s+it->first)*tleft))/(r+it->first);
	}
	return ret + slow;
}

int main()
{
	int i, j, k, t, tests;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	scanf("%d\n", &tests);

	for (int tt=0; tt<tests; tt++) {
		double ret = run();
		printf("Case #%d: %lf\n", tt+1, ret);
	}
	return 0;
}