#include <iostream>

using namespace std ;

int main(void){
	int T ;
	
	cin >> T ;
	for( int i_case=1 ; i_case<=T ; i_case++ ){
		int N ;
		cin >> N ;
		
		int ans = 0 ;
		for( int i=1 ; i<=N ; i++ ){
			int value ;
			cin >> value ;
			
			if( value != i )
				ans ++ ;
		}
		
		cout << "Case #" << i_case << ": " << ans << ".000000" << endl ;
	}

	return 0 ;
}
