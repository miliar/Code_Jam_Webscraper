#include <cstdio>
#include <cstdlib>

using namespace std;

int v[1010];
int n;

int main(){
  int t;

  scanf("%d", &t);
  for (int ka = 1; ka <= t; ka++){
    int x = 0;
    int min = 1010100;
    long long sum = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
      scanf("%d", &v[i]);
      x ^= v[i];
      sum += v[i];
      if (v[i] < min)
	min = v[i];
    }

    printf("Case #%d: ", ka);
    if (x != 0)
      printf("NO\n");
    else
      printf("%lld\n", sum-min);
  }

  return 0;
}
