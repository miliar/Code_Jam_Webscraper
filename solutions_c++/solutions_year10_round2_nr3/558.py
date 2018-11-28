#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> pii;

#define FOR(i, a, b) for(int (i) = (a); (i) < (b); ++(i))
#define REP(i, n) FOR((i), 0, (n))
#define SORT(x) sort((x).begin(), (x).end())
#define PB push_back
#define MP make_pair

int T;

int solve(int n) {
  int ans = 0;
  vi S;
  S.reserve(n);

  REP(i, 1 << (n-2)) {
    S.clear();
    int t = i;
    int c = 2;
    while (t > 0) {
      if ((t&1) == 1) S.PB(c);
      t >>= 1;
      ++c;
    }
    S.PB(n);
    
    c = n;
    while (c != 1) {
      if (!binary_search(S.begin(), S.end(), c))
        break;
      c = int(lower_bound(S.begin(), S.end(), c)-S.begin()) + 1;
    }
    if (c == 1)
      ++ans;
  }

  return ans;
}

int table[28];
int main() {
  scanf("%d", &T);

  FOR(i, 2, 26) {
    table[i] =  solve(i)%100003;
    fprintf(stderr, "end %d: %d\n", i, table[i]);
  }

  FOR(i, 1, T+1) {
    int n;
    scanf("%d", &n);
    printf("Case #%d: %d\n", i, table[n]);
  }

  return 0;
}
