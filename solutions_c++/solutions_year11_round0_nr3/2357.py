#include <cstdio>

int main() {
  int T, N, aux;
  scanf("%d",&T);
  for (int i = 1 ; i <= T ; i++) {
    int maior = 1000001;
    int x_v = 0;
    scanf("%d",&N);
    int tot_sum = 0;
    for (int j = 0 ; j < N ; j++) {
      scanf("%d",&aux);
      x_v ^= aux;
      tot_sum += aux;
      if (aux < maior)
	maior = aux;
    }
    printf("Case #%d: ",i);
    if (x_v == 0)
      printf("%d\n",tot_sum - maior);
    else
      printf("NO\n");
  }
  return 0;
}
