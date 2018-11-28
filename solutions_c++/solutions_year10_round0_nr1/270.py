#include <stdio.h>

int main() {

  int ncases;
  scanf("%d", &ncases);

  for(int ittr = 0; ittr < ncases; ++ittr) {
    long bits, k;
    scanf("%ld %ld", &bits, &k);
    long mask = (1<<bits)-1;
    printf("Case #%d: %s\n", 1+ittr, ((k&mask)==mask) ? "ON" : "OFF");
  }

  return(0);
}
