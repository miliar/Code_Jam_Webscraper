#include <stdio.h>
#define MAX 10000
using namespace std;

int groups[MAX];
int prox[MAX];
long long int sum[MAX];

int main(void)
{
  int T, r, n, k;
  long long int res;

  scanf("%d", &T);
  for (int test = 1; test <= T; test++)
  {
    scanf("%d %d %d", &r, &k, &n);
    for (int i = 0; i < n; i++)
      scanf("%d", &(groups[i]));
    
    long long int tot = 0;
    for (int i = 0; i< n; i++)
      tot += groups[i];
    
    if (tot <= k)
      res = tot * r;
    else
    {
      int i, j;
      for (i = 0; i < n; i++)
      {
	tot = 0;
	for (j = i;; j = (j + 1) % n)
	{  
	  tot += groups[j];
	  if (tot > k)
	    break;
	}  
	  
	prox[i] = j;
	sum[i]  = tot - groups[j];
      }

      int next = 0;
      res = 0;
      for (i = 0; i < r; i++)
      {
	res += sum[next];
	next = prox[next];
      }
    }  

    printf("Case #%d: %lld\n", test, res);

  }  

}
