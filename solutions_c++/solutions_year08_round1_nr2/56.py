#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int n;
int m;
vector<pair<int, int> > cust[2222];
bool res[2222];
bool ok[2222];

bool solve()
{
  for (int i = 0; i < n; i++) {
    res[i] = false;
  }
  for (int i = 0; i < m; i++) {
    ok[i] = false;
  }
  bool done;
  do {
    done = true;
    for (int i = 0; i < m; i++) {
      if (cust[i].size() != 1) continue;
      int X = cust[i][0].first;
      int V = cust[i][0].second;
      res[X] = V;
      for (int j = 0; j < m; j++) {
        for (int k = 0; k < cust[j].size(); k++) {
          if (cust[j][k].first != X) continue;
          if (cust[j][k].second == V) {
            ok[j] = true;
            cust[j].clear();
            break;
          }
          cust[j].erase(cust[j].begin() + k);
          k--;
        }
        if (!ok[j] && cust[j].empty()) return false;
      }
      done = false;
      break;
    } 
  } while (!done);
  return true;
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int cas = 1; cas <= t; cas++) {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++) {
      int k;
      cust[i].clear();
      scanf("%d", &k);
      for (int j = 0; j < k; j++) {
        int a, b;
        scanf("%d %d", &a, &b);
        cust[i].push_back(make_pair(a-1, b));
      }
    }
    printf("Case #%d:", cas);
    if (solve()) {
      for (int i = 0; i < n; i++) {
        printf(" %d", int(res[i]));
      }
      puts("");
    } else {
      puts(" IMPOSSIBLE");
    }
  }
}
