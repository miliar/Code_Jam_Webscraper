#include <algorithm>
#include <cstdio>
using namespace std;

static const int MAX_T = 100, MAX_N = 100;
int R[MAX_N], P[MAX_N];

int abs(int a) { return a >= 0 ? a : -a; }

int solve(int N) {
  int cnt = 0;
  int cur[2] = {1, 1}, can[2] = {0, 0};
  for (int j = 0; j < N; ++j) {
    int step = max(abs(P[j] - cur[R[j]]) - can[R[j]] + 1, 1);
    cnt += step;
    can[!R[j]] += step;
    cur[R[j]] = P[j];
    can[R[j]] = 0;
  }
  return cnt;
}

void output(int i, int n) {
  printf("Case #%d: %d\n", i+1, n);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; ++i) {
    int N;
    scanf("%d ", &N);
    for (int j = 0; j < N; ++j) {
      char c;
      scanf("%c", &c);
      R[j] = c == 'B';
      scanf("%d ", P + j);
    }
    output(i, solve(N));
  }
}
