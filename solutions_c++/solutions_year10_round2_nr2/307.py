#include <iostream>
#include <vector>
using namespace std ;
int main(){
	int C ; cin >> C ;
	for(int c = 1 ; c <= C ; c++){
		int n, k , b , t ; cin >> n >> k >> b >> t ;
		vector<int> x(n), v(n), good(n) ;
		for(int i = 0 ; i < n ; i++) cin >> x[i] ;
		for(int i = 0 ; i < n ; i++){
			cin >> v[i] ;
			if(v[i] * t >= (b-x[i])) good[i] = 1 ;
		}
		int bad = 0, swap = 0 ;
		for(int i = n-1 ; i >= 0 ; i--){
			if(!good[i]) bad++ ;
			else if(k != 0) k--, swap += bad ; 
		}
		cout << "Case #" << c << ": " ;
		if(k == 0) cout << swap << endl ;
		else cout << "IMPOSSIBLE" << endl ;
	}
}
