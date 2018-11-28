#include <iostream>
#include <string>
#include <vector>
using namespace std ;
int main(){
	string s ;
	int n ; cin >> n ; getline(cin,s) ;
	string pattern = "welcome to code jam" ;
	vector<int> p[256] ;
	for(int i = 0 ; i < 19 ; i++){
		p[pattern[i]].push_back(i+1) ;
	}
	for(int i = 1 ; i <= n ; i++){
		getline(cin,s) ;
		int dp[20] = {1} ;
		int length = s.length() ;
		for(int j = 0 ; j < length ; j++){
			for(int k = 0 ; k < p[s[j]].size() ; k++){
				int x = p[s[j]][k] ;
				dp[x] += dp[x-1] ;
				dp[x] %= 10000 ;
			}
		}
		printf("Case #%d: %04d\n", i, dp[19]) ;
	}

}
