#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cstdarg>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

#define pb push_back
#define mp make_pair
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define sz(x) ((int)(x).size())

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;

const int MAXH = 4;
const int MAXW = 4;

const char dc[] = { '|', '/', '-', '\\' };
const int dx[] = { 0, 1, 1, 1 };
const int dy[] = { -1, -1, 0, 1 };

int h, w;
int ty[MAXH][MAXW];
int goh[MAXH][MAXW];

int go(int x, int y) {
  if (x == w) { y++; x = 0; }
  if (y == h) {
    for (y = 0; y < h; y++)
      for (x = 0; x < w; x++)
        if (goh[y][x] != 1) return 0;
    return 1;
  }

  int res = 0;
  for (int d = -1; d <= 1; d += 2) {
    int nx = x + dx[ty[y][x]] * d;
    int ny = y + dy[ty[y][x]] * d;
    nx = (nx + w) % w; ny = (ny + h) % h;
    goh[ny][nx]++;
    res += go(x + 1, y);
    goh[ny][nx]--;
  }
  return res;
}

char buf[MAXW];
void solve() {
  scanf("%d%d", &h, &w);
  for (int y = 0; y < h; y++) {
    scanf("%s", buf);
    for (int x = 0; x < w; x++)
      for (ty[y][x] = 0; dc[ty[y][x]] != buf[x]; ty[y][x]++);
  }
  memset(goh, 0, sizeof goh);
  printf("%d\n", go(0, 0));
}

int main(int argc, char* argv[]) {
  {
    string fname = "std";
    if (argc >= 2) {
      fname = argv[1];
      if (fname.length() >= 3 && string(fname, fname.length() - 3) == ".in")
        fname = string(fname, 0, fname.length() - 3);
    }
    freopen((fname + ".in").c_str(), "r", stdin);
    freopen((fname + ".out").c_str(), "w", stdout);
  }

  int TC;
  assert(scanf("%d", &TC) >= 1);
  for (int TN = 1; TN <= TC; TN++) {
    printf("Case #%d: ", TN);
    eprintf("Case #%d\n", TN);
    solve();
  }
  return 0;
}
