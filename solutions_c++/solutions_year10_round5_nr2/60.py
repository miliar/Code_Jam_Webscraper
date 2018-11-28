#include <iostream>
#include <set>
using namespace std;

#define INF 1000000000000000001LL

long long dp[100100], b[110], v[100100];

int main() {
  int t; cin >> t;
  for(int c = 1; c <= t; c++) {
    long long L;
    int n;
    cin >> L >> n;
    // L = 120438972084720248LL; n = 100;
    for(int i = 0; i < n; i++)
      cin >> b[i];
    sort(b, b+n);

    long long res = INF;
    for(int i = 0; i < n; i++)
      if(L % b[i] == 0)
        res = min(res, L / b[i]);

    for(int i = 0; i < b[n-1]; i++)
      dp[i] = INF;
    dp[0] = 0; v[0] = 0;
    for(int i = 1; i < b[n-1]; i++) {
      for(int j = 0; j < n && b[j] <= i; j++)
        dp[i] = min(dp[i], dp[i-b[j]]+1);
      v[i] = 0;
    }

    set<long long> active[2];
    for(int i = 0; i < b[n-1]; i++)
      if(dp[i] < INF)
        active[0].insert(i);

    int sw = 0;
    for(int i = 0; i < b[n-1]; i++) {
      active[1-sw].clear();

      // cout << "active: ";
      // for(set<long long>::iterator it = active[sw].begin(); it != active[sw].end(); ++it)
      //   cout << *it << " ";
      // cout << endl;

      for(set<long long>::iterator it = active[sw].begin(); it != active[sw].end(); ++it) {
        long long val = v[*it] * b[n-1] + *it;
        if(L % b[n-1] == *it)
          res = min(res, (L - val) / b[n-1] + dp[*it]);

        for(int j = 0; j < n-1; j++) {
          long long nv = *it + b[j];
          if(dp[*it] + 1 < (i + (nv / b[n-1]) - v[nv % b[n-1]]) + dp[nv % b[n-1]]) {
            dp[nv % b[n-1]] = dp[*it] + 1;
            v[nv % b[n-1]] = i + (nv / b[n-1]);
            if(nv >= b[n-1])
              active[1-sw].insert(nv % b[n-1]);
            else
              active[sw].insert(nv);
          }
        }
      }
      sw = 1-sw;
    }

    if(res == INF)
      printf("Case #%d: IMPOSSIBLE\n", c);
    else
      printf("Case #%d: %lld\n", c, res);
  }

  return 0;
}

