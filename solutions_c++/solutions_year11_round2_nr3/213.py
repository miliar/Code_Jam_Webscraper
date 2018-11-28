#include <algorithm>
#include <cassert>
#include <string>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cctype>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <list>
#include <functional>
#include <numeric>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>
#include <stdexcept>
using namespace std;

const int maxn = 2048;

vector<int> edges[maxn];
int state[maxn], parent[maxn];

vector< vector<int> > cycles;

int n, shortest;

void find_cycles(const vector<bool>& exists) {
  /*
  for (int i = 0; i < n; ++i) if (exists[i])
    printf("%i ", i);
  puts("");
  */
  for (int i = 0; i < n; ++i) if (exists[i])
    for (int a = 0; a < edges[i].size(); ++a) {
      int j = edges[i][a];
      if (i < j && exists[j]) {
        vector<bool> up(n), down(n);
        up[i] = up[j] = down[i] = down[j] = true;
        int d = 0, u = 0;
        for (int v = 0; v < n; ++v) if (exists[v] && v != i && v != j) {
          if (i < v && v < j) { down[v] = true; ++d; }
          else { up[v] = true; ++u; }
        }
        if (u > 0 && d > 0) {
 //         printf("pick edge %i %i\n", i, j);
          find_cycles(up);
          find_cycles(down);
          return;
        }
      }
    }
  vector<int> cycle;
  for (int i = 0; i < n; ++i) if (exists[i])
    cycle.push_back(i);
  cycles.push_back(cycle);
  shortest = min(shortest, (int)cycle.size());
}

int color[maxn];

int main() {
  int cases;
  scanf("%i", &cases);
  for (int numcase = 1; numcase <= cases; ++numcase) {
    printf("Case #%i: ", numcase);
    int m;
    scanf("%i%i", &n, &m);

    for (int i = 0; i < n; ++i) edges[i].clear();

    int warra[n][2];
    for (int t = 0; t < 2; ++t)
      for (int i = 0; i < m; ++i) {
        scanf("%i", &warra[i][t]);
        --warra[i][t];
      }
    for (int i = 0; i < m; ++i) {
      edges[warra[i][0]].push_back(warra[i][1]);
      edges[warra[i][1]].push_back(warra[i][0]);
    }
    vector<bool> vertices(n, true);
    cycles.clear();
    shortest = n;
    find_cycles(vertices);

    /*
    printf("cycles:\n");
    for (int i = 0; i < cycles.size(); ++i) {
      for (int j = 0; j < cycles[i].size(); ++j)
        printf("%i ", cycles[i][j]);
      puts("");
    }
    puts("ya");
    */

    for (int nc = shortest; nc >= 0; --nc) {
      int posib = 1;
      for (int i = 0; i < n; ++i) posib *= nc;

      for (int x = 0; x < posib; ++x) {
        int y = x;
        for (int i = 0; i < n; ++i) {
          color[i] = y % nc;
          y /= nc;
        }

        bool valid = true;
        for (int i = 0; i < cycles.size(); ++i) {
          bool used[maxn];
          fill(&used[0], &used[nc], false);
          for (int j = 0; j < cycles[i].size(); ++j)
            used[color[cycles[i][j]]] = true;
          if (count(&used[0], &used[nc], true) != nc) {
            valid = false;
            break;
          }
        }
        if (valid) {
          printf("%i\n", nc);
          for (int i = 0; i < n; ++i)
            printf("%i ", color[i] + 1);
          puts("");
          goto end;
        }
      }
    }
end:;
  }
  return 0;
}
