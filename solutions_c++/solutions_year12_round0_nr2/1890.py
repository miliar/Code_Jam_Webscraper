#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cassert>
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); i++)

typedef vector<int> VI;

int main() {

  int T;
  scanf("%d", &T);

  REP(tc, T) {
    int N, S, P;
    scanf("%d%d%d", &N, &S, &P);
    int res = 0;
    REP(i, N) {
      int x;
      scanf("%d", &x);
      x -= P;
      if(x < 0) continue;
      if(x / 2 >= P - 1) {
        res++;
      } else if(x / 2 >= P - 2 && S > 0) {
        res++;
        S--;
      }
    }
    printf("Case #%d: %d\n", tc + 1, res);
  }

  return 0;
}
