#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>

using namespace std ;

#define FOR(i, n) for(int i = 0 ; i < (n) ; i++)

const int Max_N = 50 + 10 ;

string S[] = {"Neither", "Red", "Blue", "Both"} ;
int n, k ;
char b[Max_N][Max_N], r[Max_N][Max_N] ;

void input(){
	scanf(" %d %d", &n, &k);
	FOR(i, n)
		FOR(j, n)
			scanf(" %c", &b[i][j]) ;
}

void rotate(){
	FOR(i, n) FOR(j, n) r[i][j] = '.' ;
	FOR(i, n){
		for(int j = n-1, cnt = n-1; j >= 0 ; j--)
			if ( b[i][j] != '.' )
				r[cnt--][n-1-i] = b[i][j] ;
	}
	/*FOR(i, n){
		FOR(j, n)
			cerr << r[i][j] ; 
		cerr << endl ;
	}*/
}	

bool valid(int x, int y, char c){
	bool ret0, ret1, ret2 ;
	ret0 = ret1 = ret2 = true ;
	for(int q = 0 ; q < k ; q++){
		ret0 *= (x-q >= 0 && r[x-q][y] == c) ;
		ret1 *= (y-q >= 0 && r[x][y-q] == c) ;
		ret2 *= (x-q >= 0 && y-q >= 0 && r[x-q][y-q] == c) ;
	}
	return ret0 || ret1 || ret2 ;
}

int solve(){
	int ret = 0, fR = false, fB = false ;
	FOR(i, n)
		FOR(j, n){
			if ( !fR && valid(i, j, 'R') )
				ret += 1, fR = true ;
			if ( !fB && valid(i, j, 'B') )
				ret += 2, fB = true ;
		}
	return ret ;
}

int main(){
	int T ; scanf(" %d", &T) ;
	for(int i = 0 ; i < T ; i++){
		input() ;
		rotate() ;
		cout << "Case #" << i + 1 << ": " << S[solve()] << endl ;
	}
}
