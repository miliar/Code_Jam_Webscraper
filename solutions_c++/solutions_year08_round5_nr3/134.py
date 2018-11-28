#include <cstdio>
#include <queue>
#include <vector>
using namespace std;

int n, m;

char tab[88][88];

int num[88][88];
int N;

vector<int> neigh[12345];
vector<int> left;
vector<int> match;
vector<int> dist;
vector<int> color;
int farba;

void add(int i1, int j1, int i2, int j2)
{
  if (i2 < 0 || i2 >= n || j2 < 0 || j2 >= m) return;
  if (tab[i2][j2] == 'x') return;
  neigh[num[i1][j1]].push_back(num[i2][j2]);
}


bool dfs(int x)
{
  color[x] = farba;
  for (vector<int>::iterator it = neigh[x].begin(); it != neigh[x].end(); it++) {
    int y = match[*it];
    if (y < 0 || (dist[y] == dist[x] + 1 && color[y] != farba && dfs(y))) {
      match[x] = *it;
      match[*it] = x;
      return true;
    }
  }
  return false;
}
   
int matching()
{
  match.clear();
  match.resize(N, -42);
  
  dist.resize(N);
  
  color.resize(N);

  int res = 0;
  while (true) {
    farba++;
    queue<int> Q;
    for (int x = 0; x < left.size(); x++) {
      int i = left[x];
      if (match[i] < 0) {
        dist[i] = 0;
        Q.push(i);
      } else {
        dist[i] = -42;
      }
    }
    while (!Q.empty()) {
      int x = Q.front();
      Q.pop();
      for (vector<int>::iterator it = neigh[x].begin(); it != neigh[x].end(); it++) {
        int y = match[*it];
        if (y >= 0 && dist[y] < 0) {
          dist[y] = dist[x] + 1;
          Q.push(y);
        }
      }
    }
    bool done = true;
    for (int x = 0; x < left.size(); x++) {
      int i = left[x];
      if (match[i] < 0 && dfs(i)) {
        done = false;
        res++;
      }
    }
    if (done) break;
  }
  return res;
}

int main()
{
  int cases;
  scanf("%d", &cases);
  for (int case_ = 1; case_ <= cases; case_++) {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) {
      scanf(" %s", tab[i]);
    }
    N = 0;
    left.clear();
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (tab[i][j] == 'x') continue;
        if (j % 2 == 0) left.push_back(N);
        neigh[N].clear();
        num[i][j] = N;
        N++;
      }
    }
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (tab[i][j] == 'x') continue;
        for (int di = -1; di <= 1; di++) {
          for (int dj = -1; dj <= 1; dj++) {
            if (dj == 0) continue;
            add(i, j, i+di, j+dj);
          }
        }
      }
    }
    printf("Case #%d: %d\n", case_, N - matching());
  }
  return 0;
}
