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
typedef long long int ll;
typedef vector<ll> Vll;

void solve(int casenum) {
  ll L, t, N, C; cin >> L >> t >> N >> C;
  Vll A(C); loop(i,C) cin >> A[i];
  Vll dist(N+1, 0);
  loop(i,C) for (int k = 0; k*C+i < N; ++k) {
    dist[k*C+i+1] = A[i];
  }
  Vll sdist(N+1, 0);
  loop(i,N) sdist[i+1] = sdist[i] + dist[i+1];

  ll time = 0;
  loop(i,N+1) time += 2 * dist[i];

  Vll gain(N+1, 0);
  for (int i = 1; i <= N; ++i) {
    gain[i] = max(t/2-sdist[i-1], 0ll) - dist[i];
  }
  sort(All(gain));

  for (int i = 0; i < L; ++i) {
    time += gain[i];
  }

  printf("Case #%d: %d\n", casenum, time);
}

int main() {
  int T; cin >> T;
  loop(i,T) solve(i+1);
  return 0;
}

