#include <iostream>
#include <vector>
using namespace std ;
int main(){
	int T ; cin >> T ;
	for(int Case = 1 ; Case <= T ; Case++){
		int t ; cin >> t ;
		int turn = 0, pc[2] = {1,1}, tc[2] = {0,0} ; // Orange=>0, Blue=>1
		for(int i = 0 ; i < t ; i++){
			char c ; int p ; cin >> c >> p ;
			int r = (c == 'O') ? 0 : 1 ;
			int d = p - pc[r] ;
			if(d < 0) d = -d ;
			int tp = 1 ;
			if(d > tc[r]) tp += d - tc[r] ;
			turn += tp ; pc[r] = p ; tc[r] = 0 ; tc[!r] += tp ;
		}
		cout << "Case #" << Case << ": " << turn << endl ;
	}
}
