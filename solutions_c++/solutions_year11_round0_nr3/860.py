#include <iostream>

using namespace std ;

int main(void){
	int T ;
	
	cin >> T ;
	for( int i_case=1 ; i_case<=T ; i_case++ ){
		int N ;
		int sum = 0 ;
		int mask = 0 ;
		int min = 0x7FFFFFFF ;
		int value ;
		
		cin >> N ;
		while( N-- ){
			cin >> value ;
			
			sum += value ;
			mask ^= value ;
			
			if( min > value )
				min = value ;
		}
		
		if( mask )
			cout << "Case #" << i_case << ": NO" << endl ;
		else		
			cout << "Case #" << i_case << ": " << sum-min << endl ;
	}

	return 0 ;
}