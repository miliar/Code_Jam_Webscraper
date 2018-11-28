#include<iostream>
#include<set>
#include<vector>
#include<string>
using namespace std;

FILE *in, *out;

vector < pair < int, int > > v;

void fun( int x ) {
     
     int n;
     fscanf( in, "%d", &n );
     
     for( int i = 0; i < n; i++ ) {
          int a, b;
          fscanf( in, "%d %d", &a, &b ); 
          v.push_back( make_pair( a, b ) );    
     }
     
     sort( v.begin(), v.end() );
     
     int ret = 0;
     for( int i = 0; i < n; i++ ) {
          int poc = v[ i ].first;
          int kra = v[ i ].second;
          
          for( int j = i + 1; j < n; j++ ) {
          
               if( v[ j ].second >= kra ) {
                   break;   
               }
               ret++;
               
          }
               
     }
     
     v.clear();
     
     fprintf( out, "Case #%d: %d\n", x, ret );
     
}

int main() {
    
    in = fopen( "A-small.in", "r+" );
    out = fopen( "A-small.out", "w+" );
    
    int t;
    fscanf( in, "%d", &t );
    
    for( int i = 0; i < t; i++ ) fun( i + 1 ); 
    
    return 0 ;    
}
