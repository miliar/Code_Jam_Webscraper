#include <iostream>
#include <fstream>
using namespace std;
int i , j, n, k, T,K;
char a[60][60];
int f[60][60][4];
bool ans[2];
ifstream fin( "1.in" );
ofstream fout("1.out");
int main()
{
    fin >> T;
    int TT = T;
    while (T--)
    {
          memset( a, 0, sizeof(a) );
          memset( f, 0, sizeof(f) );
          ans[0] = ans[1] = false;
          
          fin >> n >> K;
          for ( i = 0 ; i < n; ++i )
          {
              
              for ( j = 0; j < n; ++j )
                  fin >> a[j][n-i-1];
          }
          for ( i = n-1; i >= 0 ; --i )
              for ( j = 0; j < n ; ++j )
              {
                  int t = i;
                  while ( t < n && a[t+1][j] == '.' )
                  {
                        a[t+1][j] = a[t][j];
                        a[t][j] = '.';
                        ++t;
                  }
              }
          for (i = n-1; i >= 0; --i )
              for ( j = n-1; j >= 0; --j )
                  if ( a[i][j] != '.' )
                  {
                     if ( a[i][j] == a[i][j+1] )
                        f[i][j][0] = f[i][j+1][0] +1;

                     if ( a[i][j] == a[i+1][j] )
                        f[i][j][1] = f[i+1][j][1] +1;
                        
                     if ( a[i][j] == a[i+1][j+1] )
                        f[i][j][2] = f[i+1][j+1][2] +1;
                        
                     if ( j > 0 && a[i][j] == a[i+1][j-1] )
                        f[i][j][3] = f[i+1][j-1][3] +1;
                     for ( k = 0; k < 4; ++k )
                         if ( f[i][j][k] >= K-1 )
                         {
                              if ( a[i][j] == 'R' ) ans[0] = true;
                              if ( a[i][j] == 'B' ) ans[1] = true;
                         }                                                               
                  }
          fout << "Case #"<< TT-T<<": ";
          if ( ans[0] && !ans[1] )
             fout << "Red"<<endl;
          if ( !ans[0] && ans[1] )
             fout << "Blue"<<endl;
          if ( ans[0] && ans[1] ) fout << "Both"<<endl;
          if ( !ans[0] && !ans[1] ) fout << "Neither"<<endl;
          
    }
    //system("pause");
}
