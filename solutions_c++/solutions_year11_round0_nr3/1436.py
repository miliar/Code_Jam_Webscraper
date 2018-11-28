#include <iostream>

using namespace std ;

int n  ;

int main(){
	int T ;
	cin >> T ;
	for(int it = 1 ; it <= T ; it++){
		cin >> n ;
		int sum = 0 , min = 1<<30 , xr = 0;
		for(int i=0;i<n;++i){
			int val ;
			cin >> val ;
			sum += val ;
			if(min > val)min = val ;
			xr ^= val ;
		}
		if(xr){
			cout << "Case #" << it <<": NO" << endl ;
		}
		else{
			int res = sum-min ;
			cout << "Case #" << it << ": " << res << endl ;
		}
	}
	return 0 ;
}
