#include <stdio.h>
#include <string.h>

int order[1000000];
int next[1000000];

int main()
{
  int T, cs, K, n;
  int i,j,k;

  scanf("%d", &T);

  for (cs=1; cs<=T; cs++)
  {
    memset(order, 0, sizeof(order));
    scanf("%d", &K);

    j=-1; k=0;
    for (i=1;i<=K; i++)
    {
      while(true)
      {
        j++;
        if (j>=K) j=0;
        
        if (!order[j])
        {
          k++;
          if (k == i)
          {
            order[j] = k;
            //printf("%d = %d\n", j, k);
            k = 0;
            break;
          }
        }
      }
    }

    scanf("%d", &n);
    printf("Case #%d:", cs);
    for (i=0;i<n;i++)
    {  
      scanf("%d", &j);
      j--;
      printf(" %d", order[j]);
    }

    printf("\n");
  }
  return 0;
}
