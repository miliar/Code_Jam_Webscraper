#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int gc[111][111], go[111][111];

int main (void)
{
  int test, tests, i, j, k, n;
  int C, D;
  int cnt[111]; int p[111];
  char c1, c2, c3;
  string li, res;
   
  freopen ("b.in", "rt", stdin);
  freopen ("b.out", "wt", stdout);
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    memset (cnt, 0, sizeof(cnt));
    memset (gc, -1, sizeof(gc));
    memset (go, -1, sizeof(go));
    res = "";
    scanf ("%d", &C);
    for (i = 0; i < C; i++)
    {
      scanf (" %c%c%c", &c1, &c2, &c3);
      gc [c1 - 'A'][c2-'A'] = c3;
      gc [c2 - 'A'][c1-'A'] = c3;
    }
    scanf ("%d", &D);
    for (i = 0; i < D; i++)
    {
      scanf (" %c%c", &c1, &c2);
      go [c1 - 'A'][c2-'A'] = 1;
      go [c2 - 'A'][c1-'A'] = 1;
    }
    scanf ("%d", &n);
    cin >> li;
    for (i = 0; i < n; i++)
    {
      cnt[li[i] - 'A']++;
      p[i] = 1;

      for (k = i - 1; k >= 0; k--)
      {
        if (p[k] == 1)            
        {
          if ((gc[li[i] - 'A'][li[k]- 'A'] != -1))
          {
            p[k] = 0;
            cnt[li[i] - 'A']--;
            cnt[li[k] - 'A']--;
            li[i] = gc[li[i] - 'A'][li[k]- 'A'];
            cnt[li[i] - 'A']++;
          }
          else
            break;
        }
      }
      for (k = i - 1; k >= 0; k--)
        if (p[k] == 1 && go[li[i] - 'A'][li[k] - 'A'] != -1)
        {
          for (j = 0; j <= i; j++)
            p[j] = 0, cnt[li[j] - 'A'] = 0;

          break;
        }  

        
    }
    k = -1;
    for (i = 0 ; i < n; i++)
      if (p[i] == 1)
      {
        k = i;
        break;
      }
    if (k >= 0)
    {
      res += li[k];
      for (i = k + 1; i < n; i++)
        if (p[i] == 1)
          res = res + ", " + li[i];
    }

    cout << "Case #" << test + 1 <<": ["<< res <<"]\n";
  }
  return 0;
}
