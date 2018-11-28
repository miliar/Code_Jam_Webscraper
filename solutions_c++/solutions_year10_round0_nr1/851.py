#include <cstdio>

int main()
{
 freopen("input.txt", "r", stdin);
 freopen("output.txt", "w", stdout);

 int t;

 scanf("%d", &t);
 for (int i = 0; i < t; ++i)
 {
  int n, k;
  scanf("%d%d", &n, &k);

  printf("Case #%d: ", i + 1);
  if ((k + 1) % (1 << n))
   printf("OFF\n");
  else
   printf("ON\n");
 }

 return 0;
}