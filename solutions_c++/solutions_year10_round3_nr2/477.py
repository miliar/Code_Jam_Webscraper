#include<iostream>
#include<set>
#include<vector>
#include<string>
using namespace std;

FILE *in, *out;

int pot( int a, int b ) {
    
    int p = 1;

    while( b ) {
           p *= a;
           b--;
    }    
    
    return p;
        
}

void fun( int x ) {
     
     int l, p, c;
     fscanf( in, "%d %d %d", &l, &p, &c );

     int ret = 0;
    
     for( ret = 0; ; ret++ ) {
     
          double l1 = l;
          double p1 = p;
          double c1 = c * c;
          for( int i = 0; i < ret; i++ ) {
               
               c1 *= c1;
                    
          }
          
          if( l1 * c1 >= p1 ) {
          
              if( l1 * c < p1 ) ret++;         
              
              break;
          }
          
     }
     
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
