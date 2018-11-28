#include<iostream>

using namespace std;

int T;
int n, h, l;
int a[1000];

int gcd ( int p, int q ) {
  if ( q == 0 )
    return p;
  else return gcd( q, p%q );
  
}

int main() {
  
  FILE* fin = fopen ( "C-small-attempt2.in", "r" );
  FILE* fout = fopen ( "C-small-attempt2.out", "w" );
  
  fscanf ( fin, "%d", &T );
  
  for ( int Z = 1; Z <= T; Z++ )
  {
    memset ( a, 0, sizeof(a) );
    fscanf ( fin, "%d %d %d", &n, &l, &h );
    for ( int i = 0; i < n; i++ )
      fscanf ( fin, "%d", &a[i] );
    bool fnd;
    for ( int k = l; k <= h ; k++ )
    {
      a[n] = k;
      fnd = true;
      for ( int i = 0; (i < n) && fnd; i++ )
        if (!( (a[i]%k==0) || (k%a[i]==0) ))
          fnd = false;
      if ( fnd )
        break;
    }
    fprintf ( fout, "Case #%d: ", Z );
    if ( fnd )
      fprintf ( fout, "%d\n", a[n] );
    else fprintf ( fout, "NO\n" );
  }
  
  fclose ( fin );
  fclose ( fout );
  return 0;
  
}
