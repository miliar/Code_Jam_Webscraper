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

int main() {

	// ! get inputs !
	freopen("d:\\gcj\\input.in","rt",stdin);
	freopen("d:\\gcj\\output.out","wt",stdout);	



	// build the dict
	char dict[26][26];
	rep(i, ('z'-'a'+  1)) 
	{
		dict[i][0]=(char)'a'+i;
	}
	string ip[] = {"y n f i c w l b k u o m x s e v z p d r j g a t h a q", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string ip2 []= {"a b c d e f g h i j k l m n o p q r s t u v y w x y z", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};

	rep(i, 3) {
		rep(j, ip[i].size()) {
			if (ip[i][j] == ' ') {
			} else {
				dict[ip[i][j]-'a'][1] = ip2[i][j];
			}
		}
	}
	int tests;
	
	scanf("%d", &tests);
	getchar();
	rep2(tt, 1, tests+1) {
		printf("Case #%d: ", tt); 
		string ip;
		getline(cin, ip);
		string ret;

		rep(i, ip.size()) {
			if (ip[i] == ' ')
				ret = ret + ' ';
			else
				ret = ret + dict[ip[i]-'a'][1];
		}
		
		printf("%s", ret.c_str());
		
		printf("\n");
	}

	
	return 0;
}