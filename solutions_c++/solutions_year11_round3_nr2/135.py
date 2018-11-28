#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <algorithm>
#include <cstring>

using namespace std;

typedef unsigned long long u64;

const int N = 1000000;
u64 a[N];
bool boost[N];

u64 go(int i, int n, int l) {
  vector< pair<u64, int> > v;
  for (int j = i; j < n; j++) v.push_back(make_pair(a[j], j));
  sort(v.begin(), v.end(), greater< pair<u64, int> >());

  memset(boost, false, sizeof(boost));
  int cnt = l;
  if (cnt > v.size()) cnt = v.size();
  for (int j = 0; j < cnt; j++) boost[v[j].second] = true;

  u64 res = 0;
  for (int j = i; j < n; j++) {
    if (boost[j]) res += a[j] / 2; else res += a[j];
  }
  return res;
}

int main() {
  int t; cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    int L; u64 t; int n;
    int C;
    cin >> L >> t >> n >> C;
    for (int i = 0; i < C; i++) {
      cin >> a[i]; a[i] *= 2;
    }
    int idx = 0;
    for (int i = C; i < n; i++) {
      a[i] = a[idx++];
      if (idx == C) idx = 0;
    }

    u64 curr = 0;
    for (int i = 0; i < n; i++) {
      if (curr + a[i] <= t) {
        curr += a[i];
      } else {
        // wait
        u64 x = curr + a[i] + go(i+1, n, L);

        // use
        if (L > 0) {
          u64 first = t-curr;
          u64 rem = a[i] - first;
          u64 y = curr + first + rem / 2 + go(i+1, n, L-1);
          if (y < x) x = y;
        }
        curr = x;
        break;
      }
    }
    cout << "Case #" << tt << ": " << curr << endl;
  }

  return 0;
}

