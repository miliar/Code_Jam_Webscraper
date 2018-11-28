#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
using namespace std;
 
#define all(c) ((c).begin()), ((c).end()) 
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end()) 
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair

const int INF = 987654321;
const int dx[4] = {0, -1, 1, 0};
const int dy[4] = {-1, 0, 0, 1};

int W, H;
int fld[110][110];

int K, id[110][110];


int saiki(int x, int y) {
  if (id[y][x] != -1) return id[y][x];

  int mih = fld[y][x], mid = -1;
  rep (td, 4) {
    int th = fld[y + dy[td]][x + dx[td]];
    if (th < mih) {
      mih = th;
      mid = td;
    }
  }

  if (mid == -1) id[y][x] = K++;
  else id[y][x] = saiki(x + dx[mid], y + dy[mid]);
  return id[y][x];
}

int main() {
  int cases;
  scanf("%d", &cases);
  
  rep (ca, cases) {
    scanf("%d%d", &H, &W);
    rep (y, H + 2) rep (x, W + 2) fld[y][x] = INF;
    for (int y = 1; y <= H; y++) {
      for (int x = 1; x <= W; x++) scanf("%d", &fld[y][x]);
    }

    printf("Case #%d:\n", ca + 1);
    K = 0;
    memset(id, -1, sizeof(id));
    for (int y = 1; y <= H; y++) {
      for (int x = 1; x <= W; x++) {
        if (x > 1) putchar(' ');
        printf("%c", 'a' + saiki(x, y));
        //printf("%d", saiki(x, y));
      }
      puts("");
    }
  }

  return 0;
}
