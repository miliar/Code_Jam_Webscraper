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

int n, k, b, limit;

class node {
public:
	int at;
	double need;
	int v;

	void setneed() {
		if ( v == 0 && at < b ) need = limit+1;
		else need = (b*1.0-at)/v;
	}
};

node	t[55];

void hexie(){
	bool flag = true;
	int i, j, num, res;
	scanf("%d%d%d%d", &n, &k, &b, &limit);
	FF (i, n) scanf("%d", &t[i].at);
	FF (i, n) scanf("%d", &t[i].v);

//	cout << '\n' << k << endl;
	FF (i, n) {
		t[i].setneed();
//		printf("%d  %d  %.2lf  %d\n", b-t[i].at, t[i].v, t[i].need, limit);
	}
	num = 0;
	FF (i, n) {
		if ( t[i].need <= limit ) ++num;
	}
	if ( num < k ) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	num = res = 0;
//	cout << n << endl;
	FFD (i, n) {
			if ( t[i].need > limit ) {
				j = i;
				while ( j > 0 ) {
					++res;
					--j;
					if ( t[j].need <= limit) break;
				}
				if ( t[j].need <= limit ) {
					swap(t[i], t[j]);
					++num;
				} else {
					flag = false;
					break;
				}
			} else {
				++num;
			}
		if ( num == k ) break;
	}
	printf("%d\n", res);
}

int main() {
	int T;
	freopen("E:\\OwnCode\\c++\\acm\\in.txt","r",stdin);
//	freopen("E:\\OwnCode\\c++\\acm\\data.out","w",stdout);
	scanf("%d", &T);
	for ( int i = 1; i <= T; ++i ) {
		printf("Case #%d: ", i);
		hexie();
	}
}

