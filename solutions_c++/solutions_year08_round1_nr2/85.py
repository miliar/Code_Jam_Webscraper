#include <cstdio>

#include <vector>

using namespace std;

#define maxn 4000

vector <int> neS[maxn];
int badNe[maxn], p[maxn], q[maxn], l, r, res[maxn], m, n;

int main( void )
{
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int tn;

  scanf("%d", &tn);
  
  for (int t = 1; t <= tn; t++)
  {
    printf("Case  #%d:", t);

    scanf("%d%d", &n, &m);
    for (int i = 0; i < maxn; i++)
    {
      neS[i].clear();
      badNe[i] = -1;
      p[i] = 0;
      res[i] = 0;
    }
    for (int i = 0; i < m; i++)
    {
      int en;
      scanf("%d", &en);
      for (int j = 0; j < en; j++)
      {
        int x, y;
        scanf("%d%d", &x, &y);
        x--;

        if (y)
        {
          badNe[i] = x;
        }
        else
        {
          p[i]++;
          neS[x].push_back(i);
        }
      }

    }

    l = 0, r = 0;
    for (int i = 0; i < m; i++)
      if (!p[i])
      {
        q[r++] = i;
      }
    int ok = 1;
    while (l < r)
    {
      int curr = q[l++];
      if (badNe[curr] == -1)
      {
        ok = 0;
        break;
      }
      if (res[badNe[curr]] == 0)
      {
        int v = badNe[curr];
        res[v] = 1;
        for (int j = 0; j < neS[v].size(); j++)
        {
          p[neS[v][j]]--;
          if (p[neS[v][j]] == 0)
          {
            q[r++] = neS[v][j];
          }
        }
      }
    }
    if (ok)
    {
      for (int i = 0; i < n; i++)
        printf(" %d", res[i]);
      printf("\n");
    }
    else
    {
      printf(" IMPOSSIBLE\n");
    }
  }

  return 0;
}
