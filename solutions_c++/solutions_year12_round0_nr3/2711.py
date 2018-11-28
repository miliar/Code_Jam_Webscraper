#include <iostream>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

int pow10 (int i) {
	if ( i == 0 )
		return 1 ;
	else if ( i % 2 == 0) {
		int r = pow10(i/2) ;
		return r * r ;
	}
	else {
		int r = pow10(i/2) ;
		return r * r * 10 ;	
	}
}

int main() {
	
	int N ;
		
	cin >> N ;
	
	for (int _i = 1 ; _i <= N ; _i++) {
		
		int a,b ;
		
		int r = 0 ;
		
		cin >> a >> b ;
		
		for (int i = a ; i < b ; i++) {
			
			int nbc = floor(log10(i)) + 1 ;			
			vector<int> Memory ;
			Memory.resize(0) ;
			for ( int j = 1 ; j < nbc ; j++) {
				int haut = i / pow10(nbc-j) ;
				int bas = i % pow10(nbc-j) ;
				int c = bas*pow10(j) + haut ;
				
				
				if (floor(log10(c)) + 1 == nbc && c > i && c <= b) {
					for ( int k = 0 ; k < Memory.size() ; k++ ){
						if (Memory[k] == c) {
							r-- ;
							break ;
						}
					}
					r++ ;
					Memory.push_back(c) ;

				}
				
			}
			
			
		}
		
		cout << "Case #" << _i << ": " << r << endl ;

		
	}
	
	return 0 ;
}
