#include<iostream>

using namespace std;

int T;
int r, c;
int g[100][100];
bool v[100][100];

bool canplace ( int p, int q ) {
  
  if ( p < r && q < c )
  {
    if ( (g[p][q]==1)&&(g[p+1][q]==1)&&(g[p][q+1]==1)&&(g[p+1][q+1]==1) )
    {
      g[p][q] = g[p+1][q+1] = 2;
      g[p+1][q] = g[p][q+1] = 4;
      return true;
    }
    else return false;
  }
  return false;
  
}

bool hasspace ( int p, int q ) {
  
  if ( p < r && q < c )
    return (g[p][q]==1)||(g[p+1][q]==1)||(g[p][q+1]==1)||(g[p+1][q+1]==1);
  return false;
  
}

int main() {
  
  FILE* fin = fopen ( "A-large.in", "r" );
  FILE* fout = fopen ( "A-large.out", "w" );
  
  fscanf ( fin, "%d", &T );
  
  for ( int Z = 1; Z <= T; Z++ )
  {
    memset ( g, 0, sizeof(g) );
    memset ( v, 0, sizeof(v) );
    fscanf ( fin, "%d %d\n", &r, &c );
    for ( int i = 1; i <= r; i++, fscanf ( fin, "\n" ) )
      for ( int j = 1; j <= c; j++ )
      {
        char ch;
        fscanf ( fin, "%c", &ch );
        g[i][j] = (ch=='#'?1:0);
      }
    bool fnd = true;
    for ( int i = 1; i <= r; i++ )
      for ( int j = 1; j <= c; j++ )
      if ( g[i][j] == 1 )
        if ( !canplace(i,j) )
        {
          fnd = false;
          break;
        }
    fprintf ( fout, "Case #%d:\n", Z );
    if ( !fnd )
      fprintf ( fout, "Impossible\n" );
    else
    {
      for ( int i = 1; i <= r; i++, fprintf ( fout, "\n" ) )
        for ( int j = 1; j <= c; j++ )
          if ( g[i][j] == 2 )
            fprintf ( fout, "/" );
          else if ( g[i][j] == 4 )
            fprintf ( fout, "\\" );
          else fprintf ( fout, "." );
    }
    
  }
  
  fclose ( fin );
  fclose ( fout );
  
  return 0;
  
}
