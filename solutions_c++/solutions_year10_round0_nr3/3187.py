#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std ;

const int Max_N = 1000 + 100 ;
int t, n, r, k, next[Max_N], val[Max_N], g[Max_N] ;

void input(){
	scanf(" %d %d %d", &r, &k, &n) ;
	for(int i = 0 ; i < n ; i++) 
		scanf(" %d", &g[i]) ;
}

int main(){
	scanf(" %d", &t) ;
	for(int tst = 0 ; tst < t ; tst++){
		input() ;
		//---------------------------------------------------
		for(int i = 0 ; i < n ; i++){
			next[i] = (i+1 == n ? 0 : i+1) ; val[i] = g[i] ;
			for(int j = next[i] ; j != i ; j = next[i]){
				if ( g[j] + val[i] > k ) break ;
				next[i] = (j+1 == n ? 0 : j+1) ; val[i] += g[j] ;
			}
			//cerr << i << " is: " << next[i] << " " << val[i] << endl ;
		}
		//---------------------------------------------------
		int ans = 0 ;
		for(int v = 0, R = r ; R-- ; v = next[v] ){
			ans += val[v] ;
		}
		//---------------------------------------------------
		cout << "Case #" << tst + 1 << ": " << ans << endl ;
	}
}
