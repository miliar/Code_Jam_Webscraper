#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <functional>
#include <utility>
#include <vector>
#include <list>

using namespace std;

typedef unsigned long long ullong;
typedef long long llong;
typedef list<int> EdgeList;
typedef vector<EdgeList> AdjList;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define FOR_EDGE(adj,v,it) for (EdgeList::iterator it = adj[v].begin(); \
    it != adj[v].end(); ++it)

int main() {
  setvbuf(stdin, NULL, _IOFBF, 10000);
  setvbuf(stdout, NULL, _IOFBF, 10000);
 
  int n_cases;
  scanf("%d", &n_cases);
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    int n, s, p;
    scanf("%d %d %d", &n, &s, &p);
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
      int x;
      scanf("%d", &x);
      if (x == 0) {
        if (p == 0) ++cnt;
      } else if (x >= 1 && (x+2)/3 >= p) {
        ++cnt;
      } else if (s > 0 && x >= 2 && (x+4)/3 >= p) {
          --s;
          ++cnt;
      }
    }
    printf("Case #%d: %d\n", ctr+1, cnt);
  }

  return 0;
}
