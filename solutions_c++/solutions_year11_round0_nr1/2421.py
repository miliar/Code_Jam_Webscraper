#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int n;
vector<int> b[2], k;
int p[2], pk, bp[2];
char cc;
int bb, res;

int sgn(int a)
{
  return (a == 0) ? 0 : ((a < 0) ? -1 : 1);
}

int main()
{
  int t;

  scanf("%d", &t);
  for (int j = 0; j < t; j++)
  {
    b[0].clear();
    b[1].clear();
    k.clear();
    scanf("%d", &n);
    for (int i = 0; i < n; i++) 
    {
      scanf(" %c %d", &cc, &bb);
      int poz = (cc == 'O' ? 0 : 1);
      b[poz].push_back(bb);
      k.push_back(poz);
    }
    p[0] = p[1] = pk = 0;
    res = 0;
    bp[0] = bp[1] = 1;
    for (pk = 0; pk < n; pk++)
    {
      while (bp[k[pk]] != b[k[pk]][p[k[pk]]])
      {
        bp[k[pk]] += sgn(b[k[pk]][p[k[pk]]] - bp[k[pk]]);
        if (p[1-k[pk]] < b[1-k[pk]].size() && bp[1-k[pk]] != b[1-k[pk]][p[1-k[pk]]])
          bp[1-k[pk]] += sgn(b[1-k[pk]][p[1-k[pk]]] - bp[1-k[pk]]);
        res++;
      }
      if (p[1-k[pk]] < b[1-k[pk]].size() && bp[1-k[pk]] != b[1-k[pk]][p[1-k[pk]]])
        bp[1-k[pk]] += sgn(b[1-k[pk]][p[1-k[pk]]] - bp[1-k[pk]]);
      res++;
      p[k[pk]]++;
    }
    printf("Case #%d: %d\n", j+1, res);
  }
  return 0;
}
