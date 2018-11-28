#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct X
{
  int N, D;
  vector<int> ds;
  vector<int> ls;
  vector<int> rs;
  queue<int> Q;

  bool run()
  {

    cin >> N;
    for (int i = 0; i < N; i++) {
      int d, l;
      cin >> d >> l;
      ds.push_back(d);
      ls.push_back(l);
      rs.push_back(0);
    }
    cin >> D;

    rs[0] = ds[0];
    Q.push(0);

    while (!Q.empty()) {
      int c = Q.front();
      Q.pop();

      int cd = ds[c];
      int cl = rs[c];
      if (cd + cl >= D) return true;

      for (int i = 0; i < N; i++) {
        if (i == c) continue;

        int d = ds[i];
        int l = ls[i];

        int dis = abs(cd - d);
        if (dis > cl) continue;
        
        if (l > dis) l = dis;
        if (rs[i] < l) {
          rs[i] = l;
          Q.push(i);
        }
      }
    }
    return false;
  }
};

int main()
{
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    X x;
    bool res = x.run();
    printf("Case #%d:", cas);
    printf(" %s", res ? "YES" : "NO");
    printf("\n");
  }

  return 0;
}
