#include <cstring>
#include <cstdio>
using namespace std;

int T, N, d, ret;
int sum, min;

int main ()
{
  freopen ("D-large.in", "r", stdin);
  freopen ("ou.txt", "w", stdout);
  
    scanf ("%d", &T);
    
    int i;
    for (i = 1; i <= T; i++) {
      scanf ("%d", &N);
      
      sum = N;
      min = 10000000;
      for (int i = 1; i <= N; i++) {
        scanf ("%d", &d);
        
        sum -= (d == i);
      } 
      
      printf ("Case #%d: %d.000000\n", i, sum);
    }
    return 0;
}
