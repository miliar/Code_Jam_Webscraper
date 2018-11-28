#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

class Frac
{
public:
  int a, b;
  Frac(int a_, int b_) : a(a_), b(b_) {}
  Frac() : a(0), b(1) {}

  bool operator == (const Frac& o) const {
    return (a*o.b == b*o.a);
  }

  bool operator < (const Frac& o) const {
    return (a*o.b < b*o.a);
  }
};

const int MAXN = 1000;

int N, L[MAXN], P[MAXN];
pair<Frac, int> q[MAXN];

void solve()
{
  for (int i = 0; i < N; ++i)
    q[i] = make_pair(Frac(L[i], P[i]), i);

  sort(&q[0], &q[N]);

  for (int i = 0; i < N; ++i) printf("%d ", q[i].second);
  printf("\n");
}

int main()
{
  int T; scanf("%d", &T);

  for (int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);

    scanf("%d\n", &N);
    for (int i = 0; i < N; ++i) scanf("%d", &L[i]);
    for (int i = 0; i < N; ++i) scanf("%d", &P[i]);

    solve();
  }

  return 0;
}
