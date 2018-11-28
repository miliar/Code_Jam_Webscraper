#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

vector< pair<int, int> > V;
int N;

int main() {
  freopen("intranet.in", "r", stdin);
  freopen("intranet.out", "w", stdout);

  int T;
  scanf("%d ", &T);

  for (int t = 1; t <= T; t++) {
    scanf("%d ", &N);

    V.clear();
    for (int i = 1; i <= N; i++) {
      int x, y;
      scanf("%d %d ", &x, &y);
      V.push_back(make_pair(x, y));
    }

    int cnt = 0;
    sort(V.begin(), V.end());
    for (int i = 0; i < N; i++) {
       for (int j = 0; j < i; j++) {
         if (V[j].second > V[i].second) {
           cnt++;
         }
       }
    }

    printf("Case #%d: %d\n", t, cnt);
  }

  return 0;
}
