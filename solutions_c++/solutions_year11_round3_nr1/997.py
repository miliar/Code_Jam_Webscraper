#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(void)
{
  int cnt = 0;
  int tc;
  cin >> tc;
  while( tc-- ){

    int h, w;
    cin >> h >> w;
    char g[h][w];

    for(int i=0; i<h; ++i){
      for(int j=0; j<w; ++j){
        cin >> g[i][j];
      }
    }

    bool flg = true;
    for(int i=0; flg && i<h; ++i){
      for(int j=0; flg && j<w; ++j){
        if( g[i][j] == '#' ){
          if( i+1 < h && j+1 < w && g[i][j+1] == '#' && g[i+1][j] == '#' && g[i+1][j+1] == '#' ){
            g[i][j] = g[i+1][j+1] = '/';
            g[i+1][j] = g[i][j+1] = '\\';
          }
          else flg = false;
        }
      }
    }

    cout << "Case #" << ++cnt << ":" << endl; 
    if( !flg )cout << "Impossible" << endl;
    else{
      for(int i=0; i<h; ++i){
        for(int j=0; j<w; ++j){
          cout << g[i][j] ;
        }
        cout << endl;
      }
    }
  }
  return 0;
}
