#include <stdio.h>
#include <stdlib.h>

int n, a[2000];

void work()
{
     int s = 0, min = a[0];
     for (int i = 0; i < n; ++i){
         if (min > a[i]) min = a[i];
         s+=a[i];
     }
     printf("%d\n", s-min);
}
     
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cases, t = 0;
    int s;
    
    scanf("%d", &cases);
    while (cases--){
          ++t;
          printf("Case #%d: ", t);
          scanf("%d", &n);
          s = 0;
          for (int i = 0; i < n; ++i){
              scanf("%d", &a[i]);
              s ^= a[i];    
          }
          if (s==0)
             work();
          else
             printf("NO\n");
    }
    return 0;
}
