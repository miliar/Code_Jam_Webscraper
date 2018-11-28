#include <iostream>
#include <string.h>
#include <sstream>
#include <string>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <list>
#include <map>

using namespace std;

struct vine { int d, L; };
vine vines[10000];

struct state { int v; int d;  state(int v_, int d_) : v(v_), d(d_) {} };

void solve (int a_case)
{
  int N, D;
  cin >> N;

  for (int i = 0; i < N; ++i) {
    cin >> vines[i].d >> vines[i].L;
  }

  cin >> D;

  set<state> visited;
  queue<state> q;

  q.push(state(0, vines[0].d));

  while (q.empty() == false) {
    state s = q.front(); q.pop();

    if (vines[s.v].d + s.d >= D) { printf("Case #%d: YES\n", a_case); return; }

    for (int i = s.v + 1; i < N; ++i) {
      if (vines[s.v].d + s.d >= vines[i].d) { // can reach vine
        int d = min(vines[i].L, vines[i].d - vines[s.v].d);
        q.push(state(i, d));
      }
    }
  }

  printf("Case #%d: NO\n", a_case);
}

int main ()
{
  int n;
  string dummy;

  cin >> n;
  getline(cin, dummy);
  for (int i = 0; i < n; ++i) solve(i+1);

  return 0;
}

