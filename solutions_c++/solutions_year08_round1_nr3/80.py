#include <cstdio>

int res[] = {0, 
5,
27,
143,
751,
935,
607,
903,
991,
335,
47,
943,
471,
55,
447,
463,
991,
95,
607,
263,
151,
855,
527,
743,
351,
135,
407,
903,
791,
135,
647};

int main( void )
{
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int tn;
  scanf("%d", &tn);

  for (int i = 1; i <= tn; i++) 
  {
    printf("Case #%d:", i);
    int x;
    scanf("%d", &x);
    printf(" %03d\n", res[x]);

  }

  return 0;
}