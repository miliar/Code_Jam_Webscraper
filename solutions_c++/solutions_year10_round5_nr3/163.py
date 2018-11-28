#include <algorithm>
#include <cstdio>
#include <set>
#include <cstring>

using namespace std;

typedef set<int> si;

const int kMaxN = 100000 + 10;
const int kMaxLen = 4000000 + 10;
const int kOffset = 2000000 + 5;

int C, P, V;
int N;

int maxcnt;
si rset[kMaxN];
int cnt[kMaxLen];

//void Modify(int idx, int count, int delta) {
//  rset[count].erase(count);
//}

int Solve() {
  int result = 0;
  while (maxcnt > 1) {
    si::iterator it = rset[maxcnt].begin();
    int idx = *it;
    rset[maxcnt].erase(it);
    rset[maxcnt - 2].insert(idx);
    cnt[idx + kOffset] = maxcnt - 2;
    
    int c = cnt[idx - 1 + kOffset];
    rset[c].erase(idx - 1);
    rset[c + 1].insert(idx - 1);
    cnt[idx - 1 + kOffset] = c + 1;
    maxcnt = max(maxcnt, c + 1);

    c = cnt[idx + 1 + kOffset];
    rset[c].erase(idx + 1);
    rset[c + 1].insert(idx + 1);
    cnt[idx + 1 + kOffset] = c + 1;
    maxcnt = max(maxcnt, c + 1);

    while (maxcnt > 1 && rset[maxcnt].empty()) --maxcnt;
    ++result;
  }
  return result;
}

int main() {
  int cases;
  scanf("%d", &cases);
  for (int e = 1; e <= cases; ++e) {
    printf("Case #%d: ", e);
    memset(cnt, 0, sizeof(cnt));
    scanf("%d", &C);
    maxcnt = 0;
    for (int i = 0; i < C; ++i) {
      scanf("%d %d", &P, &V);
      cnt[P + kOffset] = V;
      maxcnt = max(maxcnt, V);
    }
    rset[0].clear();
    rset[1].clear();
    for (int i = -1000000; i <= 1000000; ++i)
      rset[cnt[i + kOffset]].insert(i);
    printf("%d\n", Solve());
  }
  return 0;
}
