#include <iostream>
#include <vector>
using namespace std ;
int main(){
	int T ; cin >> T ;
	for(int t = 0 ; t < T ; t++){
		int r, k, n ; cin >> r >> k >> n ;
		vector<int> to(n), earn(n), g(n) ;
		for(int i = 0 ; i < n ; i++) cin >> g[i] ;
		for(int i=0,j=0,x=0,ng=0; i < n ; i++){
			if(i!=0) x -= g[i-1] , ng --;
			while(ng < n && x + g[j] <= k){
				x += g[j] ; ng++ ; j = (j+1) % n ;
			}
			earn[i] = x ; to[i] = j ;
		}
		long long ans = 0; int now = 0 ;
		while(r--){
			ans += earn[now] ; now = to[now] ;
		}
		cout << "Case #" << t+1 << ": " << ans << endl ; 
	}
}
