#include <iostream>
#include <vector>

using namespace std;

int dr[] = {1, 1, 1, 0};
int dc[] = {-1, 0, 1, 1};

string grid[50];
string grid2[50];

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    int N, K;
    cin >> N >> K;
    for(int i = 0; i < N; i++) {
      cin >> grid[i];
      grid2[i] = string(N, 0);
    }
    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++) {
        grid2[j][N - i - 1] = grid[i][j];
      }
    }
    for(int i = 0; i < N; i++) {
      int pos = N - 1;
      for(int j = N - 1; j >= 0; j--) {
        if(grid2[j][i] != '.') {
          swap(grid2[pos--][i], grid2[j][i]);
        }
      }
    }
    int res = 0;
    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++) {
        char ch = grid2[i][j];
        int m = (ch == 'R' ? 1 : (ch == 'B' ? 2 : 0));
        if(!m) continue;
        if(m & res) continue;
        for(int dir = 0; dir < 4; dir++) {
          bool ok = true;
          for(int k = 0; k < K && ok; k++) {
            int r = i + k * dr[dir];
            int c = j + k * dc[dir];
            if(r < 0 || r >= N || c < 0 || c >= N || grid2[r][c] != ch) {
              ok = false;
            }
          }
          if(ok) res |= m;
        }
      }
    }
    cout << "Case #" << t << ": ";
    if(!res) cout << "Neither";
    if(res == 1) cout << "Red";
    if(res == 2) cout << "Blue";
    if(res == 3) cout << "Both";
    cout << endl;
  }
}
