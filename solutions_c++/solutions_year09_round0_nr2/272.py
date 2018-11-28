#include <iostream>
#include <vector>
#include <map>
using namespace std;

int dx[] = { -1, 0, 0, 1 }, dy[] = { 0, -1, 1, 0 };
int H, W;

void flow(int cx, int cy, vector<vector<int> >& grid, vector<vector<int> >& comp, int& compn) {
  vector<pair<int, int> > path;

  int compv = -1;
  while (compv == -1) {
    path.push_back(make_pair(cx, cy));

    int nx = -1, ny = -1, ne = 1000000;
    for (int k = 0; k < 4; k++) {
      if (cx+dx[k] >= 0 && cx+dx[k] < H && cy+dy[k] >= 0 && cy+dy[k] < W && grid[cx+dx[k]][cy+dy[k]] < ne) {
        nx = cx + dx[k];
        ny = cy + dy[k];
        ne = grid[nx][ny];
      }
    }

    if (ne >= grid[cx][cy]) compv = compn++;
    else if (comp[nx][ny] != -1) compv = comp[nx][ny];
    cx = nx; cy = ny;
  }

  for (int i = 0; i < path.size(); i++)
    comp[path[i].first][path[i].second] = compv;
}

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    cin >> H >> W;

    vector<vector<int> > grid(H, vector<int>(W));
    for (int i = 0; i < H; i++)
      for (int j = 0; j < W; j++)
        cin >> grid[i][j];

    vector<vector<int> > comp(H, vector<int>(W, -1));
    int compn = 0;
    for (int i = 0; i < H; i++)
      for (int j = 0; j < W; j++) {
        if (comp[i][j] != -1) continue;
        flow(i, j, grid, comp, compn);
      }

    char cur = 'a';
    map<int, char> letter;
    for (int i = 0; i < H; i++)
      for (int j = 0; j < W; j++) {
        if (letter.find(comp[i][j]) != letter.end()) continue;
        letter[comp[i][j]] = cur++;
      }

    cout << "Case #" << c << ":" << endl;
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++)
        cout << letter[comp[i][j]] << " ";
      cout << endl;
    }
  }
  return 0;
}
