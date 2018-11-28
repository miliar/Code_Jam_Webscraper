#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <climits>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

#define FOR(i,N) for(int i=0;i<(N);i++)
#define REP(i,a,b) for(int i=(a);i<=(b);i++)
#define MP make_pair
#define SIZE(X) ((int)(X.size()))

using namespace std;

typedef long long LL;
typedef unsigned long long LLU;

template<class T> void checkmin(T& a,T b){if(a>b)a=b;}
template<class T> void checkmax(T& a,T b){if(a<b)a=b;}
template<class T> T gcd(T a,T b){return b?gcd(b,a%b):a;}

const double eps=(1e-8);
const int MAXN = 200+10 ;

int dcmp( double x ){
	return x < -eps ? -1 : x > eps ? 1 : 0; 
}

//#define __FILE_IO_


struct Walk{
	int b , e , w ;
	Walk(){};
	Walk(int _b,int _e,int _w):b(_b),e(_e),w(_w){};
	void in(){
		cin >> b >> e >> w ;
	}
	bool operator < ( const Walk& T )const{
		return w > T.w ;
	}
} ;

map<int,int> ww;
int main(){

	#ifdef __FILE_IO__
		freopen("a.in","r",stdin);
		freopen("out.out","w",stdout);
	#endif

	int testcase ;
	cin >> testcase ;
	FOR( tc ,testcase ){
		int X,S,R,T,N;
		cout << "Case #" << tc + 1 << ": ";
		cin >> X >> S >> R >> T >> N;
		int remain = X ;
		ww.clear();
		Walk walk ;
		FOR( i , N ){
			walk.in();
			remain -= walk.e - walk.b;
			ww[ walk.w ] += walk.e - walk.b ;
		}
		if( remain > 0 ){
			ww[0] += remain;
		}
		double ret = 0 ;
		double tot = 0 ;
		for( map<int,int>::iterator p = ww.begin(); p != ww.end() ; p ++ ){
			if( tot < T ){
				double t = min( T-tot , (0.0+p->second) / ( p->first + R) );
				ret += t ;
				tot += t ;
				if( t*( p->first + R) < 0.0+p->second ){
					ret += ( p->second - t*( p->first + R) ) / ( S + p->first ) ;
				}
			}else{
				ret += (0.0+p->second) / ( p->first + S) ;
			}
		}
		printf("%.10lf\n",ret);
	}
}
