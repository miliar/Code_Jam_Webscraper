#include <cstdio>
#include <cstdlib>

using namespace std;

int main(){
  int t, r, k, n, g[1010];
  int sz[1010], next[1010];

  scanf("%d", &t);
  for (int c = 1; c <= t; c++){
    long long lucro = 0;
    int inicio = 0;
    scanf("%d %d %d", &r, &k, &n);
    for (int i = 0; i < n; i++){
      scanf("%d", &g[i]);
    }

    for (int i = 0, j = 0, dentro = 0; i < n; i++){
      while (dentro + g[j] <= k){
	dentro += g[j];
	j++;
	if (j == n) j = 0;
	if (j == i) break;
      }
      sz[i] = dentro;
      next[i] = j;
      dentro -= g[i];
    }

    
    for (int i = 0; i < r; i++){
      lucro += sz[inicio];
      inicio = next[inicio];
    }

    printf("Case #%d: %lld\n", c, lucro);
  }
  return 0;
}
