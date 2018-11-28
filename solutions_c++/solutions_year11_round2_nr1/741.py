#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <iostream>
#include <cstdio>
#include <cassert>
using namespace std;
#define FOR(i,N) for(int i=0;i<(N);i++)
#define REP(i,a,b) for(int i=(a);i<=(b);i++)
int N ;string MAP[ 100+10 ] ;
double WP( int id , int p ){
	int win = 0 , total = 0 ;
	FOR( i , N )if( i != id && i != p ){
		if( MAP[id][i] == '1') win ++ ;
		if( MAP[id][i] != '.' ) total ++ ;
	}
	assert( total != 0 ) ;
	return win*1.0 / total ;
}

double OWP( int id ){
	double ret = 0 ;
	int cnt = 0 ;
	FOR( i, N )if( i != id && MAP[id][i] != '.' ){
		ret += WP( i , id ) ;
		cnt ++ ;
	}
	return  ret / cnt ;
}

double OOWP( int id ){
	double ret = 0 ; int cnt = 0 ;
	FOR( i, N )if( i != id && MAP[id][i] != '.' ){
		ret += OWP( i ) ;
		cnt ++ ;
	}
	return ret / cnt ;
}
int main(){
	int testcase ;cin >> testcase ;
	FOR( tc ,testcase ){
		cin >> N ;
		FOR( i , N )cin >> MAP[ i ] ;
		cout << "Case #" << tc + 1 << ":" << endl ;
		FOR( i , N ){
			printf("%.12lf\n",.25*WP(i,-1) + .5*OWP(i) + .25*OOWP(i));
		}
	}
}
