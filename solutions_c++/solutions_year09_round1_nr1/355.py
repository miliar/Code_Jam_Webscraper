#include <iostream>
#include <map>
#include <string>
#include <sstream>
using namespace std ;
#define MAX 12000000
char dp[11][MAX] ;
inline int f(int x, int p){
	int ans = 0 ;
	while(x){
		int t = x % p ; 
		ans += t * t ;
		x /= p ;}
	return ans ;
}
int g(int x , int p){
	if(dp[p][x] != 0) return dp[p][x] ;
	dp[p][x] = -1 ;
	int r = f(x,p) ;
	if(r == 1) return dp[p][x] = 1 ;
	if(r == x) return dp[p][x] =-1 ;
	else return dp[p][x] = g(r,p) ;
}
int main(){
	string s ;
	int T ; cin >> T ; getline(cin,s) ;
	memset(dp,0,sizeof(dp)) ;
	for(int p = 2 ; p <= 10 ; p++){
		for(int x = 1 ; x < MAX ; x++){
			dp[p][x] = g(x,p) ;
		}
		//cout << int(dp[p][11814485]) << endl ;
	}
	for(int t = 1 ; t <= T ; t++){
		getline(cin,s) ;
		istringstream sin(s) ;
		int tmp , n = 0 ;
		int d[10] ;
		while(sin >> tmp) d[n++] = tmp ;
		int ans = 1 ;
		while(ans++){
			bool c = true ;
			for(int i = 0 ; i < n ; i++){
				if(dp[d[i]][ans] != 1){
					c = false ; continue ;
				}
			}
			if(c) break ;
		}
		cout << "Case #" << t << ": " << ans << endl ;
	}
}
