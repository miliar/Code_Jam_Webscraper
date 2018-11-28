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

#define fe first
#define se second
#define sz size()
#define pb push_back
#define ins insert

#define FNAME "A-small-attempt0"
#define IN_FILE FNAME ".in"
#define OUT_FILE FNAME ".out"
ifstream in;
ofstream out;

#define OUT(A) out << A; cout << A;

int N, M;
vi aa, bb;
vi B;

int there(int p, int q, int r, int s)
{
	FOR(i,0,N) if (!B[i])
		if (aa[i] >= p && aa[i] <= q && bb[i] >= r && bb[i] <= s) return 1;
	return 0;
}

void do_case(int cc)
{
	//take case input
	in >> N;
	aa.clear(); bb.clear(); B.clear();
	aa.resize(N);
	bb.resize(N);
	B.resize(N);
	int cb = 0;
	FOR(i,0,N)
	{
		in >> aa[i] >> bb[i];
		string str;
		in >> str;
		if (str == "NOT")
		{
			in >> str;
			B[i] = 0;
		}
		else
		{
			B[i] = 1;
			cb++;
		}
	}
	OUT("Case #" << cc << ":" << endl);
	//identify BIRD region
	int lo = INT_MAX, hi = 0, lef = INT_MAX, rit = 0;
	FOR(i,0,N) if (B[i])
	{
		lo <?= aa[i];
		hi >?= aa[i];
		lef <?= bb[i];
		rit >?= bb[i];
	}
	in >> M;
	while (M--)
	{
		int a, b;
		in >> a >> b;
		if (a >= lo && a <= hi && b >= lef && b <= rit) { OUT("BIRD");}
		else
		{
			int nb = 0;
			if (a >= lo && a <= hi)
				if (b < lef)
					nb |= there(lo,hi,b,lef);
				else
					nb |= there(lo,hi,rit,b);
			if (b >= lef && b <= rit)
				if (a < lo)
					nb |= there(a,lo,lef,rit);
				else
					nb |= there(hi+1,a,lef,rit);
			if (a > hi && b > rit) nb |= there(hi,a,rit,b);
			if (a > hi && b < lef) nb |= there(hi,a,b,lef);
			if (a < hi && b > rit) nb |= there(a,lo,rit,b);
			if (a < hi && b < lef) nb |= there(a,lo,b,lef);
			if (lo == INT_MAX) nb = 0;
			if (nb)
			{
				OUT("NOT BIRD");
			}
			else { OUT("UNKNOWN");}
		}
		OUT(endl);
	}
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
