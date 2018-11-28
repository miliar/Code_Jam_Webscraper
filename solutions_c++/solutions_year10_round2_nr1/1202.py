#include <iostream>
#include <cstring>

using namespace std;


int
main( ) {

	int t , n , m;
	string str[ 1000 ];
	string test;

	
	cin >> t;
	
	for( int i = 0 ; i < t ; ++i ) {
         
         cin >> n;
         cin >> m;
         
         for( int j = 0 ; j < n ; ++j ) {
         
              cin >> str[ j ]; 
              str[ j ] += "/";
         }
         
         int wyn = 0;
         int min;
         int g;
         int max;
         
         for( int j = 0 ; j < m ; ++j ) {
         
              cin >> test;
              
              test += "/";
              
              int w = 0;
              
              for( int l = 1; l < test.size( ) ; ++l ) {
                   
                    if( test[ l ] == '/' ) {
                        
                        ++w;
                    }
              }
              
              min = w;
              g = 0;
              max = 0;
              
              for( int k = 0 ; k < n ; ++k ) {
              
                   g = 0;
                   int l;
                   for( l = 1; l < test.size( ) ; ++l ) {
                   
                        if( l >= str[ k ].size( ) || test[ l ] != str[ k ][ l ] ) {
                        
                            if( g > max ) {
                            
                                max = g;    
                            }
                            break;
                        }
                        if( test[ l ] == '/' ) {
                            
                            ++g;
                        }
                   }
                   if( g > max ) {
                   
                       max = g;    
                   }
                   if( w - max < min ) {
                   
                       min = w - max;    
                   }
                   if( min == 0 ) {
                   
                       break;    
                   }
              }
              
              str[ n ] = test;
              ++n;
              
              wyn += min;
         }
         
         cout << "Case #" << i + 1 << ": " << wyn << endl;
    }    
    

	return 0;
}
