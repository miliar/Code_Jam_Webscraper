#include <cstdio>
#include <string>
#include <cstring>
#include <unordered_map>
#include <map>
#include <queue>
#include <vector>
#include <utility>
#include <algorithm>
#include <set>

using namespace std;

int N,D;
int d[10000];
int l[10000];

typedef pair<int, int> PII;

namespace std {
  template <> struct hash<PII>
  {
    size_t operator()(const PII & x) const
    {
      return x.second * 9973 + x.first;
    }
  };
}

unordered_map<PII, int> cache;

int calc(int liane, int potential) {
  //  fprintf(stderr, "swinging from %d with pot %d\n", liane, potential);
  PII p = make_pair(liane, potential);
  if (cache.find(p) != cache.end())
    return cache[p] == 1;
  
  if (D - d[liane] <= potential)
    return (cache[p] = 1);

  int i = liane - 1;
  cache[p] = 2;
  while (i >= 0 && d[liane] - d[i] <= potential) {
    if (calc(i, min(d[liane] - d[i], l[i])) == 1)
      return (cache[p] = 1);
    i--;
  }
  i = liane + 1;
  while (i < N && d[i] - d[liane] <= potential) {
    if (calc(i, min(d[i] - d[liane], l[i])) == 1)
      return (cache[p] = 1);
    i++;
  }
  return (cache[p] = 0);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int ttt=0; ttt<T; ttt++) {
    scanf("%d", &N);
    cache.clear();
    for (int i=0; i<N; i++) {
      scanf("%d %d", d+i, l+i);
    }
    scanf("%d", &D);

    printf("Case #%d: ", ttt+1);
    if (calc(0, d[0]))
      printf("YES\n");
    else
      printf("NO\n");
  }
  
}
