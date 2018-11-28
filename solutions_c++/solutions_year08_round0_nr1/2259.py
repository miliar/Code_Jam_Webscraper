#include <map>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

int n, q, s;
map<string, int> nm;
char b[10000];

int main()
{
  scanf("%d\n", &n);
  for (int ii = 0; ii < n; ii++)
  {
    nm.clear();
    scanf("%d\n", &s);
    for (int i = 0; i < s; i++)
    {
      fgets(b, 10000, stdin);
      string bb(b);
      nm[bb] = i;
    }
    scanf("%d\n", &q);
    int res = 0, ile = 0, nr = 109;
    bool odw[110];
    memset(odw, false, sizeof(odw));
    for (int i = 0; i < q; i++)
    {
      fgets(b, 10000, stdin);
      string bb(b);
      int nr = nm[bb];
      if (!odw[nr])
      {
        odw[nr] = true;
        ile++;
        if (ile == s)
        {
          memset(odw, false, sizeof(odw));
          odw[nr] = true;
          res++;
          ile = 1;
        }
      }
    }
    printf("Case #%d: %d\n", ii+1, res);
  }
  return 0;
}
