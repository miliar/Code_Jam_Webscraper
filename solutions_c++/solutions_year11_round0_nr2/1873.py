#include <stdio.h>
#include <string.h>

char comb[200][200];
bool oppo[200][200];
char ans[1000];
char s[1000];
int tc, n;

int main()
{
  scanf("%d", &tc);
  for (int tt = 1; tt <= tc; tt++)
  {
    memset(comb, 0, sizeof(comb));
    memset(oppo, 0, sizeof(oppo));
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
      scanf("%s", s);
      comb[s[0]][s[1]] = s[2];
      comb[s[1]][s[0]] = s[2];
    }
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
      scanf("%s", s);
      oppo[s[0]][s[1]] = true;
      oppo[s[1]][s[0]] = true;
    }
    scanf("%d", &n);
    scanf("%s", s);
    int len = 0;
    for (int i = 0; i < n; i++)
    {
      char ch = s[i];
      if (comb[ch][ans[len - 1]])
      {
        ans[len - 1] = comb[ch][ans[len - 1]];
      }
      else
      {
        bool op = false;
        for (int j = 0; j < len; j++)
        {
          if (oppo[ans[j]][ch])
          {
            len = 0;
            op = true;
            break;
          }
        }
        if (!op)
        {
          ans[len++] = ch;
        }
      }
    }
    printf ("Case #%d: [", tt);
    for (int i = 0; i < len; i++)
    {
      if (i == 0)
        printf("%c", ans[i]);
      else
        printf(", %c", ans[i]);
    }
    printf ("]\n");
  }
  return 0;
}
