#include <iostream>
#include <vector>
#include <utility>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<char> VC;
typedef vector<VC> VVC;
typedef pair<int, int> PII;

PII nextStep(VVI &grid, PII &cur) {
  int di[] = {-1,0,0,1};
  int dj[] = {0,-1,1,0};
  int i = cur.first, j = cur.second, ni = i, nj = j;
  for (int t = 0; t < 4; ++t)
    if (grid[i+di[t]][j+dj[t]] < grid[ni][nj]) {
      ni = i+di[t]; nj = j+dj[t];
      }
  return PII(ni, nj);
  }

void setBasin(VVI &grid, VVC &basin, PII p, char &nextBas) {
  PII cur = p, nxt;
  while ((cur != (nxt = nextStep(grid, cur))) && !basin[nxt.first][nxt.second])
    cur = nxt;
  if (!basin[nxt.first][nxt.second])
    basin[nxt.first][nxt.second] = nextBas++;
  basin[p.first][p.second] = basin[nxt.first][nxt.second];
  }

int main() {
  int T; cin >> T;
  for (int c = 1; c <= T; ++c) {
    int H, W; cin >> H >> W;
    VVI grid(H+2, VI(W+2, 10000));
    for (int i = 1; i <= H; ++i)
      for (int j = 1; j <= W; ++j)
        cin >> grid[i][j];
    VVC basin(H+2, VC(W+2)); char nextBas = 'a';
    for (int i = 1; i <= H; ++i)
      for (int j = 1; j <= W; ++j)
        setBasin(grid, basin, PII(i, j), nextBas);
    cout << "Case #" << c << ":\n";
    for (int i = 1; i <= H; ++i) {
      cout << basin[i][1];
      for (int j = 2; j <= W; ++j)
        cout << ' ' << basin[i][j];
      cout << '\n';
      }
    }
  }