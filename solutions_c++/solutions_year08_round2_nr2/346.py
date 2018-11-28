#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

typedef long long ll;

int uf[1024*1024];

ll a, b, p;

int find (int x) {
  if (uf[x] == x) return x;
  return uf[x] = find (uf[x]);
}

void join (int x, int y) {
  uf[find (x)] = find (y);
}

bool is_p (int x) {
  if (x == 2) return true;
  if ((x % 2) == 0) return false;
  for (int i = 3; i*i <= x; i += 2) {
    if ((x % i) == 0) return false;
  }
  return true;
}

void factor (ll x) {
  for (ll y = p; y <= x; ++y) {
    if (x % y == 0 && is_p (y)) {
      for (ll z = x + y; z <= b; z += y) {
	join (z-a, x-a);
      }
    }
  }
}

void solve () {
  cin >> a >> b >> p;

  for (int i = b-a; i >= 0; --i)
    uf[i] = i;

  
  for (ll x = a; x <= b; ++x) {
    factor (x);
  }

  set<int> r;
  for (int i = b-a; i >= 0; --i) {
    r.insert (find(i));
  }
  cout << r.size () << endl;
}

int main () {
  int N; cin >> N;
  for (int i = 1; i <= N; ++i) {
    cout << "Case #" << i << ": ";
    solve ();
  }
  return 0;
}

