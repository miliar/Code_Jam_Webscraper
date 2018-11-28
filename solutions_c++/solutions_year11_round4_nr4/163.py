#include <cstdio>
#include <cstring>

#include <vector>
#include <queue>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

#define INF 0x3f3f3f3f

int N, W;
VVI adj;

int D[404];
VI P[404];
int bfs(int src, int dst) {
   memset(D, 0x3f, sizeof(D));
   D[src] = 0;
   for (int i = 0; i < N; ++i)
      P[i].clear();
   queue<int> q;
   q.push(src);
   int best_dist = INF;
   while (!q.empty()) {
      int cur = q.front();
      q.pop();
      int dist = D[cur];
   // fprintf(stderr, "cur = %d  %d\n", cur, dist);
      if (cur == dst) {
         best_dist = dist;
         continue;
      }
      if (dist > best_dist)
         continue;
      for (int j = 0; j < adj[cur].size(); ++j) {
         int nxt = adj[cur][j];
         if (D[nxt] > dist+1) {
            D[nxt] = dist + 1;
            q.push(nxt);
            P[nxt].clear();
            P[nxt].push_back(cur);
         }
         else if (D[nxt] == dist+1) {
            P[nxt].push_back(cur);
         }
      }
   }
   return best_dist;
}

int vis[404];
int res1, res2;
void dfs(int x, int cur = 0) {
//   fprintf(stderr, "x = %d  cur = %d\n", x, cur);

   int orig = vis[x];
   if (vis[x] > 0)
      cur--;
   vis[x] = -1;
   for (int j = 0; j < adj[x].size(); ++j) {
      int y = adj[x][j];
      if (vis[y] == 0 && y != 0) {
         vis[y] = x+1;
         ++cur;
//         fprintf(stderr, "%d ++ cur = %d\n", y, cur);
      }
   }

//   fprintf(stderr, "new cur = %d\n", cur);

   if (x == 0) {
      res2 = max(res2, cur);
   }
   else {
      for (int j = 0; j < P[x].size(); ++j) {
         int y = P[x][j];
         if (vis[y] >= 0) {
            dfs(y, cur);
         }
      }
   }

   for (int j = 0; j < adj[x].size(); ++j) {
      int y = adj[x][j];
      if (vis[y] == x+1 && y != 0) {
         vis[y] = 0;
      }
   }
   vis[x] = orig;
}

int main(int argc, char* argv[]) {
   int TC;
   scanf("%d", &TC);
   for (int tc = 1; tc <= TC; ++tc) {
      scanf("%d %d", &N, &W);
      adj = VVI(N);
      for (int j = 0; j < W; ++j) {
         int u, v;
         scanf("%d,%d", &u, &v);
      // fprintf(stderr, "(%d,%d)\n", u, v);
         adj[u].push_back(v);
         adj[v].push_back(u);
      }
      res1 = bfs(0, 1)-1;

      res2 = 1;
      for (int j = 0; j < P[1].size(); ++j) {
         memset(vis, 0, (N+1)*sizeof(int));
         int y = P[1][j];
         dfs(y);
      }

      printf("Case #%d: %d %d\n", tc, res1, res2);
   }
   return 0;
}
