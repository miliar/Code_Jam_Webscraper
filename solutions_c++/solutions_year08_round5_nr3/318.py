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

#define getL(str,B) str.getline(B,sizeof(B))
#define getI(str,B,n) getL(str,B); sscanf(B,"%ld",&(n))
#define getF(str,B,n) getL(str,B); sscanf(B,"%lf",&(n))

#define fe first
#define se second
#define sz size()
#define pb push_back
#define ins insert

#define IN_FILE "C-small-attempt0.in"
#define OUT_FILE "sample.out"
ifstream in;
ofstream out;

#define OUT(A) out << A; cout << A;

#define BUF_SIZE 10000
char buf[BUF_SIZE];

int M, N;
vs B;

int dp[11][1<<10];

bool valid(int n, int mask)
{
	REP(i,N) if ((mask & (1 << i)) && B[n][i] == 'x') return false;
	return true;
}

bool nice (int mask)
{
	for (int i = 1, j = 0; i < 31; i++, j++)
		if ((mask&(1<<i)) && (mask&(1<<j))) return false;
	return true;
}

void do_case(int cc)
{
	in >> M >> N;
	B.resize(M);
	REP(i,M) in >> B[i];
	SET(dp,0);
	REPE(i,M)
		REP(j,(1<<N)) if (valid(i-1,j) && nice(j))
			REP(k,(1<<N)) if (nice(j^k))
				dp[i][j] >?= dp[i-1][k] + bitc(j);
	int ma = 0;
	REP(i,(1<<N)) ma >?= dp[M][i];
	OUT("Case #" << cc << ": ");
	OUT(ma);
	OUT(endl);
}

int main()
{
	in.open(IN_FILE);
	out.open(OUT_FILE);
	int T;
	in >> T;
	REPE(cc,T)
		do_case(cc);
	in.close();
	out.close();
	return 0;
}
