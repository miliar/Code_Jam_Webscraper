#include<iostream>
#include<map>
#include<vector>
#include<set>
#include<string>
#include<queue>
#include<cstring>
#include<algorithm>
using namespace std;

char a[ 101 ][ 101 ];

double rpi( double wp, double owp, double oowp ) {
       return 0.25 * wp + 0.5 * owp + 0.25 * oowp;       
}

double wp1[ 101 ], owp1[ 101 ], oowp1[ 101 ];
int pobjede[ 101 ], utakmice[ 101 ];

void solve( int t ) {

     int n;
     cin >> n;
     
     memset( pobjede, 0, sizeof( pobjede ) );
     memset( utakmice, 0, sizeof( utakmice ) );
     
     for( int i = 0; i < n; i++ )
     wp1[ i ] = owp1[ i ] = oowp1[ i ] = 0.0;
     
     for( int i = 0; i < n; i++ )
     scanf( "%s", a[ i ] );
     
     for( int i = 0; i < n; i++ ) {
     
          int br_u = 0, br_p = 0;
          
          for( int j = 0; j < n; j++ ) {
          
               if( a[ i ][ j ] != '.' ) br_u++;
               if( a[ i ][ j ] == '1' ) br_p++; 
               
          }
          
          pobjede[ i ] = br_p;
          utakmice[ i ] = br_u;
          wp1[ i ] = 1. * br_p / (double)br_u;
          
     }
     
     for( int i = 0; i < n; i++ ) {
     
          double tmp = 0.0;
          for( int j = 0; j < n; j++ ) {
          
               if( i == j ) continue;
               if( a[ i ][ j ] == '.' ) continue;
          
               if( a[ j ][ i ] == '1' && utakmice[ j ] > 1 && pobjede[ j ] > 0 ) tmp += (double)( pobjede[ j ] - 1 ) / (double)( utakmice[ j ] - 1 ); 
               else if( a[ j ][ i ] == '0' && utakmice[ j ] > 1 ) tmp += (double)( pobjede[ j ] ) / (double)( utakmice[ j ] - 1 ); 
               else if( utakmice[ j ] ) tmp += (double)( pobjede[ j ] ) / (double)( utakmice[ j ] );
               
          }
          
          owp1[ i ] =  tmp / (double)utakmice[ i ];
          
     }
     
     for( int i = 0; i < n; i++ ) {
     
          double tmp = 0.0;
          for( int j = 0; j < n; j++ ) {
          
               if( a[ i ][ j ] == '.' ) continue;
               if( i == j ) continue;
               
               tmp += owp1[ j ]; 
               
          }
          
          oowp1[ i ] = tmp / (double)utakmice[ i ];
          
     }
     
     cout << "Case #" << t + 1 << ":" << endl;
     for( int i = 0; i < n; i++ )
     printf( "%.10f\n", rpi( wp1[ i ], owp1[ i ], oowp1[ i ] ) );
     
     
}

int main() {

    int t;
    cin >> t;
    
    for( int i = 0; i < t; i++ ) 
         solve( i );     

    return 0;
}
