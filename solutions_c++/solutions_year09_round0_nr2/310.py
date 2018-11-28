#include <stdio.h>
#include <map>
#include <set>

using namespace std;

int dr[4] = {-1, 0, 0, 1};
int dc[4] = {0, -1, 1, 0};

pair<int, int> parent[100][100];

pair<int, int> find(int r, int c) {
  if (parent[r][c].first == r && parent[r][c].second == c) return parent[r][c];
  return (parent[r][c] = find(parent[r][c].first, parent[r][c].second));
}

int main() {
  int T;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; ++t) {
    int R, C;
    scanf("%d %d\n", &R, &C);
    int ht[R][C];
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        scanf((j==C-1) ? "%d " : "%d\n", &ht[i][j]);
        parent[i][j] = make_pair(i, j);
      }
    }
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        int flow = -1;
        for (int k = 0; k < 4; ++k) {
          int r = i+dr[k], c = j+dc[k];
          if (r >= 0 && r < R && c >= 0 && c < C && ht[r][c] < ht[i][j]) {
            if (flow < 0 || ht[r][c] < ht[i+dr[flow]][j+dc[flow]]) flow = k;
          }
        }
        if (flow >= 0) parent[i][j] = make_pair(i+dr[flow], j+dc[flow]);
      }
    }
    set<pair<int, int> > basin;
    for (int i = 0; i < R; ++i)
      for (int j = 0; j < C; ++j) {
        parent[i][j] = find(i, j);
        basin.insert(parent[i][j]);
      }
    map<pair<int, int>, char> name;
    char letter = 'a';
    for (int i = 0; i < R; ++i)
      for (int j = 0; j < C; ++j)
        if (name.find(parent[i][j]) == name.end())
          name[parent[i][j]] = letter++;

    printf("Case #%d:\n", t);
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        printf("%c%s", name[parent[i][j]], (j < C-1) ? " " : "\n");
      }
    }
  }

  return 0;
}
