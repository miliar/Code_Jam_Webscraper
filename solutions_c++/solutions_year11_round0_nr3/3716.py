#include<iostream>
#include<algorithm>

using namespace std;

int T;
int n;
int cnt[20];
int a[10000];
int s;

int main() {
  
  FILE* fin = fopen ( "C-large.in", "r" );
  FILE* fout = fopen ( "C-large.out", "w" );
  
  fscanf ( fin, "%d", &T );
  
  for ( int z = 1; z <= T; z++ )
  {
    fprintf ( fout, "Case #%d: ", z );
    memset ( cnt, 0, sizeof(cnt) );
    fscanf ( fin, "%d", &n );
    s = 0;
    
    for ( int i = 0; i < n; i++ )
    {
      fscanf ( fin, "%d", &a[i] );
      int k = a[i];
      s += k;
      for ( int i = 0; i < 20; i++ )
      {
        cnt[i] += k&1;
        k = k>>1;
      }
    }
    
    sort ( a, a+n );
    
    bool fnd = true;
    int ult = 0;
    for ( int i = 0; i < 20; i++ )
    {
      ult = ult*2+cnt[i]>0?1:0;
      if ( cnt[i]&1 )
        fnd = false;
    }
    
    if ( !fnd )
    {
      fprintf ( fout, "NO\n" );
      continue;
    }
    
    s -= a[0];
    fprintf ( fout, "%d\n", s );
    
  }
  
  fclose ( fin );
  fclose ( fout );
  
  return 0;
  
}
