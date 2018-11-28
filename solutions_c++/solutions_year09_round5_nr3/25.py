#include <algorithm>
#include <string>
#include <vector>
#include <cassert>
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
using namespace __gnu_cxx;

typedef long long ll;
const int infinity = 1000000000;

const int maxn = 1000;

vector<int> edge[maxn], edge2[maxn];
int col[maxn];
bool joined[maxn][maxn];

bool dfs(int v, int c) {
  col[v] = c;
  for (int j = 0; j < edge2[v].size(); ++j) {
    int k = edge2[v][j];
    if (col[k] == c) return false;
    if (col[k] < 0 && !dfs(k, c ^ 1)) return false;
  }
  return true;
}
    int x[maxn], y[maxn];

struct cmp {
  bool operator()(int a, int b) const {
    return x[a] < x[b];
  }
};

int main() {
  int cases;
  scanf("%i\n", &cases);
  for (int caseno = 1; caseno <= cases; ++caseno) {
    printf("Case #%i: ", caseno);
    int n;
    scanf("%i", &n);

    vector<int> v;
    for (int i = 0; i < n; ++i) {
      scanf("%i%i", &x[i], &y[i]);
      edge[i].clear();
      edge2[i].clear();
      v.push_back(i);
    }

    fill(&joined[0][0], &joined[n][0], false);
    for (int i = 0; i < n; ++i)
      joined[i][i] = true;
    
    for (int i = 0; i < n; ++i) {
      int m[3] = { -1, -1, -1 };
      for (int j = 0; j < n; ++j)
        if (x[i] < x[j] && abs(y[i] - y[j]) <= 1) {
          int d = y[i] - y[j] + 1;
          if (m[d] < 0 || x[j] < x[m[d]])
            m[d] = j;
        }
      for (int k = 0; k < 3; ++k) {
        int j = m[k];
        if (j < 0) continue;

        edge[i].push_back(j);
//        edge[j].push_back(i);
        edge2[j].push_back(i);
        edge2[i].push_back(j);
        joined[i][j] = joined[j][i] = true;
      }
    }
    int maxdeg = 0;
    for (int ii = 0; ii < n; ++ii)
      maxdeg = max(maxdeg, (int)edge[ii].size());
    if (maxdeg == 0) { puts("1"); continue; }

    fill(&col[0], &col[n], -1);
    bool bip = true, connected = true;
    for (int i = 0; i < n; ++i) {
      if (i != 0 && col[i] < 0) connected = false;
      if (col[i] < 0 && !dfs(i, 0)) {
        bip = false;
        break;
      }
    }
    if (bip) { puts("2"); continue; }

    bool complete = true;
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
        if (!joined[i][j]) complete = false;

    int numcol = 4;
    sort(v.begin(), v.end(), cmp());

    for (int t = 0; t < 10000; ++t) {
      fill(&col[0], &col[n], -1);
      int maxc = 0;
      for (int i = n - 1; i >= 0; --i) {
        int used[4] = { false, false, false, false };
        int a = v[i];
        
        int perm[4];
        for (int i = 0; i < 4; ++i) perm[i] = i;
        if (t) {
          random_shuffle(&perm[0], &perm[3]);
        }

        for (int j = 0; j < edge[a].size(); ++j) {
          int b = edge[a][j];
          assert(col[b] >= 0);
          used[col[b]] = true;
        }
        for (int j = 0; j < 4; ++j)
          if (!used[perm[j]]) {
            col[a] = perm[j];
            break;
          }
        assert(edge[a].size() <= 3 && col[a] >= 0);
        maxc = max(maxc, col[a]);
        if (col[a] == 3 && t > 0) break;
      }

      numcol = min(numcol, maxc + 1);
    }
    assert(numcol > 2 && numcol <= maxdeg + 1 && maxdeg >= 2);
 /*   if (numcol == 4 && connected && !complete)
      numcol = maxdeg;*/
    printf("%i\n", numcol);
        
    fflush(stdout);
  }
  return 0;
}
