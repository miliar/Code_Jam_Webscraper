#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <queue>
#include <cstring>
using namespace std;

#define loop(i,n) for (int i = 0; i < (int)(n); ++i)
#define Bounded(x,a,b) ((a) <= (x) && (x) <= (b))
#define db(x) #x << " = " << x
#define pdb(x) printf("#x = %d\n",x);
#define All(x) x.begin(),x.end()
#define sz(x) x.size()
typedef vector<int> Vi;
typedef pair<int,int> Pii;
typedef vector<Vi> Adj;
typedef vector<bool> Vb;

void solve(int casenum) {
  int X, S, R, N; double t; cin >> X >> S >> R >> t >> N;
  Vi B(N), E(N), w(N);
  loop(i,N) {
    cin >> B[i] >> E[i] >> w[i];
  }

  R -= S;

  vector<Pii> d(N);
  int total_d = 0;
  loop(i,N) {
    d[i] = Pii(w[i]+S, E[i] - B[i]);
    total_d += d[i].second;
  }
  sort(All(d));

  double time = X / (double)S;
  loop(i,N) {
    time -= w[i] / (w[i] + (double)S) * (E[i]-B[i])/(double)S;
  }

  // printf("Time without running %f\n", time);

  double run_time = min(t, (X - total_d) / (S + (double)R));

  time -= R / (double)S * run_time;
  // printf("Running time off walkways %f (time %f)\n", run_time, time);

  t -= run_time;
  for (int i = 0; i < d.size(); ++i) {
    if (t > 1e-30) {
      double time_if_run = min(t, d[i].second / (double)(d[i].first + R));
      t -= time_if_run;
      time -= R / (double)d[i].first * time_if_run;
      // printf("Run on walkway %d for %.3f seconds, reduction in time is %.3f\n", i+1, time_if_run, R / (double)d[i].first * time_if_run);
    }
  }

  printf("Case #%d: %.10f\n", casenum, time);
}

int main() {
  int T; cin >> T;
  loop(i,T) solve(i+1);
  return 0;
}

