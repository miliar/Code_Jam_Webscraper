#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
	
	int N,S,p,T ;
	
	cin >> T ;
	
	for (int _i = 1 ; _i <= T ; _i++) {
				
		cin >> N ;
		cin >> S ;
		cin >> p ;
		
		int result = 0 ;
		
		for (int i = 0 ; i < N ; i++) {
			int t ;
			cin >> t ;
			if ( t == 0 ) {
				if (p == 0) {
					result++ ;
				}
			}
			else if ( t <= 3 ) {
				if ( p <= 1 ) {
					result++ ;
				}
				if ( p == 2 && S > 0) {
					result++ ;
					S-- ;
				}
			}
			else if ( t >= p + 2 * (p-1)) {
				result++ ;
			}
			else if ( t >= p + 2*(p-2) && S > 0 ) {
				result++ ;
				S-- ;
			}
		}
		
		
		cout << "Case #" << _i << ": " << result << endl ;
	}
	
	return 0 ;
}
