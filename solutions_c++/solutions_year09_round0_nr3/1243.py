#include <stdio.h>
#include <cstring>

char s[]="welcome to code jam";
char t[1005];
int d[1005][20];

int main(void)
{
  freopen("c.in", "r", stdin);
  freopen("c.out", "w", stdout);

  int tn, nt, i, j;
  scanf("%d\n", &nt);
  for (tn=0; tn<nt; tn++)
  {
    memset(d, 0, sizeof(d));
    gets(t);
    d[0][0]=1;
    for (i=0; t[i]; i++)
      for (j=0; j<=19; j++)
      {
        d[i+1][j]=(d[i+1][j]+d[i][j])%10000;
        if (s[j]==t[i]) d[i+1][j+1]=(d[i+1][j+1]+d[i][j])%10000;
      }

    printf("Case #%d: %04d\n", tn+1, d[i][j-1]);
  }

  return 0;
}