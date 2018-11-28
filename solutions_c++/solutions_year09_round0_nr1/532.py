#include <cstdio>
#include <cstring>

#define maxd 5010
#define maxl 20

int l, d, n;
char s[maxd][maxl];
char temp[maxl * 100];
bool can[maxl][26];

int main()
{
  scanf("%d%d%d", &l, &d, &n);
  for (int i = 0; i < d; i++)
    scanf("%s", s[i]);
  for (int i = 0; i < n; i++)
  {
    scanf("%s", temp);
    memset(can, 0, sizeof(can));
    for (int j = 0, k = 0; temp[j]; j++)
      if (temp[j] == '(')
      {
        for (j++; temp[j] && temp[j] != ')'; j++)
          can[k][temp[j] - 'a'] = true;
        k++;
      }
      else
        can[k++][temp[j] - 'a'] = true;
     int ans = 0;
     for (int j = 0; j < d; j++)
     {
       bool good = true;
       for (int k = 0; k < l; k++)
         if (!can[k][s[j][k] - 'a'])
           good = false, k = l;
       ans += good;
     }
     printf("Case #%d: %d\n", i + 1, ans);
  }
  return 0;
}

