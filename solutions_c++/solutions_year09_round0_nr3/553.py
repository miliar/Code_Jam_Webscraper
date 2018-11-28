#include <cstdio>
#include <cstring>

const int maxl = 510;

int testN;
char s[maxl], t[maxl] = "welcome to code jam";
int d[maxl][maxl];

int main()
{
  scanf("%d", &testN);
  gets(s);
  for (int test = 1; test <= testN; test++)
  {
    gets(s);
    int n = strlen(s), m = strlen(t);
    memset(d, 0, sizeof(d));
    d[0][0] = 1;
    for (int i = 0; i < n; i++)
      for (int j = 0; j <= m; j++)
      {
        d[i + 1][j] = (d[i + 1][j] + d[i][j]) % 10000;
        if (s[i] == t[j])
          d[i + 1][j + 1] = (d[i + 1][j + 1] + d[i][j]) % 10000;
      }
    int ans = d[n][m];
    printf("Case #%d: %04d\n", test, ans);
  }
  return 0;
}

