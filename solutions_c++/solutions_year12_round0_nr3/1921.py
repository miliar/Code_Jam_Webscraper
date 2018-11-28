#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cassert>
#include <map>
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#define FOR(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

typedef vector<int> VI;

int main() {

  int T;
  scanf("%d", &T);

  REP(tc, T) {

    int A, B;
    scanf("%d%d", &A, &B);
    
    int d = 1;
    for(; d <= A; d *= 10);

    // map<pair<int, int>, int> m;

    int res = 0;
    int memo[10], p = 0;
    for(int i = A; i <= B; i++) {
      for(int j = 10; j < d; j *= 10) {
        int x = i % j * (d / j) + i / j;        
        if(i < x && x <= B) {
          bool f = true;
          REP(k, 10) if(memo[k] == x) f = false;
          if(f) {
            res++;
            // m[pair<int, int>(i, x)]++;
            memo[p++] = x;
          }
        }
      }
      memset(memo, 0, sizeof(memo));
      p = 0;
    }

    printf("Case #%d: %d\n", tc + 1, res);
    // FOR(e, m) {
    //  if(e->second > 1) printf("(%d, %d)\n", e->first.first, e->first.second);
    // }
  }

  return 0;
}
