#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

int m, inner;
int g[10*1024], c[10*1024], v[10*1024];
int bbuf[10*1024][2];

int force (int node, int value);
int apply (int node, int value, int is_and);

void solve () {
  int V;
  cin >> m >> V;
  inner = (m-1)/2;
  for (int i = 1; i <= inner; ++i) {
    cin >> g[i] >> c[i];
  }
  for (int i = inner+1; i <= m; ++i)
    cin >> v[i];

  for (int i = 0; i <= m; ++i)
    bbuf[i][0] = bbuf[i][1] = -1;

  int best = force (1, V);
  if (best > m) cout << "IMPOSSIBLE" << endl;
  else cout << best << endl;
}

int force (int node, int value) {
  if (bbuf[node][value] >= 0) return bbuf[node][value];

  if (node > inner) {
    return bbuf[node][value] = ((value == v[node]) ? 0 : m+1);
  }

  if (c[node]) 
    return bbuf[node][value] = 
      (min (apply (node, value, g[node]), 
	    1 + apply (node, value, 1-g[node])));
  else
    return bbuf[node][value] = (apply (node, value, g[node]));
}

int apply (int node, int value, int is_and) {
  int left = 2*node;
  int right = left + 1;

  if (is_and) {
    if (value)
      return force (left, 1) + force (right, 1);
    else 
      return min (force (left, 0), force (right, 0));
  } else {
    if (value)
      return min (force (left, 1), force (right, 1));
    else
      return force (left, 0) + force (right, 0);
  }
}

int main () {
  int N; cin >> N;
  for (int i = 1; i <= N; ++i) {
    cout << "Case #" << i << ": ";
    solve ();
  }
  return 0;
}

