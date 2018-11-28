#include <iostream>
#include <vector>
#include <algorithm>
using namespace std ;
int f(int x, int v , int dp[][2] , int m , vector<int>&g , vector<int> &c){
	if(dp[x][v] != -1) return dp[x][v] ;
	if(x >= (m-1)/2){
		if(v == g[x]) return 0 ;
		else return 20000 ;
	}else{
		int minv = 20000 ;
		if(v == 1){
			if(g[x] == 1){
				int a = f(x*2+1,1,dp,m,g,c) ;
				int b = f(x*2+2,1,dp,m,g,c) ;
				minv <?= a+b ;
				if(c[x])
					minv <?= 1 + min(a,b); 
			}else{
				int a = f(x*2+1,1,dp,m,g,c) ;
				int b = f(x*2+2,1,dp,m,g,c) ;
				minv <?= min(a,b) ;
			}
		}else{
			int a = f(x*2+1,0,dp,m,g,c) ;
			int b = f(x*2+2,0,dp,m,g,c) ;
			if(g[x] == 1){
				minv = min(a,b) ;
			}else{
				minv <?= a + b ;
				if(c[x])
					minv <?= 1 + min(a,b) ;
			}
		}
		return dp[x][v] = minv ;
	}
}
int main(){
	int testcase ;
	cin >> testcase ;
	for(int T = 1 ; T <= testcase ; T++){
		int m , v ;
		cin >> m >> v ;
		vector<int> g , c , d ;
		for(int i = 0 ; i < (m-1)/2 ; i++){
			int a , b ;
			cin >> a >> b ;
			g.push_back(a) ;
			c.push_back(b) ;
		}
		for(int i = 0 ; i < (m+1)/2 ; i++){
			int a ;
			cin >> a ;
			g.push_back(a) ;
		}
		int dp[11000][2] ;
		for(int i = 0 ; i < 11000 ; i++){
			dp[i][0] = dp[i][1] = -1 ;
		}
		int ans = f(0,v,dp,m,g,c) ;
		cout << "Case #"<<T <<": " ;
		if(ans >= 20000)
			cout << "IMPOSSIBLE" << endl ;
		else
			cout << f(0,v,dp,m,g,c) << endl; 
	}
}
