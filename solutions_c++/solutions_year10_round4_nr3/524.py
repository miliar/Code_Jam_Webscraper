#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std ;

const int Max_N = 100 + 10 ;
#define FOR(i, n) for(int i = 0 ; i < (n) ; i++)
#define SZ(x) (int)x.size()
#define PB push_back

int n, r, b[2][Max_N][Max_N] ;

void input(){
	n = 101 ; FOR(i, n) FOR(j, n) b[0][i][j] = b[1][i][j] = 0 ;
	scanf(" %d", &r);
	FOR(i, r){
		int x1, x2, y1, y2 ; scanf(" %d %d %d %d", &x1, &y1, &x2, &y2) ; 
		for(int x = x1-1 ; x < x2 ; x++)
			for(int y = y1-1 ; y < y2 ; y++)
				b[1][y][x] = true ;
	}
}

inline bool bact(int k, int i, int j){
	return ( (i >= 0 && j >= 0) ? b[k][i][j] : false ) ;
}

bool move(int t){
	int ne = t % 2, ol = (t+1) % 2, ret = 0 ;
	FOR(i, n){
		FOR(j, n){
			if ( !bact(ol, i-1, j) && !bact(ol, i, j-1) ) b[ne][i][j] = false ;
			else if ( bact(ol, i-1, j) && bact(ol, i, j-1) ) b[ne][i][j] = true ;
			else b[ne][i][j] = b[ol][i][j] ;
			ret = max(ret, b[ne][i][j]) ;
		}
	}
	return ret ;
}

int main(){
	int t ; scanf(" %d", &t) ;
	for(int tst = 0 ; tst < t ; tst++){
		input() ;
		int T ; for(T = 0 ; move(T) ; T++) ;
		printf("Case #%d: %d\n", tst+1, T+1) ;
	}
}
