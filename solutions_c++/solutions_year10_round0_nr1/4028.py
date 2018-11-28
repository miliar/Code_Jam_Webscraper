#include<iostream>
using namespace std;

FILE *r, *w;

void solve( int t ) {
     
     int n, k;
     fscanf( r, "%d %d", &n, &k );
     
     k %= ( 1 << n );
     if( k + 1 == ( 1 << n ) ) fprintf( w, "Case #%d: ON\n", t );
     else fprintf( w, "Case #%d: OFF\n", t );
          
}

int main() {
    
    int t;
    
    r = fopen( "a-large.in", "r" );
    w = fopen( "a-large.out", "w" );
    
    fscanf( r, "%d", &t );
    
    for( int i = 0; i < t; i++ ) solve( i + 1 );
     
    return 0;    
}
