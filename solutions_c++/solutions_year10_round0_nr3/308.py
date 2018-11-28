#include <cstdio>
#include <cstring>
#include <cassert>
using namespace std;

long long g[1000];
int turn[1000];
long long money[1000];

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t) {
    memset(turn, -1, sizeof(turn));
    memset(money, -1, sizeof(money));
    int R, k, N;
    scanf("%d%d%d", &R, &k, &N);
    for (int i = 0; i < N; ++i) {
      scanf("%lld", g+i);
    }
    int head = 0;
    long long m = 0;
    for (int i = 0; i < R; ) {
      if (turn[head] != -1) {
        long long period = i - turn[head];
        long long mouke = m - money[head];
        long long times = (R - i) / period;
        assert(mouke * times >= 0);
        assert(period * times >= 0);
        m += mouke * times;
        i += period * times;
        memset(turn, -1, sizeof(turn));
        memset(money, -1, sizeof(money));
      } else {
        money[head] = m;
        turn[head] = i;
        long long n_ride = 0, j;
        for (j = head; ; j = (j + 1) % N) {
          if (j == head && n_ride > 0)
            break;
          if (n_ride + g[j] > k)
            break;
          n_ride += g[j];
        }
        m += n_ride;
        head = j;
        ++i;
      }
      assert(m >= 0);
    }
    printf("Case #%d: %lld\n", t+1, m);
  }
}
