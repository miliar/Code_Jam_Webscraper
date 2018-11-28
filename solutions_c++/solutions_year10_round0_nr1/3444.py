#include <stdio.h>

int min_snaps[30];

int min_all_on(int k)
{
  if (k==0) return 0;
  if (k==1) return 1;
  return (min_all_on(k-1) * 2) + 1;
}

int is_on(int n, int k)
{
  if (min_snaps[n]==0) min_snaps[n]=min_all_on(n);
  if (k%(min_snaps[n]+1)==min_snaps[n]) return 1;
  else return 0;
}

int main()
{
  int t, n, k;
  scanf("%d", &t);
  for (int i=0; i<t; i++)
  {
  scanf("%d %d", &n, &k);
  if (is_on(n, k)==1)
    printf("Case #%d: ON\n", i+1);
  else
    printf("Case #%d: OFF\n", i+1);
  }
}
