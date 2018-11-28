/* GCJ'08
 * Author: Per Austrin
 */
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <queue>

using namespace std;
#define dprintf debug && printf
bool debug = false;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<int, double> pid;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<ll> vll;
typedef set<string> ss;
typedef set<int> si;
typedef set<ll> sll;
typedef set<pii> spii;
typedef map<string, int> msi;
typedef map<ll,int> mli;
typedef map<string, string> mss;
typedef queue<int> qi;



void init() {
}


ll N;
ll W, H;

int ok(int x, int y) {return x >= 0 && y >= 0 && x < W && y < H; }

void solve(int P) {
  scanf("%lld%lld", &W, &H);
  N = W*H;

  assert(N >= W && N >= H && N/W == H);


  int dx1, dy1, dx2, dy2;
  scanf("%d%d%d%d", &dx1, &dy1, &dx2, &dy2);

  int r, c;
  scanf("%d%d", &c, &r);
  ll res = 0;
  int mark[200][200];
  memset(mark, 0, sizeof(mark));
  
  queue<pii> q;

  mark[c][r] = true;
  q.push(pii(c, r));

  while (!q.empty()) {
    int y = q.front().second, x = q.front().first;
    q.pop();
    if (ok(x+dx1,y+dy1) && !mark[x+dx1][y+dy1]) {
      mark[x+dx1][y+dy1] = true;
      q.push(pii(x+dx1,y+dy1));
    }
    if (ok(x+dx2,y+dy2) && !mark[x+dx2][y+dy2]) {
      mark[x+dx2][y+dy2] = true;
      q.push(pii(x+dx2,y+dy2));
    }
  }
  for (int i = 0; i < H; ++i)
    for (int j = 0; j < W; ++j)
      res += mark[j][i];
  
  printf("Case #%d: %lld\n", P, res);
}

int main() {
  int n;
  scanf("%d", &n);
  init();
  for (int i = 1; i <= n; ++i) solve(i);
  return 0;
}
