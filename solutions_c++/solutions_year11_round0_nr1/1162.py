#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <deque>
using namespace std;

const int infinity = 1000000000;
int f[128][128][128];

struct State {
  int i, a, b;
  State(int ii, int aa, int bb) : i(ii), a(aa), b(bb) {}
};

const int maxn = 101;

int main() {
  int cases;
  scanf("%i", &cases);
  for (int numcase = 1; numcase <= cases; ++numcase) {
    printf("Case #%i: ", numcase);

    int n;
    scanf("%i", &n);
    int r[n]; int button[n];
    for (int i = 0; i < n; ++i) {
      char robot;
      scanf(" %c%i", &robot, &button[i]);
      --button[i];
      r[i] = (robot == 'B');
    }

    fill(&f[0][0][0], &f[n + 1][0][0], infinity);
    f[0][0][0] = 0;
    deque<State> q;
    q.push_back(State(0, 0, 0));

    while (!q.empty()) {
      State st = q.front(); q.pop_front();
      int i = st.i, a = st.a, b = st.b, moves = f[i][a][b];
      if (i == n) { printf("%i\n", moves); break; }

      for (int da = -1; da <= 1; ++da) if (a + da >= 0 && a + da < maxn)
        for (int db = -1; db <= 1; ++db) if (b + db >= 0 && b + db < maxn)
          for (int press = 0; press < 3; ++press) {
            int na = a + da, nb = b + db, ni = i;
            if (press == 1 && da == 0 && r[i] == 0 && button[i] == a || 
                press == 2 && db == 0 && r[i] == 1 && button[i] == b)
              ++ni;
            if (f[ni][na][nb] == infinity) {
              f[ni][na][nb] = moves + 1;
              State next(ni, na, nb);
              q.push_back(next);
            }
          }
    }
  }
  return 0;
}
