#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int T, N;

int main() {
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d", &N);
    vector<int> elems(N);
    for (int i = 0; i < N; ++i) {
      scanf("%d", &elems[i]);
    }

    vector<int> sorted_elems(elems);
    sort(sorted_elems.begin(), sorted_elems.end());

    double ans = 0.0;
    for (int i = 0; i < N; ++i) {
      if (elems[i] != sorted_elems[i]) ++ans;
    }
    
    printf("Case #%d: %lf\n", t, ans);
  }
}
