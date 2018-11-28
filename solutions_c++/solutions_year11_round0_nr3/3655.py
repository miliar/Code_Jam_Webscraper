#include<iostream>
#include<map>
#include<vector>
#include<set>
#include<string>
#include<queue>
#include<cstring>
#include<algorithm>
using namespace std;

int a[ 1000005 ];

int rijesi( int n ) {

     for( int i = 0; i < n; i++ )
     cin >> a[ i ];
     
     int maxi = 0;
     
     for( int i = 1; i < ( 1 << n ); i++ ) {
     
          int x = 0, y = 0;
          int k = 0;
          
          for( int j = 0; j < n; j++ )
          if( i & ( 1 << j ) ) x ^= a[ j ];
          else {
               y ^= a[ j ];
               k += a[ j ];
          }
          
          if( x == y )
          maxi >?= k;
          
     }
     
     return maxi;
}

int rijesi2( int n ) {

    for( int i = 0; i < n; i++ )
    scanf( "%d", &a[ i ] );
    
    sort( a, a + n );

    for( int i = 1; i < n; i++ ) {
         
         int k1 = 0, k2 = 0;
         
         int x = 0, y = 0;   
         
         for( int j = 0; j < i; j++ ) {
              k1 ^= a[ j ];
              x += a[ j ];
         }
         
         for( int j = i; j < n; j++ ) {
              k2 ^= a[ j ];
              y += a[ j ];
         }
         
         if( k1 == k2 ) return y;
    
    }
         
    
    
      
    return 0;
}

int main() {

    int t;
    cin >> t;
    
    for( int i = 0; i < t; i++ ) {
    
         int n;
         cin >> n;
         int r = rijesi2( n );
         
         cout << "Case #" << i + 1 << ": ";
         if( r ) cout << r;
         else cout << "NO";
         cout << endl;
         
    }

    return 0;
}
