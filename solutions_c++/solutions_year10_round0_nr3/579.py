#include <cstdio>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

#define ll long long

int main () {
  int tests;
  int R, k, N, i, j;
  vector<int> g, next;
  vector<ll> people;

  scanf("%d", &tests);
  for (int test = 0; test < tests; ++test) {
    scanf("%d %d %d", &R, &k, &N);
    g.resize(N, 0);
    people.resize(N, 0);
    next.resize(N, 0);
    for (i = 0; i < N; ++i)
	scanf("%d", &g[i]);

    for (i = 0; i < N; ++i) {
      people[i] = next[i] = 0;
      for (j = 0; j < N; ++j) {
        if (people[i] + g[(i+j)%N] > k)
           break;
        people[i] += (ll)g[(i+j)%N];
      }
      next[i] = (i+j)%N;
    }

    int cur = 0;
    ll ans = 0;
    for (i = 0; i < R; ++i) {
      ans += people[cur];
      cur = next[cur];
    }

    printf("Case #%d: ", test+1);
    cout << ans << endl;
  }
};

