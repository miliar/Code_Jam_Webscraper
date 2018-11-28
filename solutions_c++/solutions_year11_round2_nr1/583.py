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

const double EPS=(1e-10);
const int MAXN = 100+10 ;

//#define __FILE_IO_


int N ;
string statics[ MAXN ] ;

double WP( int id ){
	int win = 0 , total = 0 ;
	FOR( i , N )if( i != id ){
		if( statics[id][i] == '1') win ++ ;
		if( statics[id][i] != '.' ) total ++ ;
	}
	//cout << id << win  << total;
	assert( total != 0 ) ;
	return win*1.0 / total ;
}

double WP( int id , int p ){
	int win = 0 , total = 0 ;
	FOR( i , N )if( i != id && i != p ){
		if( statics[id][i] == '1') win ++ ;
		if( statics[id][i] != '.' ) total ++ ;
	}
	//cout << id << win  << total;
	assert( total != 0 ) ;
	return win*1.0 / total ;
}

double OWP( int id ){
	double ret = 0 ;
	int cnt = 0 ;
	FOR( i, N )if( i != id && statics[id][i] != '.' ){
		ret += WP( i , id ) ;
		cnt ++ ;
	}
	return  ret / cnt ;
}

double OOWP( int id ){
	double ret = 0 ; int cnt = 0 ;
	FOR( i, N )if( i != id && statics[id][i] != '.' ){
		ret += OWP( i ) ;
		cnt ++ ;
	}
	return ret / cnt ;
}
double calc( int id ){
	return .25*WP(id) + .5*OWP(id) + .25*OOWP(id);
}
int main(){

	#ifdef __FILE_IO__
		freopen("a.in","r",stdin);
		freopen("out.out","w",stdout);
	#endif

	int testcase ;
	cin >> testcase ;
	FOR( tc ,testcase ){
		cout << "Case #" << tc + 1 << ":" << endl ;
		cin >> N ;
		FOR( i , N ){
			cin >> statics[ i ] ;
		}
		//FOR( i , N ) cout << statics[i] << endl;
		FOR( i , N ){
			printf("%.9lf\n",calc(i));
		}
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