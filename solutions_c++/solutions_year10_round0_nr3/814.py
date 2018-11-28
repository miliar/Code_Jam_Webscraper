#include <cstdio>
#include <string>
#include <deque>
#include <map>

using namespace std;

const int MAXN = 1123;

typedef long long int64;

int R, k, N;
int64 g[MAXN];

int64 next_ride(deque<int> &state) {
  int64 cap = 0;
  for (int i = 0; i < N; i++) {
    int f = state.front();
    if (cap + g[f] > k)
      break;
    cap += g[f];
    state.pop_front();
    state.push_back(f);
  }
  return cap;
}

int main() {
  int T;

  scanf(" %d", &T);
  for (int cases = 1; cases <= T; cases++) {
    scanf(" %d%d%d", &R, &k, &N);
    
    deque<int> state;
    map<deque<int>, pair<int64, int64> > visited;
    for (int i = 0; i < N; i++) {
      scanf(" %lld", &g[i]);
      state.push_back(i);
    }
    
    int64 rides = 0, cost = 0, crides, ccost;
    while (rides < R) {
      map<deque<int>, pair<int64, int64> >::iterator i;
      if ((i = visited.find(state)) != visited.end()) {
	crides = rides - i->second.first;
	ccost = cost - i->second.second;
	break;
      }

      visited[state] = make_pair(rides, cost);

      cost += next_ride(state);
      rides++;
    }

    if (rides < R) {
      int64 q = (R - rides) / crides;
      int64 r = (R - rides) % crides;
      
      for (int j = 0; j < r; j++)
	cost += next_ride(state);
      cost += q * ccost;
    }

    printf("Case #%d: %lld\n", cases, cost);
  }

  return 0;
}
