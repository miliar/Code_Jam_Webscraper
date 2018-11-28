#include "cstdlib"
#include "cctype"
#include "cstring"
#include "cstdio"
#include "cmath"
#include "algorithm"
#include "vector"
#include "string"
#include "iostream"
#include "sstream"
#include "set"
#include "queue"
#include "stack"
#include "fstream"
#include "iomanip"
#include "bitset"
#include "list"
#include "ctime"
using namespace std;

typedef long long				LL;
typedef unsigned long long		ULL;
typedef unsigned char			uchar;
typedef vector <string>			vs;
typedef vector <int>			vi;
#define CC(m,what)				memset(m,what,sizeof(m))
#define FOR(i,a,b)				for( i = (a); i < (b); ++i )
#define FF(i,a)					for( i = 0; i < (a); ++i )
#define FFD(i,a)				for( i = (a)-1; i >= 0; --i )
#define FORD(i,a,b)				for( i = (a)-1; i >= (b); --i )
#define ll(a)					((a)<<1)
#define rr(a)					(((a)<<1)+1)
#define sz(a)					((int)a.size())
#define PP(n,m,a)				puts("---");FF(i,n){FF(j,m)printf("%10d", a[i][j]);puts("");}
const double eps = 1e-11;
const double Pi = acos(-1.0);

LL l, p, c, t[32];
int res, n;


int play(int t) {
	if ( t== 1 ) return 0;
	if ( t&1 ) return 1+play((t+1)/2);
	else return 1+play(t/2);
}

void hexie() {
	cin >> l >> p >> c;
	n = res = 0;
	t[0] = l;
	n = 1;
//	cout << l << ' ' << p << ' ' << c << endl;
	while ( p > t[n-1]*c ) {
		t[n] = t[n-1]*c;
		++n;
	}
//	cout << n << endl;
	res = play(n);
}


int main() {
	int T;
	freopen("E:\\OwnCode\\c++\\acm\\in.txt","r",stdin);
	freopen("E:\\OwnCode\\c++\\acm\\data.out","w",stdout);
	cin >> T;
	for ( int i = 1; i <= T; ++i ) {
		hexie();
		printf("Case #%d: %d\n", i, res);
	}
	return 0;
}