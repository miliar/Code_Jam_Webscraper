#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    int H, W;
    cin >> H >> W;

    int m[100][100];
    char b[100][100];
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        cin >> m[i][j];
        b[i][j] = 0;
      }
    }
    char ch = 'a';
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        int ii = i;
        int jj = j;
        vector<int> tr_h, tr_w;
        while (true) {
          tr_h.push_back(ii);
          tr_w.push_back(jj);
          if (b[ii][jj] > 0) break;
          int iii = ii;
          int jjj = jj;
          if (ii > 0 && m[iii][jjj] > m[ii-1][jj]) {
            iii = ii-1; jjj = jj;
          }
          if (jj > 0 && m[iii][jjj] > m[ii][jj-1]) {
            iii = ii; jjj = jj-1;
          }
          if (jj + 1 < W && m[iii][jjj] > m[ii][jj+1]) {
            iii = ii; jjj = jj+1;
          }
          if (ii + 1 < H && m[iii][jjj] > m[ii+1][jj]) {
            iii = ii+1; jjj = jj;
          }
          if (iii == ii && jjj == jj) {
            b[ii][jj] = ch++;
            break;
          }
          ii = iii;
          jj = jjj;
        }
        for (int t = 0; t < tr_h.size(); t++) {
          b[tr_h[t]][tr_w[t]] = b[ii][jj];
        }
      }
    }
    cout << "Case #" << cas << ": " << endl;
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        if (j > 0) cout << ' ';
        cout << b[i][j];
      }
      cout << endl;
    }
  }
  return 0;
}

