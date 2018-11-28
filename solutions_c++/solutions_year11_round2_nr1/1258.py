#include<iostream>
#include<cstring>
#include<algorithm>
#include<string>

int g[1000][1000];
int T;
int n;
double wp[1000], owp[1000], oowp[1000], rpi[1000];
int cwp[1000], cowp[1000], coowp[1000];

using namespace std;

int main() {
  
  FILE* fin = fopen ( "A-large.in", "r" );
  FILE* fout = fopen ( "A-large.out", "w" );
  
  fscanf ( fin, "%d", &T );
  
  for ( int Z = 1; Z <= T; Z++ )
  {
    fscanf ( fin, "%d\n", &n );
    memset ( g, 0, sizeof(g) );
    memset ( cwp, 0, sizeof(cwp) );
    memset ( cowp, 0, sizeof(cowp) );
    memset ( coowp, 0, sizeof(coowp) );
    for ( int i = 0; i < n; i++ )
      wp[i] = owp[i] = oowp[i] = rpi[i] = 0.0;
      
    for ( int i = 0; i < n; i++, fscanf ( fin, "\n" ) )
      for ( int j = 0; j < n; j++ )
      {
        char ch;
        fscanf ( fin, "%c", &ch );
        if ( ch == '.' )
          g[i][j] = 0;
        else if ( ch == '1' )
          g[i][j] = 2;
        else if ( ch == '0' )
          g[i][j] = 1;
      }
    for ( int i = 0; i < n; i++ )
    {
      for ( int j = 0; j < n; j++ )
        if ( g[i][j] != 0 )
        {
          cwp[i] += 1;
          if ( g[i][j] == 2 )
            wp[i] += 1;
        }
    }
//    for ( int i = 0; i < n; i++ )
//      cout << wp[i]/cwp[i] << endl;
    for ( int i = 0; i < n; i++ )
    {
      for ( int j = 0; j < n; j++ )
        if ( g[i][j] != 0 )
        {
          cowp[i] += 1;
          owp[i] += (wp[j]-(g[j][i]==2?1:0))/(cwp[j]-1);
        }
      owp[i] /= cowp[i];
    }
//    for ( int i = 0; i < n; i++ )
//      cout << owp[i] << endl;
    for ( int i = 0; i < n; i++ )
    {
      for ( int j = 0; j < n; j++ )
        if ( g[i][j] != 0 )
        { 
          coowp[i] += 1;
          oowp[i] += owp[j];
        }
      oowp[i] /= coowp[i];
    }
//    for ( int i = 0; i < n; i++ )
//      cout << oowp[i]/coowp[i] << endl;
    
    for ( int i = 0; i < n; i++ )
      rpi[i] = 0.25*(wp[i]/cwp[i])+0.5*owp[i]+0.25*oowp[i];
    
    fprintf ( fout, "Case #%d:\n", Z );
    for ( int i = 0; i < n; i++ )
      fprintf ( fout, "%.6lf\n", rpi[i] );
//    system("PAUSE");
  }
  
  fclose ( fin );
  fclose ( fout );

  return 0;
  
}
