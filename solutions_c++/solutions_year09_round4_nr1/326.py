#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "set"
#include "string"
#include "vector"
using namespace std;
typedef long long i64;

int main() {
  int T; scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
    int n; scanf("%d", &n);
    vector<string> v(n);
    for (int i = 0; i < n; ++i) {
      char str[100]; scanf("%s", str);
      v[i] = string(str);
    }
    vector<int> sizes(n, 0);
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
        if (v[i][j] == '1') sizes[i] = j;
    int swaps = 0;
    for (int i = 0; i < n; ++i) if (sizes[i] > i) {
      int k = -1;
      for (int j = i + 1; j < n && k == -1; ++j)
        if (sizes[j] <= i) k = j;
      for (int j = k - 1; j >= i; --j)
        swap(sizes[j], sizes[j + 1]), ++swaps;
    }
    printf("Case #%d: %d\n", Ti, swaps);
  }
  return 0;
}
