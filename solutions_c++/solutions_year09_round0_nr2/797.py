#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int A[100][100];
int vis[100][100];

int dr[] = {-1, 0, 0, 1};
int dc[] = {0, -1, 1, 0};

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    int rows, cols; cin >> rows >> cols;
    for(int i = 0; i < rows; i++) {
      for(int j = 0; j < cols; j++) {
        cin >> A[i][j];
      }
    }
    int nxt = 0;
    memset(vis, -1, sizeof(vis));
    for(int i = 0; i < rows; i++) {
      for(int j = 0; j < cols; j++) {
        if(vis[i][j] != -1) continue;
        vector<int> v;
        int ci = i;
        int cj = j;
        while(vis[ci][cj] == -1) {
          v.push_back(ci * cols + cj);
          int xi = -1, xj = -1;
          for(int k = 0; k < 4; k++) {
            int ni = ci + dr[k];
            int nj = cj + dc[k];
            if(ni < 0 || ni >= rows || nj < 0 || nj >= cols || A[ni][nj] >= A[ci][cj]) continue;
            if(xi == -1 || A[ni][nj] < A[xi][xj]) {
              xi = ni; xj = nj;
            }
          }
          if(xi == -1) {
            vis[ci][cj] = nxt++;
          } else {
            ci = xi; cj = xj;
          }
        }
        for(int i = 0; i < v.size(); i++) {
          int zi = v[i] / cols;
          int zj = v[i] % cols;
          vis[zi][zj] = vis[ci][cj];
        }
      }
    }
    cout << "Case #" << t << ":" << endl;
    for(int i = 0; i < rows; i++) {
      for(int j = 0; j < cols; j++) {
        cout << (j?" ":"") << (char)('a' + vis[i][j]);
      }
      cout << endl;
    }
  }
}
