#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

using namespace std;

int nextInt() { int tmp; scanf("%d", &tmp); return tmp; }

int main() {

  int T = nextInt();
  for (int t = 1; t <= T; ++t) {
    int N = nextInt();
    vector<int> L(N);
    for (int i = 0; i < N; ++i)
      L[i] = nextInt();
    vector<int> P(N);
    for (int i = 0; i < N; ++i)
      P[i] = nextInt();

    vector<pair<int,int> > v(N);
    for (int i = 0; i < N; ++i)
      v[i] = make_pair(-P[i], i);
    sort(v.begin(), v.end());

    printf("Case #%d:", t);
    for (int i = 0; i < N; ++i)
      printf(" %d", v[i].second);
    puts("");
  }

  return 0;

}
