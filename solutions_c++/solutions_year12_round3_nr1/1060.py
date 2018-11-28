#include "assert.h"
#include "stdio.h"
#include "stdlib.h"
#define SIZE 1024
#define DEBUG 0
static int dfs(int N, int graph[SIZE][SIZE], int color[SIZE], int u)
{
   int r = 0;
   for (int v = 0; v<N && r==0; v++) {
      if (v == u) continue;
      else if (graph[u][v] == 0) continue;
      else if (color[v] != 0) r = 1;
      else { color[v] = 1; r = dfs(N, graph, color, v); }
      //if (DEBUG) printf("#%d ", v+1);
   }
   return r;
}
int main()
{
   //if (DEBUG) freopen("diamond.sin", "r", stdin);
   int T; int N; int graph[SIZE][SIZE]; int color[SIZE]; int edges[SIZE]; int q;
   scanf("%d", &T); assert(T>0);
   for (int hulk = 0; hulk < T; hulk++) {
      scanf("%d", &N); assert(N>0); q = 0;
      for (int jack = 0; jack < N; jack++) for (int jill = 0; jill < N; jill++) graph[jack][jill] = 0;
      for (int jack = 0; jack < N; jack++) {
         scanf("%d", &edges[jack]); assert(edges[jack] >= 0);
         for (int jill = 0; jill < edges[jack]; jill++) {
            int sodium; scanf("%d", &sodium); sodium--;
            graph[jack][sodium] = 1;
         }
      }
      //if (DEBUG) for (int jack = 0; jack < N; jack++, printf("\n")) { printf("Vertex=%d inherits from ", jack+1); for (int jill=0; jill < N; jill++) if (graph[jack][jill]==1) printf("#%d ", jill+1); }
      for (int u = 0; u < N && q == 0; u++) {
         if (edges[u] == 0) continue;
         for (int jack = 0; jack < N; jack++) color[jack] = 0;
         //if (DEBUG) printf("DFS from vertex=%d. Hit=", u+1);
         q = dfs(N, graph, color, u);
         //if (DEBUG) printf("\n");
      }
      if (q==0) printf("Case #%d: No\n", hulk+1);
      else printf("Case #%d: Yes\n", hulk+1);
   }
   //if (DEBUG) fclose(stdin);
   return 0;
}
