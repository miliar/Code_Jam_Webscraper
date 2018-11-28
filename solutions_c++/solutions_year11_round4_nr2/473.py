#include<iostream>
#include<set>
#include<stack>
#include<string>
#include<sstream>
#include<numeric>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
typedef long long ll;
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
long long X[600][600], Y[600][600], M[600][600];
long long aX[600][600], aY[600][600], aM[600][600];
int main(){
  int t; scanf("%d", &t);
  for(int i = 0; i < 11; i++) X[i][0] = X[0][i] = Y[i][0] = Y[0][i] = M[i][0] = M[0][i] = 0;

  for(int caso = 1; caso <= t; caso++){
    int r, c, d;
    cin >> r >> c >> d;
    for(int i = 0; i < r; i++)
      for(int j = 0; j < c; j++){
        char w; cin >> w;
        M[i + 1][j + 1] = (w - '0') + d;
        X[i + 1][j + 1] = M[i + 1][j + 1] * (i + 1); 
        Y[i + 1][j + 1] = M[i + 1][j + 1] * (j + 1); 
      }

    r++, c++;
    for(int i = 0; i < r; i++) for(int j = 0; j < c; j++) 
        aX[i][j] = 0, aY[i][j] = 0, aM[i][j] = 0;

    for(int i = 1; i < r; i++) for(int j = 1; j < c; j++)
        aM[i][j] = M[i][j] + aM[i - 1][j] + aM[i][j - 1] - aM[i - 1][j - 1],
        aX[i][j] = X[i][j] + aX[i - 1][j] + aX[i][j - 1] - aX[i - 1][j - 1],
        aY[i][j] = Y[i][j] + aY[i - 1][j] + aY[i][j - 1] - aY[i - 1][j - 1];
    int res = 0;
    for(int sz = 3; sz <= min(r - 1, c - 1); sz++){
      bool can = false;
      long long xx = 0, yy = 0, ww = 0;
      for(int i = 0; i < sz; i++) for(int j = 0; j < sz; j++){
        xx += i * 1;
        yy += j * 1;
        ww += 1;
      }
      xx -= 2 * (sz - 1);
      yy -= 2 * (sz - 1);
      ww -= 4;
      //ixx /= ww; yy /= ww;
     // xx++, yy++;
      for(int i = sz; i < r && !can; i++) for(int j = sz; j < c && !can; j++){
        long long x = aX[i][j] - aX[i][j - sz] - aX[i - sz][j] + aX[i - sz][j - sz];
        long long y = aY[i][j] - aY[i][j - sz] - aY[i - sz][j] + aY[i - sz][j - sz];
        long long w = aM[i][j] - aM[i][j - sz] - aM[i - sz][j] + aM[i - sz][j - sz];
        w -= M[i][j] + M[i - sz + 1][j] + M[i][j - sz + 1] + M[i - sz + 1][j - sz + 1];
        x -= X[i][j] + X[i - sz + 1][j] + X[i][j - sz + 1] + X[i - sz + 1][j - sz + 1];
        y -= Y[i][j] + Y[i - sz + 1][j] + Y[i][j - sz + 1] + Y[i - sz + 1][j - sz + 1];
        //x /= w;
        //y /= w;
        can |= w * xx == ww * (x + w * ( -i + sz -1)) &&
               w * yy == ww * (y + w * ( -j + sz -1));
      }
      if(can) res = max(res, sz);
    }
    cout << "Case #" << caso << ": ";
    if(res > 0) cout << res << endl;
    else cout << "IMPOSSIBLE" << endl;

  }
}

