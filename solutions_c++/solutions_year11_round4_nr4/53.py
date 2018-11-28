#include <climits>
#include <cstdio>
#include <numeric>
#include <queue>
#include <vector>
using namespace std;

const int INF = INT_MAX/2;
const int MAXV = 400;
vector<int> adj[MAXV];

int V;
int dist[MAXV];
void bfs(int src) {
  for (int i=0; i<V; ++i) dist[i] = INF;
  queue<int> q; q.push(src); dist[src] = 0;
  while (!q.empty()) {
    int a = q.front(); q.pop();
    for (int i=0; i<(int)adj[a].size(); ++i) {
      int b = adj[a][i];
      if (dist[b] == INF) {
        dist[b] = dist[a]+1;
        q.push(b);
      }
    }
  }
}

int best;
vector<int> path;
void rek(int a) {
  if (dist[a] == 0) {
    static vector<char> threat;
    threat.clear();
    threat.resize(V);
    for (int i=0; i<(int)path.size(); ++i) {
      for (int j=0; j<(int)adj[path[i]].size(); ++j) {
        int b = adj[path[i]][j];
        threat[b] = 1;
      }
    }
    for (int i=0; i<(int)path.size(); ++i) {
      threat[path[i]] = 0;
    }
    best = max(best, accumulate(threat.begin(), threat.end(), 0));
    return;
  }
  path.push_back(a);
  for (int i=0; i<(int)adj[a].size(); ++i) {
    int b = adj[a][i];
    if (dist[b] == dist[a]-1) {
      rek(b);
    }
  }
  path.pop_back();
}

int main(void) {
  int CASES; scanf("%d", &CASES);
  for (int tt=1; tt<=CASES; ++tt) { // caret here
    int E;
    scanf("%d%d", &V, &E);
    for (int i=0; i<V; ++i) {
      adj[i].clear();
    }
    while (E--) {
      int a, b; scanf("%d,%d", &a, &b);
      adj[a].push_back(b);
      adj[b].push_back(a);
    }

    bfs(1);
    best = 0;
    rek(0);
    printf("Case #%d: %d %d\n", tt, dist[0]-1, best);
  }

  return 0;
}
