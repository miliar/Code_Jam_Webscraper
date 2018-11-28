#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)

int main()
{
  int T;
  cin >> T;
  FOR(t,1,T+1) {
    int N;
    cin >> N;
    vector<int> x(N-1);
    REP(i,N-1) {
      cin >> x[i];
      --x[i];
    }

    vector<long long> ans(N);
    ans[N-1] = ans[N-2] = 1;
    for (int i = N-3; i >= 0; --i) {
      double m = -HUGE_VAL;
      double M = HUGE_VAL;
      for (int j = i+1; j < N; ++j) {
        if (j == x[i]) continue;
        int dist = x[i] - j;
        int diff = ans[x[i]] - ans[j];
        double d = ans[x[i]] + (double)diff / dist * (i - x[i]);
        if (j < x[i]) m = max(m, d + 1e-12);
        else M = min(M, d);
      }
      if (m == -HUGE_VAL) {
        ans[i] = (long long)floor(M - 1.0);
        if (ans[i] <= 0) {
          FOR(j,i+1,N) {
            ans[j] += 1 - ans[i];
          }
          ans[i] = 1;
        }
        continue;
      }
      if (M == HUGE_VAL) {
        ans[i] = (long long)ceil(m);
        if (ans[i] <= 0) {
          FOR(j,i+1,N) {
            ans[j] += 1 - ans[i];
          }
          ans[i] = 1;
        }
        continue;
      }
      if (m >= M) {
        cout << "Case #" << t << ": Impossible" << endl;
        goto fail;
      }
      for (int k = 1; ; ++k) {
        long long kM = (long long)(k * M);
        long long km = (long long)ceil(k * m);
        if (kM > km) {
          FOR(j,i+1,N) {
            ans[j] *= k;
          }
          ans[i] = km;
          if (km <= 0) {
            FOR(j,i,N) {
              ans[j] += 1 - km;
            }
          }
          break;
        }
      }
    }
    cout << "Case #" << t << ':';
    REP(i,N) {
      cout << ' ' << ans[i];
    }
    cout << endl;
  fail:;
  }

  return 0;
}
