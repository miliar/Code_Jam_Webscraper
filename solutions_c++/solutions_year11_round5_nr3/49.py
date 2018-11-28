#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

set <int> prev[10005];
int deg[10005];
set <int> ne[10005];
int m, n;

char s[105][105];

int num(int x, int y) {
  x = (x + m) % m;
  y = (y + n) % n;
  return x * n + y;
}

void add(int x1, int y1, int x2, int y2) {
  int a = num(x1, y1);
  int b = num(x2, y2);
  ne[a].insert(b);
  prev[b].insert(a);
  deg[b]++;
}

int tn, nt;

int dx[8]={-1,0,-1,1,1,0,1,-1};
int dy[8]={-1,-1,0,-1,1,1,0,1};
const char *t = "\\-|/";

int mark[10005][2];

void dfs(int v, int d) {
  mark[v][d] = 1;
  if (d == 0) {
    for (set <int>::iterator p = ne[v].begin(); p != ne[v].end(); p++)
       if (!mark[*p][1-d])
         dfs(*p, 1-d);
  } else {
    for (set <int>::iterator p = prev[v].begin(); p != prev[v].end(); p++)
       if (!mark[*p][1-d])
         dfs(*p, 1-d);
  }
}

int main(void)
{
//  freopen("C-small-attempt1.in", "r", stdin);
//  freopen("C-small-attempt1.out", "w", stdout);
  freopen("C-large.in", "r", stdin);
  freopen("C-large.out", "w", stdout);

  scanf("%d", &nt);
  for (tn=0; tn<nt; tn++)
  {
    fprintf(stderr, "Case #%d: \n", tn+1);

    printf("Case #%d: ", tn+1);

    scanf("%d%d", &m, &n);
    for (int i=0; i<m*n; i++) {
      prev[i].clear();
      ne[i].clear();
    }
    memset(deg, 0, sizeof(deg));

    for (int i=0; i<m; i++) {
      scanf("%s", s[i]);

      for (int j=0; j<n; j++) {
        int p = strchr(t, s[i][j]) - t;
        add(i, j, i+dx[p], j+dy[p]);
        add(i, j, i-dx[p], j-dy[p]);
      }
    }

    set <pair <int, int> > s;
    for (int i=0; i<m*n; i++) {
      s.insert(make_pair(deg[i], i));
    }

    int ans = 1;
    while (s.size() && s.begin()->first < 2) {
      set <pair <int, int> >::iterator p = s.begin();
      s.erase(p);
      if (p->first == 0) {
        ans = 0;
        break;
      }

      int i = p->second;
      int j = *prev[i].begin();

      deg[i]--;
      prev[i].erase(j);
      ne[j].erase(i);

      if (ne[j].size()) {
        i = *ne[j].begin();

        s.erase(make_pair(deg[i], i));
        deg[i]--;
        prev[i].erase(j);
        ne[j].erase(i);
        s.insert(make_pair(deg[i], i));
      }
    }

/*    for (int i=0; i<m*n; i++) {
      printf ("%d -> ", i);
      for (set <int>::iterator p = ne[i].begin(); p != ne[i].end(); p++)
        printf ("%d ", *p);
      puts("");
    }

    for (int i=0; i<m*n; i++) {
      printf ("%d <- ", i);
      for (set <int>::iterator p = prev[i].begin(); p != prev[i].end(); p++)
        printf ("%d ", *p);
      puts("");
    }*/

    if (ans) {
      memset(mark, 0, sizeof(mark));
      for (int i=0; i<m*n; i++) {
        if (!mark[i][0] && ne[i].size()) {
          dfs(i, 0);
          ans = (ans * 2) % 1000003;
        }
        if (!mark[i][1] && prev[i].size()) {
          dfs(i, 1);
          ans = (ans * 2) % 1000003;
        }
      }
    }

    printf ("%d\n", ans);
  }
  return 0;
}

