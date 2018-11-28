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

const int dr[] = {-1,0,1,0};
const int dc[] = {0,-1,0,1};

const int inf = 0x1f1f1f1f;

int T;
int C[1000][1000];

int W, H;
int Tx[2600], Ty[2600];
char board[60][60];
int dist[60][60];
int dist2[60][60];

bool ok(int r, int c) { return r >= 0 && c >= 0 && r < H && c < W && board[r][c] != '.'; }

void solve(int P) {

  scanf("%d%d", &H, &W);
  for (int i = 0; i < H; ++i)
    scanf("%s", board[i]);

  T = 0;
  for (int i = 0; i < H; ++i) {
    for (int j = 0; j < W; ++j) {
      if (board[i][j] == 'T') {
	Tx[T] = j;
	Ty[T] = i;
	++T;
      }
    }
  }

  queue<pii> q;

  memset(dist, inf, sizeof(dist));
  
  for (int i = 0; i < T; ++i) {
    dist[Ty[i]][Tx[i]] = 0;
    q.push(pii(Ty[i],Tx[i]));
  }
  while (!q.empty()) {
    int r = q.front().first, c = q.front().second;
    q.pop();
    for (int i = 0; i < 4; ++i) {
      int nr = r + dr[i], nc = c + dc[i];
      if (ok(nr, nc) && dist[nr][nc] == inf) {
	dist[nr][nc] = dist[r][c]+1;
	q.push(pii(nr, nc));
      }
    }
  }

  for (int i = 0; i < T; ++i) {
    memset(dist2, inf, sizeof(dist2));
    dist2[Ty[i]][Tx[i]] = 0;
    q.push(pii(Ty[i],Tx[i]));
    while (!q.empty()) {
      int r = q.front().first, c = q.front().second;
      q.pop();
      for (int i = 0; i < 4; ++i) {
	int nr = r + dr[i], nc = c + dc[i];
	if (ok(nr, nc) && dist2[nr][nc] == inf) {
	  dist2[nr][nc] = dist2[r][c]+1;
	  q.push(pii(nr, nc));
	}
      }
    }
    for (int j = 0; j < T; ++j)
      C[i][j] = dist2[Ty[j]][Tx[j]];
  }
  int cost = 0;


  if (T > 1) {
    for (int i = 1; i <= C[0][1]; ++i) cost += i-min(i, C[0][1]-i);
  }
  
  for (int i = 0; i < H; ++i)
    for (int j =0 ; j < W; ++j) { 
      if (ok(i,j)) cost += dist[i][j];
    }
    

  printf("Case #%d: %d\n", P, cost);
}

int main() {
  int n;
  scanf("%d", &n);
  init();
  for (int i = 1; i <= n; ++i) solve(i);
  return 0;
}
