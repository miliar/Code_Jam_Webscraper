/* C Libs */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
/* IOstream Libs */
#include <iostream>
#include <fstream>
#include <sstream>
/* String Libs */
#include <string>
/* STL Containers */
#include <bitset>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
/* STL Algorithm */
#include <algorithm>
/* Miscellaneous */
#include <complex>
#include <functional>
#include <iterator>
//#include <limits>
#include <numeric>
#include <typeinfo>
#include <utility>
#include <valarray>

using namespace std;

#define REP(i,s,t) for(int _t=t,i=s;i<_t;i++ )
#define REPP(i,s,t) for(int _t=t,i=s;i<=_t;i++)

#define LET(x,a) __typeof(a) x (a)
#define ITER(i,a,b) for(LET(i,a);i!=(b);++i)
#define FOREACH(it,v) ITER(it,v.begin(),v.end())

#define FILLA(a,x) memset(&a,x,sizeof(a))
#define FILL(a,x) memset(a,x,sizeof(a))
#define CLEARA(a,x) FILLA(a,0)
#define CLEAR(a) FILL(a,0)

#define m_p make_pair
#define fst first
#define snd second
typedef pair<int,int> PII;
typedef long long ll;
template<class T> void check_max( T&a, T b ){ if ( a < b ) a = b; }
template<class T> void check_min( T&a, T b ){ if ( a > b ) a = b; }

//#define debug


const int MAXN = 250;

struct Point{
	int x,y;
	void read(){cin>>x>>y;}
};
struct Chain{
	int n;
	vector<Point> l;
	void read(int _n){
		n = _n;
		l.clear();
		REP(i,0,n){
			Point p;
			p.read();
			l.push_back( p );
		}
	}
	double gety( int x ){
		int i;
		for( i = 0; i < (int) l.size(); i++ )
			if ( l[i].x >= x )
				break;
		if ( l[i].x == x )
			return l[i].y;
		else
			return l[i-1].y + double( l[i].y-l[i-1].y ) * ( x-l[i-1].x )/(l[i].x-l[i-1].x);
	}
}l,u;
int W,L,U,G;

vector<double> yl,yu,h;
vector<int> x;

double a[MAXN],b[MAXN];

double get_s( double cx ){
	double res = 0;
	for ( int i = 1; i < (int)x.size(); i++ ){
		if ( x[i] <= cx )
			res += (h[i]+h[i-1])*(x[i]-x[i-1])/2;
		else{
			double ch = h[i-1] + (h[i]-h[i-1])*(cx-x[i-1])/(x[i]-x[i-1]);
			res += (ch+h[i-1])*(cx-x[i-1])/2;
			break;
		}
	}
	return res;
}
double get_next_x( double cx, double part ){
	double l = cx, r = W;
	while ( r-l > 1e-9 ){
		double m = (l+r)/2;
		double s = get_s( m ) - get_s(cx);
		if ( s > part )
			r = m;
		else
			l = m;
	}
	return (r+l)/2;
}

int main(){
	int T; cin >> T;
	REP(Case,1,T+1){
		cin >> W>>L>>U>>G;
		
		l.read(L);
		u.read(U);

		x.clear();
		REP(i,0,l.n)x.push_back( l.l[i].x );
		REP(i,0,u.n)x.push_back( u.l[i].x );
		sort(x.begin(),x.end());
		x.resize( unique(x.begin(),x.end()) - x.begin());

		yl.clear(); yu.clear();
		REP(i,0,x.size()){
			yl.push_back( l.gety( x[i] ) );
			yu.push_back( u.gety( x[i] ) );
		}
		/*
		puts("points");
		REP(i,0,x.size()){
			printf("%d : [%.4lf , %.4lf]\n",x[i],yl[i],yu[i]);
		}
		*/
		
		h.clear();
		REP(i,0,x.size())
			h.push_back( yu[i] - yl[i] );
		double all_s = 0;
		REP(i,0,x.size()-1){
			all_s += (h[i]+h[i+1])*(x[i+1]-x[i])/2;
		}

		printf("Case #%d:\n",Case);

		double part = all_s / G;
		G--;
		double cx = 0;
		while ( G-- ){
			cx = get_next_x( cx, part );
			printf("%.8lf\n",cx);
		}
	}
	return 0;
}
