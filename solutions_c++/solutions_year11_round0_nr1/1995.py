#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int n;
int e[128];
int ans;

int gett() {
  int c = getchar();
  while (c != 'O' && c != 'B') c = getchar();
  return c;
}

void proc() {
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    int c = gett(), x;
    scanf("%d", &x);
    if (c == 'B') x = -x;
    e[i] = x;
  }

  int ans[2] = {0, 0};
  int pos[2] = {1, 1};
  for (int i = 0; i < n; ++i) {
    int np = abs(e[i]);
    int t = e[i] > 0;
    int nt = 1 - t;
    ans[t] += abs(np - pos[t]) + 1;
    pos[t] = np;
    if (ans[t] <= ans[nt]) ans[t] = ans[nt] + 1;
  }
  ::ans = max(ans[0], ans[1]);
}

int main() {
  // freopen("input.txt", "r", stdin);
  int T;
  scanf("%d", &T);
  while (T --) {
    proc();
    static int id = 0;
    printf("Case #%d: %d\n", ++id, ans);
  }
  return 0;
}
