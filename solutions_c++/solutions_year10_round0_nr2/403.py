#include <cstdio>
#include <climits>

int gcd(int x, int y)
{
  while(y) {
    int t = x;
    x = y;
    y = t % y;
  }
  return x;
}

int main()
{
  int c, n, t[1010], min;
  scanf("%i", &c);
  
  for(int i = 0; i < c; i++) {
    scanf("%i", &n);
    //printf("n: %i\n", n);
    min = 0;
    for(int j = 0; j < n; j++) {
      scanf("%i", &t[j]);
      if(t[min] > t[j]) min = j;
    }
    int curgcd = min == 0 ? t[1] - t[0] : t[0] - t[min];
    for(int j = 0; j < n; j++) {
      //printf("curgcd: %i\n", curgcd);
      curgcd = gcd(curgcd, t[j] - t[min]);
    }
    //printf("curgcd: %i\nmin: %i\nt[min]: %i\n", curgcd, min, t[min]);
    printf("Case #%i: %i\n", i + 1, t[min] % curgcd == 0 ? 0 : curgcd - t[min] % curgcd);
  }
}
