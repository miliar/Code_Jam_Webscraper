#include<iostream>
#include<string>
#include<vector>

using namespace std;

int H, W, T;
int G[200][200];
int L[200][200];
int label;

int dr[4] = {-1,0,0,1};
int dc[4] = {0,-1,1,0};



int smurf(int r, int c) {
  if (L[r][c] != -1) return L[r][c];

  int tr, tc, td = G[r][c];

  for (int i = 0; i < 4; ++i) {
    int nr = r + dr[i];
    int nc = c + dc[i];
    if (nr < 0 || nr >= H) continue;
    if (nc < 0 || nc >= W) continue;
    if (G[nr][nc] < td) {
      td = G[nr][nc];
      tr = nr;
      tc = nc;
    }
  }
  if (td < G[r][c]) {
    return L[r][c] = smurf(tr, tc);
  } else {
    return L[r][c] = label++;
  }

}

int main() {
  cin >> T;

  for (int i = 0; i < T; ++i) {
    cin >> H >> W;
    memset(G, -1, sizeof(G));
    memset(L, -1, sizeof(L));
    label = 0;
    for (int r = 0; r < H; ++r)
    for (int c = 0; c < W; ++c)
      cin >> G[r][c];

    for (int r = 0; r < H; ++r)
    for (int c = 0; c < W; ++c)
      if (L[r][c] == -1) {
        smurf(r,c);
      }

    printf("Case #%d:\n", i+1);
    for (int r = 0; r < H; ++r) {
      for (int c = 0; c < W; ++c) {
        if (c) cout << " ";
        cout << (char)(L[r][c]+'a');
      }
      cout << endl;
    }

  }

  return 0;
}
