#include <cstdio>
#include <vector>

int main() {
  int t;
  scanf("%d", &t);
  for (int ti = 0; ti < t; ++ti) {
    int n;
    scanf("%d", &n);
    std::vector<int> v(n, 0);
    for (int i = 0; i < n; i++) {
      scanf("%d", &v[i]);
      --v[i];
    }
    std::vector<bool> u(n, false);
    double result = 0;
    for (int i = 0; i < n; i++) {
      if (u[v[i]]) {
	continue;
      }
      int j = i, s = 0;
      while (!u[v[j]]) {
        u[v[j]] = true;
        ++s;
        j = v[j];
      }
      
      result += (s > 1) ? s : 0;
    }
    
    printf("Case #%d: %.6lf\n", ti + 1, result);
  }

  return 0;
}
