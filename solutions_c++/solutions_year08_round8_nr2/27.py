#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <cassert>
#include <ctime>
#include <cstdlib>
#include <cmath>

#define eps 1e-9

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define sz(v)((v).size())

#define task_name "b"


using namespace std;

map <string, int> col;
int nn;

vector < pair <pair <int, int>, int > > v;

int dp[310][310][310];

int main( void )
{
  freopen(task_name ".in", "r", stdin);
  freopen(task_name ".out", "w", stdout);

  int tn;
  scanf("%d", &tn);



  for (int tt = 1; tt <= tn; tt++)
  {
    printf("Case #%d: ", tt);

    col.clear();
    v.clear();

    int n;
    scanf("%d", &n);

    col["none"] = 0;
    nn = 1;

    for (int i = 0; i < n; i++)
    {
      string s;
      int l, r;
      cin >> s >> l >> r;
      if (!col.count(s))
        col[s] = nn++;
      int num = col[s];
      v.push_back(make_pair(make_pair(l, r), num));
    }

    v.push_back(make_pair(make_pair(0, 0), 0));
    sort(v.begin(), v.end());
    memset(dp, 63, sizeof(dp));
    int inf = dp[0][0][0];
    dp[0][0][0] = 0;
    int res = inf;
    for (int i = 0; i < (int)v.size(); i++)
      for (int a = 0; a < nn; a++)
        for (int b = 0; b < nn; b++)
          if (dp[i][a][b] < inf)
          {
            if (v[i].first.second == 10000)
              res <?= dp[i][a][b];
            int c = v[i].second;
            for (int j = i + 1; j < (int)v.size(); j++)
              if (v[j].first.first - 1 <= v[i].first.second)
              {
                int add = v[j].second;
                int na = a, nb = b, nc = c;
                if (na == add)
                  swap(na, nc);
                else if (nb == add)
                  swap(nb, nc);
                else if (nc == add)
                {}
                else if (na == 0)
                  swap(na, nc);
                else if (nb == 0)
                  swap(nb, nc);
                else if (nc == 0)
                {}
                else
                  continue;
                dp[j][na][nb] <?= dp[i][a][b] + 1; 
              }
          }
     if (res == inf)
       printf("IMPOSSIBLE\n");
     else
       printf("%d\n", res);

  }

   
  
  return 0;
}