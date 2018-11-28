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


struct req { int x, y, z; 
  bool operator<(const req &r) const { return x < r.x; }
};


bool yless(const req &r1, const req &r2) { return r1.y < r2.y; }

void solve(int P) {

  req R[10000];

  int N;
  scanf("%d", &N);

  for (int i = 0; i < N; ++i) {
    scanf("%d%d%d", &R[i].x, &R[i].y, &R[i].z);
  }

  int res = 0;
  sort(R, R+N);
  int lastA = -1;
  for (int xl = N; xl >= 0; --xl)  {
    int saved = 0;
    int A = 0;
    if (xl > 0) A = R[xl-1].x;
    if (A == lastA) continue;
    for (int i = 0; i < xl; ++i) 
      if (R[i].y + R[i].z <= 10000-A) swap(R[saved++], R[i]);
    sort(R, R+saved, yless);
    for (int i = 0; i < saved; ++i) {
      if (saved <= res) break;
      if (i+1 < saved && R[i].y == R[i+1].y) continue;
      int B = R[i].y, C = 10000-A-B;
      int cnt = 0;
      for (int j = 0; j <= i; ++j) {
	if (R[j].z <= C)  ++cnt;
      }
      res = max(res,cnt);
    }
    sort(R, R+N);
  }


  fprintf(stderr, "Case #%d: %d\n", P, res);
  printf("Case #%d: %d\n", P, res);
}

int main() {
  int n;
  scanf("%d", &n);
  init();
  for (int i = 1; i <= n; ++i) solve(i);
  return 0;
}
