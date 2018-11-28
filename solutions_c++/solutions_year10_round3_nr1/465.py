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
#include "map"
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

class node {
public:
	int s, e;
};

int		n, res;
node	t[1100];

bool cmp(node a, node b) {
	return a.s < b.s;
}
void hexie() {
	scanf("%d", &n);
	int i, j, k;
	res = 0;
	FF (i, n) {
		scanf("%d%d", &t[i].s, &t[i].e);
	}
	sort(t, t+n, cmp);
	FF (i, n) {
		FOR (j, i+1, n) {
			if ( t[i].e >= t[j].e ) ++res;
		}
	}
}


int main() {
	int T;
	freopen("E:\\OwnCode\\c++\\acm\\in.txt","r",stdin);
	freopen("E:\\OwnCode\\c++\\acm\\data.out","w",stdout);
	scanf("%d", &T);
	for ( int i = 1; i <= T; ++i ) {
		hexie();
		printf("Case #%d: %d\n", i, res);
	}
}