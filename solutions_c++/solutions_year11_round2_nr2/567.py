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

const double eps=(1e-10);
const int MAXN = 200+10 ;

int dcmp( double x ){
	return x < -eps ? -1 : x > eps ? 1 : 0; 
}

int P[ MAXN ] , V[ MAXN ] ;
int N , D;
int check( double t ){
	double last = -1e50;
	FOR( i ,  N){
		double left  = max( P[i] - t , last ) ;
		double right = P[i] + t ;
		if( dcmp( ( right - left ) - (V[i]-1)*D ) < 0 ) return 0;
		checkmax( last, left + V[i]*D ) ;
	}
	return 1;
}
//#define __FILE_IO_
int main(){

	#ifdef __FILE_IO__
		freopen("a.in","r",stdin);
		freopen("out.out","w",stdout);
	#endif

	int testcase ;
	cin >> testcase ;
	FOR( tc ,testcase ){
		cout << "Case #" << tc + 1 << ": ";
		cin >> N >> D ;
		FOR( i , N ){
			cin >> P[i]  >> V[i] ;
		}
		double lo = 0 , hi = 1e50 , ret;
		while( lo + eps < hi ){
			double md = ( lo + hi ) / 2 ;
			if( check(md) ) {
				ret = md ;
				hi = md - eps ;
			}else lo = md + eps ;
		}
		printf("%.10lf\n", ret );
	}
}
/*
2
4
.11.
0.00
01.1
.10.

*/