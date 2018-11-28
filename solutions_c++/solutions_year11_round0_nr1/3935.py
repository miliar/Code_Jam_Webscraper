#include<iostream>
#include<fstream>
#include<queue>

using namespace std;

int T;
int n;
char r[200];
int p[200];
queue<bool> q;
int x[200], y[200], nx, ny;
int a, b;

int main() {
  
  FILE* fin = fopen ( "A-large.in", "r" );
  FILE* fout = fopen ( "A-large.out", "w" );
  
  fscanf ( fin, "%d", &T );
  
  for ( int z = 1; z <= T; z++ )
  {
    int ans = 0;
    
    memset ( r, 0, sizeof(r) );
    memset ( p, 0, sizeof(p) );
    while ( q.size() ) q.pop();
    a = b = 1;
    nx = ny = 0;
    int tx, ty;
    tx = ty = 0;
    bool ba;
    ba = false;
    
    fscanf ( fin, "%d", &n );
    
    for ( int i = 0; i < n; i++ )
    {
      fscanf ( fin, " %c %d", &r[i], &p[i] );
      if ( r[i] == 'O' )
        x[nx++] = i;
      else y[ny++] = i;
      q.push ( r[i]=='O' );
      
      if ( i == 0 )
      {
        ans += abs( 1-p[i] )+1;
        if ( r[i] == 'O' )
        {
          ba = true;
          a = p[i];
          ty += abs(1-p[i])+1;
        }
        else
        {
          ba = false;
          b = p[i];
          tx += abs(1-p[i])+1;
        }
      }
      else
      {
        if ( r[i] == 'O' )
        {
          int k = abs ( a-p[i] );
          if ( ba )
          {
            ty += k + 1;
            ans += k + 1;
            tx = 0;
            a = p[i];
          }
          else
          {
            ans += max ( k-tx, 0 ) + 1;
            ty += max ( k-tx, 0 ) + 1;
            a = p[i];
            tx = 0;
            ba = true;
          }
        }
        else
        {
          int k = abs ( b-p[i] );
          if ( !ba )
          {
            tx += k+1;
            ans += k+1;
            ty = 0;
            b = p[i];
          }
          else
          {
            ans += max ( k-ty, 0 ) + 1;
            tx += max ( k-ty, 0 ) + 1;
            b = p[i];
            ty = 0;
            ba = false;
          }
        }
      }
      
      
    }
    
    
    fprintf ( fout, "Case #%d: %d\n", z, ans );
  }
  
  fclose ( fin );
  fclose ( fout );
  
  return 0;
  
}
