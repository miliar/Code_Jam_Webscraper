#include <iostream>
using namespace std;

char mp[103][103];
int cou[106][2], ccou[106][2];

double wp[103], owp[103], oowp[103];
double wpp[103];


int main()
{
    freopen("A-large.in", "r" , stdin );
    freopen("out.txt", "w" , stdout );
     
    int T;
    cin >> T;
    for( int Case = 1; Case <= T; ++Case ){         
         cout << "Case #" << Case << ":" << endl;
         
         int n; cin >> n;
         for( int i = 0; i < n; ++i ) {
              cou[i][0] = 0; cou[i][1] = 0;
              for( int j = 0; j < n; ++j ) {
              cin >> mp[i][j];
              if( mp[i][j] != '.') cou[i][int( mp[i][j] - '0' )]++;
              }
         }
         
         for( int i = 0; i < n; ++i ){
              wp[i] = (double) cou[i][1] / ( double( cou[i][0] + cou[i][1] ) );
         }
         
         for( int i = 0; i < n; ++i ){
              owp[i] = 0;
              
              for( int j = 0; j < n; ++j ){
                   ccou[j][0] = 0; ccou[j][1] = 0;
                   for( int m = 0; m < n; ++m ){
                        if( m != i && mp[j][m] != '.' ){
                            ccou[j][int( mp[j][m] - '0' )]++;
                        }
                   }
              }
              
              for( int j = 0; j < n; ++j ){
                   wpp[j] = (double) ccou[j][1] / ( double( ccou[j][0] + ccou[j][1] ) );
              }
              
              int pp = 0;
              for( int j = 0; j < n; ++j ){
                   if(  mp[i][j] != '.' ){
                        ++pp;
                        owp[i] += wpp[j];
                   }
              }
              if( pp != 0 )
                    owp[i] /= pp; 
         }
         
          for( int i = 0; i < n; ++i ){
              oowp[i] = 0;
              for( int j = 0; j < n; ++j ){
                   if( mp[i][j] != '.' ){
                       oowp[i] += owp[j];
                   }
              }
              oowp[i] = oowp[i] / double ( cou[i][0] + cou[i][1] );
         }
         
         for( int i = 0; i < n; ++i ){
              cout << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;     
         }
    }
    
         
    
}
