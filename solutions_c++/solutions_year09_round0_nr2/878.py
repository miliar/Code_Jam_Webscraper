#include <cstdio>
#include <cstring>
#include <vector>
#include <cassert>

using namespace std;

#define maxn 10010
vector <int> ney[maxn], nex[maxn];
#define maxd 110
int a[maxd][maxd], b[maxd][maxd];
int dy[] = {-1, 0, 0, 1}, dx[] = {0, -1, 1, 0};

int main( void )
{
  int tn;
  scanf("%d", &tn);

  for (int tt = 1; tt <= tn; tt++)
  {
    printf("Case #%d:\n", tt);

    int h, w;
    scanf("%d%d", &h, &w);

    memset(a, 63, sizeof(a));
    for (int i = 0; i < maxn; i++)
      ney[i].clear(), nex[i].clear();
    for (int i = 1; i <= h; i++)
      for (int j = 1; j <= w; j++)
      {
        scanf("%d", &a[i][j]);
        ney[a[i][j]].push_back(i);
        nex[a[i][j]].push_back(j);
      }
    int curr = 0;
    for (int h = 0; h < maxn; h++)
      for (int i = 0; i < (int)nex[h].size(); i++)
      {
        b[ney[h][i]][nex[h][i]] = curr;
        int best = maxn;
        for (int t = 3; t >= 0; t--)
          if (a[ney[h][i] + dy[t]][nex[h][i] + dx[t]] < a[ney[h][i]][nex[h][i]] && best >= a[ney[h][i] + dy[t]][nex[h][i] + dx[t]])
            b[ney[h][i]][nex[h][i]] = b[ney[h][i] + dy[t]][nex[h][i] + dx[t]], best = a[ney[h][i] + dy[t]][nex[h][i] + dx[t]];
        if (b[ney[h][i]][nex[h][i]] == curr) 
          curr++;
      }
    curr = 0;
    int was[26];
    memset(was, 0, sizeof(was));
    for (int i = 1; i <= h; i++)
      for (int j = 1; j <= w; j++)
      {
        if (!was[b[i][j]])
          was[b[i][j]] = ++curr;
        printf("%c%c", (char)was[b[i][j]] - 1 + 'a', " \n"[j == w]);
      }
    assert(curr <= 26);
  }

  return 0;
}