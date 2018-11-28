#include <iostream>
#include <cstring>

using namespace std;


int
main( ) {

	int t , n;
	int tab[ 2000 ][ 2 ];
	

	cin >> t;

	for( int i = 0 ; i < t; ++i ) {

		cin >> n;
  
        int w = 0;
        
        for( int j = 0 ; j < n ; ++j ) {
             
             cin >> tab[ j ][ 0 ];
             cin >> tab[ j ][ 1 ];
             
             for( int k = 0 ; k < j ; ++k ) {
             
                  if( tab[ k ][ 0 ] > tab[ j ][ 0 ] ) {
                      
                      if( tab[ k ][ 1 ] < tab[ j ][ 1 ] ){
                          
                          ++w;
                      }
                  }
                  if( tab[ k ][ 0 ] < tab[ j ][ 0 ] ) {
                      
                      if( tab[ k ][ 1 ] > tab[ j ][ 1 ] ){
                          
                          ++w;
                      }
                  }
             }
        }

		cout << "Case #" << i + 1 << ": " << w << endl;
	}


	return 0;
}
