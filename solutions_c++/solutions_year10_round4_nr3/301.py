#include <iostream>
using namespace std;

int g[128][128][2];

int main() {
  int t; cin >> t;
  for(int c = 1; c <= t; c++) {
    int n; cin >> n;

    for(int i = 0; i < 128; i++)
      for(int j = 0; j < 128; j++)
        g[i][j][0] = 0;

    for(int i = 0; i < n; i++) {
      int x1, y1, x2, y2; cin >> x1 >> y1 >> x2 >> y2;
      for(int j = x1; j <= x2; j++)
        for(int k = y1; k <= y2; k++)
          g[j][k][0] = 1;
    }

    int s = 0, tm = 0;
    while(true) {
      tm++;
      for(int i = 1; i < 128; i++)
        for(int j = 1; j < 128; j++) {
          if(g[i][j][s] == 1) {
            if(g[i-1][j][s] == 0 && g[i][j-1][s] == 0) g[i][j][1-s] = 0;
            else g[i][j][1-s] = 1;
          }
          else {
            if(g[i-1][j][s] == 1 && g[i][j-1][s] == 1) g[i][j][1-s] = 1;
            else g[i][j][1-s] = 0;
          }
        }
      s = 1-s;
      int ct = 0;
      for(int i = 0; i < 128; i++)
        for(int j = 0; j < 128; j++)
          ct += g[i][j][s];
      if(ct == 0) break;
    }

    printf("Case #%d: %d\n", c, tm);
  }

  return 0;
}
