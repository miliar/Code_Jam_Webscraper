#include <cstring>
#include <cstdio>
using namespace std;

int T, N, d, ret;
int sum, min;

int main ()
{
  freopen ("C-large.in", "r", stdin);
  freopen ("ou.txt", "w", stdout);
  
    scanf ("%d", &T);
    
    int i;
    for (i = 1; i <= T; i++) {
      scanf ("%d", &N);
      
      ret = sum = 0;
      min = 10000000;
      for (int i = 0; i < N; i++) {
        scanf ("%d", &d);
        
        ret ^= d;
        sum += d;
        if (d < min) min = d; 
      } 
      
      printf ("Case #%d: ", i);
      if (ret == 0) {
          printf ("%d\n", sum - min);
      } else {
          printf ("NO\n");
      }
    }
    return 0;
}
