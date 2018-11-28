#include <cstdio>
#include <cstring>
#include <fstream>

#define KONJ 42 - 42

FILE *fin = fopen( "googleRecycledIn.txt", "r" );
FILE *fout = fopen( "googleRecycledOut.txt", "w" );

using namespace std;

int T, A, B;
bool bio[20000100];

int rotate( int x ){

    int init = x, ret = 0;
    while ( x != init || ret == 0 ){
          
          //printf( "%d\n", x );
          
          ret += ( bio[x] == false && x >= A && x <= B ); bio[x] = true;
          
          int p = 10;
          while ( x % p == 0 ){ p *= 10; }
          
          //if ( x % p == x ) break;
          
          int lo = x % p, hi = x / p;
          p = 1;
          
          while ( hi % p != hi ) p *= 10;
          x = lo * p + hi; 
                     
    }
    
    return ret;
    
}

void solve( int t ){

     printf( "%d", t );

     long long sol = 0;
     memset( bio, false, sizeof bio );
     
     fscanf( fin, "%d%d", &A, &B );
     
     for ( int i = A; i <= B; ++i ){
         if ( bio[i] ) continue;
         long long tmp = ( long long ) rotate( i );
         sol += ( long long ) tmp * ( tmp - 1 ) / 2;
     }

     fprintf( fout, "Case #%d: %lld\n", t, sol );

}

int main( void ){

    fscanf( fin, "%d", &T );
    for ( int i = 0; i < T; ++i ) solve( i + 1 );

    return KONJ;

}
 
