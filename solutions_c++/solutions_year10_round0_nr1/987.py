#include <stdio.h>

int main()
{
  int t, n, k;
  scanf("%i", &t);
  
  for(int i = 0; i < t; i++) {
    scanf("%i%i", &n, &k);
    printf("Case #%i: %s\n", i + 1, (k % (1 << n)) == ((1 << n) - 1) ? "ON" : "OFF");
    //printf("%i %i %i %i %i\n", n, k, 1 << n, k % (1 << n), 1 << n - 1);
  }
}
