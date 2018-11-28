#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <climits>
#include <cassert>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <utility>
#include <string>
#include <sstream>
#include <functional>
#include <algorithm>
#include <numeric>
#include <complex>
#include <ext/hash_map>
#include <ext/hash_set>
#include <ext/slist>

using namespace std;

#define FOR(i,a,b) for (typeof(a) i = (a); i < (b); i++)
#define FORR(i,a,b) for (typeof(b) i = (b); i >= (a); i--)
#define FORS(i,a,b,s) for (typeof(a) i = (a); i < (b); i += (s))
#define FORE(t,A) for (typeof(A.begin()) t = A.begin(); t != A.end(); t++)
#define REP(t,n) for (int t = 0; t < (n); t++)
#define REPE(t,n) for (int t = 1; t <= (n); t++)

#define LET(A,b) typeof(b) A = b
#define SET(A,p) memset(A,p,sizeof(A))
#define SETS(A,p,S) memset(A,p,S)

#define ALL(A) A.begin(), A.end()

typedef long long int ll;
typedef unsigned long long int ull;
typedef pair <int, int> iip;
typedef pair <ll, ll> llp;
typedef vector <int> vi;
typedef vector <ll> vll;
typedef vector <double> vd;
typedef vector <string> vs;

int bitc(ll n) { LET(r,0); while(n) { r += (n&1); n >>= 1;} return r;}
ll gcd (ll a, ll b) { return b==0?a:gcd(b,a%b);}

template<class T> T& operator >?= (T& x, T y) {if(y>x) x=y; return x;}
template<class T> T& operator <?= (T& x, T y) {if(y<x) x=y; return x;}
template<class T> T operator >? (T x, T y) {return x>y?x:y;}
template<class T> T operator <? (T x, T y) {return x<y?x:y;}

#define fi first
#define se second
#define sz size()
#define pb push_back
#define ins insert

#define FNAME "D-small-attempt0"
#define IN_FILE FNAME ".in"
#define OUT_FILE FNAME ".out"
ifstream in;
ofstream out;

#define OUT(A) out << A; cout << A;

int n, m;
vector <iip> a, b;

void do_case(int cc)
{
	a.clear();
	b.clear();
	in >> n;
	FOR(i,1,n)
	{
		iip t;
		in >> t.fi >> t.se;
		a.pb(t);
	}
	in >> m;
	FOR(i,1,m)
	{
		iip t;
		in >> t.fi >> t.se;
		b.pb(t);
	}
	int F = 0;
	FOR(i,0,1<<n)
	{
		if (bitc(i) != m) continue;
		vi p;
		FOR(j,0,n) if (i & (1<<j)) p.pb(j+1);
		do
		{
			vector<iip> g;
			vector<iip> h;
			FOR(j,0,m-1) g.pb(iip(p[b[j].fi-1],p[b[j].se-1]));
			int hh = 0;
			FOR(j,0,n-1)
				if ((i & (1<< (a[j].fi-1))) && (i & (1<< (a[j].se-1)))) { h.pb(a[j]); hh++;}
			if (hh != m-1) continue;
			FOR(j,0,m-1) if (g[j].fi > g[j].se) swap(g[j].fi,g[j].se);
			FOR(j,0,m-1) if (h[j].fi > h[j].se) swap(h[j].fi,h[j].se);
			sort(ALL(g)); sort(ALL(h));
			if (g == h) F = 1;
		} while (next_permutation(ALL(p)));
	}
	OUT("Case #" << cc << ": ");
	if(F) { OUT("YES");}
	else { OUT("NO");}
	OUT(endl);
}

int main()
{
	in.open(IN_FILE);
	out.open(OUT_FILE);
	int T = 1;
	in >> T;
	REPE(cc,T)
		do_case(cc);
	in.close();
	out.close();
	return 0;
}
