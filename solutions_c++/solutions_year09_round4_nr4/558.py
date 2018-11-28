#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;
using namespace rel_ops;

// defines
#define forn(i,n)       for( int ___n=int(n), i=0 ; i<___n ; ++i )
#define fordn(i,n)      for( int i=int(n)-1 ; i>=0 ; --i )
#define forsn(i,s,n)    for( int ___n=int(n), i=int(s) ; i<___n ; ++i )
#define fordsn(i,s,n)   for( int ___s=int(s), i=int(n)-1 ; i>=___s ; --i )
#define forall(i,c)     for( typeof((c).begin()) i=(c).begin() ; i!=(c).end() ; ++i )
#define fordall(i,c)    for( typeof((c).rbegin()) i=(c).rbegin() ; i!=(c).rend() ; ++i)
#define pb      push_back
#define sz(a)   ((int)(a).size())
#define clr(x)  memset( (x), 0, sizeof(x) )
#define all(c)  (c).begin(), (c).end()
#define entre(a,x,b)  (((a)<=(x)) && ((x)<(b)))
#define lg(n)   (8*sizeof(n)-__builtin_clz(n)-1)
template <class T> inline string tostr(const T&a) { ostringstream os(""); os << a; return os.str(); }
template <class T> inline T sqr(const T&x) { return x*x; }
// structs
typedef int tipo;
struct punto{
	tipo x,y;
	punto():x(0),y(0){}
	punto(tipo x,tipo y):x(x),y(y){}
	punto operator-(){ return punto(-x,-y); }
	punto operator+( const punto& p ){ return punto(x+p.x,y+p.y);}
	punto operator-( const punto& p ){ return punto(x-p.x,y-p.y); }
	bool  operator<( const punto& p )const{ return (y==p.y)?x<p.x:y<p.y; }
	bool operator==( const punto& p )const{ return y==p.y&&x==p.x; }
	punto operator=( const punto& p ){ x=p.x;y=p.y; return *this; }
	tipo  operator*( const punto& p ){ return x*p.x+y*p.y; }
	tipo  operator^( const punto& p ){ return x*p.y-y*p.x; }
	template<class T>
	punto operator*( const T& c ){ return punto(x*c,y*c); }
};

template<class T> struct Ftree{
	vector<T> v;
	Ftree(int n) {v.resize((1<<lg(n)+1)+1,0);}
	T range(int a) {T s=0;for(++a;a;a&=a-1)s+=v[a];return s;}
	void add(int p,T c) {for(++p;p<sz(v);p+=p&-p)v[p]+=c;}
};

// debuging
#define DBG(x)   cerr << __LINE__ << " :: " << #x << " = " << (x) << endl;
#define DEBUG(x) cerr << __LINE__ << " :: " << #x << " = " << (x); cin.get()
template <class T> ostream& operator<<( ostream& o, vector<T>& v ) // vector
{ o << endl << '['; forall(i,v) o << (*i) << ','; o << ']' ; return o; }
template <class U, class V> ostream& operator<<( ostream& o, pair<U,V>& p) // pair
{ o << '(' << p.first << ',' << p.second << ')'; return o; }
ostream& operator<<( ostream& o, punto& p ) // punto
{ o << '(' << p.x << ',' << p.y << ')'; return o; }

//typedefs
typedef long double   ld;
typedef long long     tint;
typedef pair<int,int> PII;

#define CV_(x,a) typedef vector< x > V##a;
#define CV(x,a) CV_(x,a) CV_(V##a,V##a) CV_(VV##a,VV##a)
CV(int,I) CV(tint,TI) CV(double,D) CV(ld,LD) CV(bool,B) CV(PII,PII) CV(string,S) CV(punto,P)
#undef CV
#undef CV_

// consts
const int inf  = 2134567890;
const int minf = 1234567890;
const int mx[] = {-1,0,1,0};
const int my[] = {0,-1,0,1};

//remember cp(bg,end,back_inserter(container));
//remember cin >> ws;



 #define cout sal
/// #define cin ent

long double dis( punto a,punto b){ return sqrt(sqr(a.x-b.x)+sqr(a.y-b.y)); }

int main(){
	ios::sync_with_stdio(false);
	ifstream ent("ent.txt");
	ofstream sal("sol.txt");
	int nc;
	cin >> nc;
	forn(l,nc){
		int n;
		cin >> n;
		vector<punto> p(n+3,punto(0,0));
		vector<int> r(n+3,0);
		forn(i,n){
			cin >> p[i].x >> p[i].y >> r[i];
		}
		
		long double sol = 10000000;
		if(n==1 || n==2 || p[0]==p[1] || p[1]==p[2] || p[0]==p[3])
			sol = 2*max( r[0], max(r[1], r[2]) );
		else{
			forn(i,n)
				forn(j,n)
					if(i!=j)
						sol = min( sol, dis(p[i],p[j])+r[i]+r[j] );
		}
		cout << "Case #" << l+1 << ": " << fixed << setprecision(6) << sol/2 << endl;
	}
	return 0;
}