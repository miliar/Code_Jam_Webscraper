#include <cmath>
#include <iostream>
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
    vector<int> d(N+1), l(N+1);
    REP(i,N) {
      cin >> d[i] >> l[i];
    }
    cin >> d[N];
    l[N] = (int)1e9;

    vector<double> m(N+1,-1);
    m[0] = d[0];
    FOR(i,1,N+1) {
      REP(j,i) {
        if (m[j] < -0.5) continue;
        double dist = d[i] - d[j];
        double sq = m[j] * m[j] - dist * dist + 1e-12;
        if (sq < 0.0) continue;
        m[i] = max(m[i], min(dist, (double)l[i]));
      }
    }
    cout << "Case #" << t << ": "
         << (m[N] > -0.5 ? "YES" : "NO")
         << endl;
  }

  return 0;
}
