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
const int    dir[4][2] = {0, 1, 1, 0, 0, -1, -1, 0};

int		k, n, c[40];

void hexie() {
	scanf("%d%d", &n, &k);
	int i, j;
	j = 0;
	CC(c, 0);
	while (k) {
		c[j] = k&1;
		k >>= 1;
		++j;
	}
	bool res = true;
	FF (i, n) {
		if ( c[i] == 0 ) {
			res = false;
			break;
		}
	}
	if ( res ) cout << "ON" << endl;
	else cout << "OFF" << endl;
}

int main() {
	freopen("E:\\OwnCode\\c++\\acm\\in.txt","r",stdin);
	freopen("E:\\OwnCode\\c++\\acm\\out.txt","w",stdout);
//	freopen("in","r",stdin);
//	freopen("out","w",stdout);
	int T;
	scanf("%d", &T);
	for ( int i = 1; i <= T; ++i ) {
		printf("Case #%d: ", i);
		hexie();
	}
	return 0;
}
