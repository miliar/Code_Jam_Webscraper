#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <list>

#define FOR(i, m, n) for (int i=m; i<n; i++)

using namespace std;

int N, L, H;
int note[20000];

void solve() {
  scanf("%d%d%d", &N, &L, &H);
  FOR (i, 0, N)
    scanf("%d", &note[i]);
  bool b = false;
  FOR (i, L, H+1) {
    b = true;
    FOR (j, 0, N)
      if (i%note[j]!=0 && note[j]%i!=0) {
        b = false; break;
      }
    if (b) {
      printf("%d\n", i);
      break;
    }
  }
  if (!b)
    printf("NO\n");
}

int main() {
  int T; scanf("%d", &T);
  FOR (qq, 0, T) {
    printf("Case #%d: ", qq+1);
    solve();
  }
  return 0;
}
