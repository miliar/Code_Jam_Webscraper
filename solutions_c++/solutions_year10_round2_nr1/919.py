#include<iostream>
#include<set>
#include<string>
using namespace std;

set <string> S;
int ret;
FILE *in, *out;

void pocepaj ( string x ) {

        x += "/";

        string tmp;
        for( int i = 2; i < x.size(); i++ ) {
             if( x[ i ] == '/' ) {
                 tmp = x.substr( 0, i );   
                 if( S.find( tmp ) == S.end() ) {
                     ret++;
                     S.insert( tmp );     
                 }
             }     
        }
        
        
}

void fun( int x ) {

     ret = 0;
     
     int n, m;
     fscanf( in, "%d %d", &n, &m );
     
     char buff[ 128 ];
     string s;
     
     for( int i = 0; i < n; i++ ) {
          fscanf( in, "%s", buff );
          s = buff;
          S.insert( s );     
     }
     
     for( int i = 0; i < m; i++ ) {
          fscanf( in, "%s", buff );
          s = buff;
          pocepaj( s );      
     }
     
     S.clear();
     
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
