#include <stdio.h>

#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))

int main()
{
  int T, a1, a2, b1, b2;
  scanf("%i", &T);
  for(int t = 0; t < T; t++) {
    scanf("%i %i %i %i", &a1, &a2, &b1, &b2);
    //printf("(%i, %i, %i, %i)", a1, a2, b1, b2);
    int res = 0;
    for(int i = a1; i <= a2; i++)
      for(int j = b1; j <= b2; j++) {
        //printf("(i, j, res): (%i, %i, %i)\n", i, j, res);
        if(max(i, j) / min(i, j) >= 2) {
          res++;
          continue;
        } else {
          int w, x = max(i, j), y = min(i, j);
          for(w = 0; y && max(x, y) / min(x, y) < 2; w = 1 - w) {
            int temp = y;
            y = x % y;
            x = temp;
            //printf("(x, y): %i %i\n", x, y);
          }
          //printf("(w, y) = (%i, %i)\n", w, y);
          //if(!(w % 2) && !y) res++;
          //if(w % 2 && y) res++;
          if(!(w % 2)) res++;
        }
      }
    printf("Case #%i: %i\n", t + 1, res);
  }
  return 0;
}
