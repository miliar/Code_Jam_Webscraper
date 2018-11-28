#include <vector>
#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

#define MOD 10007

int main()
{
  int N;
  cin >> N;

  for (int cas = 1; cas <= N; cas++) {
    int H, W, R;
    cin >> H >> W >> R;

    vector<int> rx;
    vector<int> ry;
    for (int i = 0; i < R; i++) {
      int r, c;
      cin >> r >> c;
      rx.push_back(c);
      ry.push_back(r);
    }

    int tbl[128][128];
    memset(tbl, 0, sizeof(tbl));
    tbl[0][0] = 1;
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        int rock = 0;
        for (int k = 0; k < R; k++) {
          if (rx[k] == j+1 && ry[k] == i+1) {
            rock = 1;
            break;
          }
        }
        if (!rock) {
          if (i >= 1 && j >= 2) {
            tbl[i][j] += tbl[i-1][j-2] % MOD;
          }
          if (i >= 2 && j >= 1) {
            tbl[i][j] += tbl[i-2][j-1] % MOD;
          }
        }
      }
    }
    
    cout << "Case #" << cas << ": ";
    cout << tbl[H-1][W-1] % MOD << endl;
  }
  
  return 0;
}

