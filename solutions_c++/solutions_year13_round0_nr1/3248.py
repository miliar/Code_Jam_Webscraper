#include <iostream>
#include <string>
using namespace std;

string s[10];

int dir[4][2] = { {0, 1}, {1, 0}, {1, 1}, {1,-1} };
inline int out( int x, int y ) {
       if( x >= 4 || y >= 4 ) return 1;
       return 0;
}

int solve() {
    int vis[10][10]={0};
    for( int i = 0 ; i < 4; ++i ) {
         for( int j = 0; j < 4; ++j ) {
              if( s[i][j] == 'X' || s[i][j] == 'T' ) {
                  for( int k = 0; k < 4; ++k ) {
                       int x = i, y = j, step = 0;
                       while( step < 4 && !out(x, y) 
                              && (s[x][y] == 'X' || s[x][y] == 'T') ) {
                              x += dir[k][0];
                              y += dir[k][1];
                              step++;
                       }
                       if( step >= 4 ) {
                            //cout<<"x="<<i<<" y="<<j<<" "<<k<<endl;
                            return 0;
                       } 
                  }
              }
              
              if( s[i][j] == 'O' || s[i][j] == 'T' ) {
                  for( int k = 0; k < 4; ++k ) {
                       int x = i, y = j, step = 0;
                       while( step < 4 && !out(x, y) 
                              && (s[x][y] == 'O' || s[x][y] == 'T') ) {
                              x += dir[k][0];
                              y += dir[k][1];
                              step++;
                       }
                       if( step >= 4 ) {
                          // cout<<"x="<<i<<" y="<<j<<" "<<k<<endl;
                           return 1; 
                       }
                  }              
              }
              
              if( s[i][j] == '.' ) vis[i][j] = 1;
         }
    }
    
    for( int i = 0 ; i < 4; ++i ) 
    for( int j = 0 ; j < 4; ++j )
    if( vis[i][j] ) return 3;
    return 2;
}

int main() {
    int T;
    cin>>T;
    for( int tc = 1; tc <= T; ++tc ) {
         for( int i = 0 ; i < 4; ++i ) {
              cin>>s[i];
         }
         cout<<"Case #"<<tc<<": ";
         int ret = solve();
         switch( ret ) {
                 case 0: cout<<"X won"<<endl;break;
                 case 1: cout<<"O won"<<endl;break;
                 case 2: cout<<"Draw"<<endl; break;
                 case 3: cout<<"Game has not completed"<<endl;
         }
    }
    return 0;
}
