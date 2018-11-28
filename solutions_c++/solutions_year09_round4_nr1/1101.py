#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
using namespace std ;
int main(){
	int T ; cin >> T ;
	for(int t = 1 ; t <= T ; t++){
		int n ; cin >> n ;
		vector<int > d(n) ;
		for(int i = 0 ; i < n ; i++){
			string s ; cin >> s ;
			for(int j = 0 ; j < n ; j++)
				if(s[j] == '1') d[i] = j+1 ;
		}
		int ans = 0 ;
		for(int i = 0 ; i < n ; i++){
//			for(int j = 0 ; j < n ; j++) cout << ' ' << d[j] ;
//			cout << endl; 
			for(int j = i ; j < n ; j++){
				if(d[j] <= i+1){
					for(int k = j ; k > i ; k--)
						swap(d[k-1],d[k]) ;
					 ans += j - i ;
					break ;
				}
			}
		}
		cout << "Case #" << t << ": " << ans << endl ;
	}
}

