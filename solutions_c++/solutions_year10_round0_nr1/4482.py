#include<iostream>

using namespace std;

int main() {
  
  int t;
  int n, k;
  int c[28];
  c[0] = 1;
  FILE* fin = fopen ( "A-small-attempt0.in", "r" );
  FILE* fout = fopen ( "A-small-attempt0.out", "w" );
  for ( int i = 1; i < 28; i++ )
    c[i] = c[i-1]*2;
  for ( int i = 1; i < 28; i++ )
    c[i] -= 1;
/*  
  for ( int i = 1; i < 28; i++ )
    printf ( "%d\n", c[i] );
*/    

  fscanf ( fin, "%d", &t );
  
  for ( int z = 1; z <= t; z++ )
  {
    fprintf ( fout, "Case #%d: ", z );
    fscanf ( fin, "%d %d", &n, &k );
    
    if ( c[n] == (c[n]&k) )
      fprintf ( fout, "ON\n" );
    else fprintf ( fout, "OFF\n" );
  };    

//system("PAUSE");
  return 0;
};
