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
using namespace std;

#define all(c) ((c).begin()), ((c).end()) 
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end()) 
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)

typedef long long ll;

int readint() { 
  int i, j, s;
  while (!isdigit(i = getchar()) && i != '-');
  if (i == '-') { s = -1; j = 0; }
  else { s = 1; j = i - '0'; }
  while (isdigit(i = getchar())) j = ((j << 1) + (j << 3) + (i - '0'));
  return j * s;
}

typedef pair<int, int> pii;
typedef vector<pii> vpii;
#define X first
#define Y second

const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};

int W, H, N;
char fld[20][20];

int dist(pii &a, pii &b) {
  return abs(a.X - b.X) + abs(a.Y - b.Y);
}

int par[10];
int parent(int x) {
  return par[x] == x ? x : par[x] = parent(par[x]);
}

int danger(vpii &s) {
  rep (i, N) par[i] = i;
  rep (i, N) rep (j, N) {
    if (i == j) continue;
    if (dist(s[i], s[j]) > 1) continue;
    int p = parent(i);
    int q = parent(j);
    par[p] = q;
  }
  rep (i, N) rep (j, N) {
    if (parent(i) != parent(j)) return 1;
  }
  return 0;
}

int main() {
  int cases = readint();
  rep (ca, cases) {
    H = readint();
    W = readint();
    vpii s, g;
    memset(fld, '#', sizeof(fld));
    for (int y = 1; y <= H; y++) {
      for (int x = 1; x <= W; x++) {
        scanf(" %c", &fld[y][x]);
        if (fld[y][x] == 'o') s.pb(mp(x, y));
        if (fld[y][x] == 'x') g.pb(mp(x, y));
        if (fld[y][x] == 'w') s.pb(mp(x, y)), g.pb(mp(x, y));
        if (isalpha(fld[y][x])) fld[y][x] = '.';
      }
    }
    W += 2;
    H += 2;
    N = s.size();
    sort(all(s));
    sort(all(g));

    map<vpii, int> mem;
    queue<vpii> que;
    que.push(s);
    mem[s] = 0;

    while (!que.empty()) {
      s = que.front(); que.pop();
      if (s == g) break;

      rep (i, N) fld[s[i].Y][s[i].X] = 'o';
      /*
      rep (y, H) {
        rep (x, W) printf("%c", fld[y][x]);
        puts("");
      }
      puts("");
      */
      
      int dng = danger(s);
      int cst = mem[s];

      rep (i, N) {
        int x = s[i].X;
        int y = s[i].Y;
        rep (d, 4) {
          int tx = x + dx[d];
          int ty = y + dy[d];
          int hx = x - dx[d];
          int hy = y - dy[d];

          if (fld[ty][tx] != '.') continue;
          if (fld[hy][hx] != '.') continue;

          vpii t = s;
          t[i] = mp(tx, ty);
          sort(all(t));

          if (mem.count(t)) continue;
          if (dng + danger(t) > 1) continue;
          
          que.push(t);
          mem[t] = cst + 1;
        }
      }

      rep (i, N) fld[s[i].Y][s[i].X] = '.';
    }

    printf("Case #%d: ", ca + 1);
    if (mem.count(g)) printf("%d\n", mem[g]);
    else printf("-1\n");
  }
}
