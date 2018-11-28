#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;

int p, ans1, ans2;
int xx[2001], yy[2001];
int level[401], prev[401];
bool edge[401][401];
int marked[401];

void DFS(int n) {
  int count;

  if (n == 0) {
    count = 0;
    for (int i = 0; i < p; i++)
      if (marked[i] == 1)
        for (int j = 0; j < p; j++)
          if (edge[i][j] && marked[j] == 0) {
            marked[j] = 2;
            count++;
          }
    if (ans2 < count)
      ans2 = count;
    for (int i = 0; i < p; i++)
      if (marked[i] == 2)
        marked[i] = 0;
    return;
  }

  for (int i = 0; i < p; i++)
    if (edge[n][i] && level[i] + 1 == level[n]) {
      marked[i] = 1;
      DFS(i);
      marked[i] = 0;
    }
}

void BFS() {
  int node;
  queue<int> q;

  memset(marked, 0, sizeof marked);
  memset(level, 0xff, sizeof level);
  memset(prev, 0xff, sizeof prev);
  level[0] = 0;
  q.push(0);

  while (!q.empty()) {
    node = q.front();
    q.pop();

    for (int i = 0; i < p; i++)
      if (edge[node][i] && level[i] == -1) {
        prev[i] = node;
        level[i] = level[node] + 1;
        q.push(i);
      }
  }
  
  ans2 = 0;
  ans1 = level[1] - 1;
  DFS(1);
}

int main() {
  int case_no, w, x, y, t;

  scanf("%d", &t);
  for (case_no = 1; case_no <= t; case_no++) {
    scanf("%d%d", &p, &w);

    memset(edge, false, sizeof edge);

    for (int i = 0; i < w; i++) {
      scanf("%d", &xx[i]);
      getchar();
      scanf("%d", &yy[i]);
      edge[xx[i]][yy[i]] = edge[yy[i]][xx[i]] = true;
    }
    
    BFS();
/*
    BFS();
    ans1 = level[1] - 1;
    memset(marked, 0, sizeof marked);
    for (int v = 1; v; v = prev[v])
      marked[prev[v]] = 1;
    count = 0;
    for (int i = 0; i < p; i++)
      if (marked[i] == 1)
        for (int j = 0; j < p; j++)
          if (edge[i][j] && marked[j] == 0) {
            marked[j] = 2;
            count++;
          }
    ans2 = count;

    for (int i = 0; i < w; i++) {
      edge[xx[i]][yy[i]] = edge[yy[i]][xx[i]] = false;
      BFS();
      tmp = level[1] - 1;
      edge[xx[i]][yy[i]] = edge[yy[i]][xx[i]] = true;
      if (tmp == ans1) {
        memset(marked, 0, sizeof marked);
        for (int v = 1; v; v = prev[v])
          marked[prev[v]] = 1;
        count = 0;
        for (int i = 0; i < p; i++)
          if (marked[i] == 1)
            for (int j = 0; j < p; j++)
              if (edge[i][j] && marked[j] == 0) {
                marked[j] = 2;
                count++;
              }
        if (count > ans2)
          ans2 = count;
      }
    }
*/
    printf("Case #%d: %d %d\n", case_no, ans1, ans2);
  }

  return 0;
}
