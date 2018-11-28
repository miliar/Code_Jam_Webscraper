#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)
#define sorta(v) sort(all(v))
#define sortid(v) sort(all(v), greater<int>())
#define sortdd(v) sort(all(v), greater<double>())

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;


template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
template <class T> void outc(T a, T b) { for (T i = a; i  != b; ++i) {  cout << * i << ((i+1) != b ? ", " : ""); } }

int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }


bool canbeok(int sc, int p, bool s) {
	for (int i = p; i <= sc && i <=10 ; i++) {
		int rem= sc - i;
		if (!s &&  ((rem <= 2*i) && (rem >= 2*i-2))) {
			
			//printf("Normal : %d + %d --> %d \n", i, rem, sc);
			return true;
		}
		if (s && ((rem >= 2*i-4) && (rem <= 2*i))) {
			//	printf("Surprise : %d + %d --> %d \n", i, rem, sc);
			return true;
		}
	}

//	printf("score %d not ok fo %d\n", sc, p);
			return false;
}
int main() {

	// ! get inputs !
	freopen("d:\\gcj\\input.in","rt",stdin);
	freopen("d:\\gcj\\output.out","wt",stdout);	


	int tests;
	scanf("%d", &tests);
	getchar();
	rep2(tt, 1, tests+1) {
		printf("Case #%d: ", tt); 
		int n = ni(), s = ni(),p = ni();
		bool stts[100];
		rep(i, 100)
			stts[i] = false;
		vi sc;
		rep(i, n)
			sc.pb(ni());
		sorta(sc);

		int ret = 0;
		do{ 
		
			
		int v=0;
		rep(i, s) 
			stts[i] = canbeok(sc[i], p, true);
		rep2(i, s, n) 
			stts[i] = canbeok(sc[i], p, false);
		rep(i,n) 
			v += stts[i];

	//	printf("---------------------> Total %d \n", v);
		ret = max(ret, v);
		
		}while(next_permutation(sc.begin() , sc.end()) );
		printf("%d", ret);
		printf("\n");
	}

	
	return 0;
}