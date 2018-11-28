#include <iostream>
#include <algorithm>
#include <numeric>
#include <cstdio>

using namespace std;

int main(void)
{
  int tc, cnt = 0;
  cin >> tc;
  while( tc-- ){
    int n;
    cin >> n;
    int g[n][n];
    for(int i=0; i<n; ++i){
      for(int j=0; j<n; ++j){
        char c;
        cin >> c;
        if( c == '.' )g[i][j] = 2;
        else g[i][j] = c - '0';
      }
    }

    /*
    for(int i=0; i<n; ++i){
      for(int j=0; j<n; ++j){
        cout << g[i][j] << ' ' ;
      }
      cout << endl;
    }
    */

    double wp[ n ];
    double owp[ n ];
    double oowp[ n ];

    for(int i=0; i<n; ++i){
      int win = 0;
      int game = 0;
      for(int j=0; j<n; ++j){
        if( g[i][j] == 2 )continue;
        if( g[i][j] == 1 )++win;
        ++game;
      }
      wp[i] = (double)win / (double)game;
    }

    //cout << endl;

    for(int i=0; i<n; ++i){
      double sum = 0;
      double cnt = 0;
      for(int j=0; j<n; ++j){
        if( g[i][j] == 2 )continue;
        double game = 0;
        double win = 0;
        for(int k=0; k<n; ++k){
          if( g[j][k] == 2 )continue;
          if( k == i )continue;
          ++game;
          if( g[j][k] == 1 )++win;
        }
        ++cnt;
        sum += win / game;
      }
      owp[i] = sum / cnt;
    }

    /*
    for(int i=0; i<n; ++i){
      double s = 0, c = 0;
      for(int j=0; j<n; ++j){
        double sum = 0, cnt = 0;
        if( g[i][j] == 2 )continue;
        for(int k=0; k<n; ++k){
          if( g[j][k] == 2 )continue;
          if( k == i )continue;
          double win = 0, game = 0;    
          for(int l=0; l<n; ++l){
            if( g[k][l] == 2 )continue;
            if( l == j )continue;
            ++game;
            if( g[k][l] == 1 )++win;
          }
          ++cnt;
          sum += win / game;
        }
        cout << (char)()
        ++c;
        s += sum / cnt;
      }
      oowp[i] = s / c;
    }
    */

    for(int i=0; i<n; ++i){
      double sum = 0, cnt = 0;
      for(int j=0; j<n; ++j){
        if( g[i][j] == 2 ) continue;
        ++cnt;
        sum += owp[j];
      }
      oowp[i] = sum / cnt;
    }

    /*
    cout << "wp" << endl;
    for(int i=0; i<n; ++i)cout << i << " : " << wp[i] << endl;
    cout << "owp" << endl;
    for(int i=0; i<n; ++i)cout << i << " : " << owp[i] << endl;
    cout << "oowp" << endl;
    for(int i=0; i<n; ++i)cout << i << " : " << oowp[i] << endl;
    */

    cout << "Case #" << ++cnt << ":" << endl;
    for(int i=0; i<n; ++i){
      double r = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
      //cout << r << endl;
      printf("%.12lf\n", r);
    }
  }
  return 0;
}
