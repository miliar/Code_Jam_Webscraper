#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std ;
int sol(int n , int s, int S , vector<int>&query , int dp[][1000]){
	if(dp[s][n] != -1) return dp[s][n] ;
	if(s == query[n]) return dp[s][n] = 1000 ;
	if(n == 0) return 0 ;
	int min = -1 ;
	for(int i = 0 ; i < S ; i++){
		int times = sol(n-1 , i , S,query,dp) + ((i==s)?0:1);
		if(times < min || min == -1) min = times ;
	}
	return dp[s][n] = min ;
}
int main(){
	int T ;
	cin >> T ;
	for(int tcase = 1 ; tcase <= T ; tcase++){
		int S , Q ;
		cin >> S ;
		map<string,int> m ;
		for(int i = 0 ; i < S ; i++){
			string name ;
			if(i == 0 ) getline(cin,name) ;
			getline(cin,name) ;
			m[name] = i ;
		}
		cin >> Q;
		vector<int> query(Q) ;
		for(int i = 0 ; i < Q ; i++){
			string name ;
			if(i == 0 ) getline(cin,name) ;
			getline(cin, name );
			query[i] = m[name] ;
		}
		int dp[100][1000] ;
		for(int i = 0 ; i < 100 ; i++){
			for(int j = 0 ; j < 100 ; j++){
				dp[i][j] = -1 ;
			}
		}
		int min = -1 ;
		for(int i = 0 ; i < S ; i++){
			int times = sol(Q-1,i,S,query,dp) ;
			if(times < min || min == -1) min = times ;
		}
		cout << "Case #" << tcase << ": " << min << endl ;
		/*      for(int i = 0 ; i < Q ; i++){
				for(int j = 0 ; j < S ; j++){
				cout << dp[j][i] <<' ' ;
				}
				cout << endl ;
				}
				*/
	}
}

