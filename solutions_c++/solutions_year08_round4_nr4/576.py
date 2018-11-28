#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <stdlib.h>

#define min(a,b) ((a)<(b)?(a):(b))

using namespace std;

int main()
{ 
  int N,i,j,k;
  int perm[5];
  char str[1001];
  char strtmp[1001];

  scanf("%d", &N);

  for (int cs=1; cs<=N; cs++)
  {
    scanf("%d", &k);
    scanf("%s", str);

    for (i=0;i<k;i++)
      perm[i] = i;
    
    int n = strlen(str);
    int m = -1;
    do
    {
      for (i=0;i<n/k;i++)
        for (j=0;j<k;j++)
          strtmp[i*k+j] = str[i*k + perm[j]];

      strtmp[n] = 0;

      //printf("Perm: %s\n", strtmp);

      char b=0;
      int a=0;
      for (i=0;i<n;i++)
      {
        if (strtmp[i] != b)
        {
          b = strtmp[i];
          a++;
        }
      }

      //printf("Found: %d\n", a);
      m = min(m,a);
      if (m == -1) m = a;

    } while (next_permutation(perm, perm+k));

    printf("Case #%d: %d\n", cs, m);
  }

  return 0;
}
