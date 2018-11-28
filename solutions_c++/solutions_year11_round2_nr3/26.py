#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cassert>
#include <queue>
#include <cctype>
using namespace std;

typedef long double Real;

const Real o = 1e-8;
const Real pi = acos(-1.0);
const int max_n = 2048;
const int oo = 0x7fffffff;

int u[max_n], v[max_n], color[max_n];
bool used[max_n];
int n, m, T, I, ans;
vector<int> a[max_n];

void input() {
  cin >> n >> m;
  for (int x = 0; x < n; x++)
    a[x].clear();
  for (int i = 0; i < m; i++) {
    cin >> u[i];
    u[i]--;
  }
  for (int i = 0; i < m; i++) {
    cin >> v[i];
    v[i]--;
  }
  for (int i = 0; i < m; i++) {
    int x = u[i], y = v[i];
    a[x].push_back(y); a[y].push_back(x);
  }
  for (int x = 0; x < n; x++) {
    a[x].push_back((x + 1) % n);
    a[x].push_back((x + n - 1) % n);
  }
  for (int x = 0; x < n; x++) {
    sort(a[x].begin(), a[x].end());
    a[x].resize(unique(a[x].begin(), a[x].end()) - a[x].begin());
  }
}

void traverse(int x, int y, vector<int> &room) {
  room.clear();
  room.push_back(x);
  int z = x;
  while (true) {
    vector<int>::iterator it = lower_bound(a[z].begin(), a[z].end(), y);
    if (z != x && it != a[z].end() && *it == y) {
      room.push_back(y);
      break;
    }
    assert(it != a[z].begin());
    --it;
    assert(*it > z);
    room.push_back(*it);
    z = *it;
  }
#if 0
  cerr << "room:";
  for (size_t i = 0; i < room.size(); ++i)
    cerr << " " << room[i];
  cerr << endl;
#endif
}

int min_room(int x, int y) {
  assert(x < y);
  if (x + 1 == y)
    return oo;
  vector<int> room;
  traverse(x, y, room);
  int res = (int)room.size();
  assert(res >= 3);
  for (size_t i = 0, E = room.size(); i + 1 < E; ++i) {
    int cur = min_room(room[i], room[i + 1]);
    res = min(res, cur);
  }
  return res;
}

void check(int x, int y) {
  assert(x < y);
  if (x + 1 == y)
    return;
  vector<int> room;
  traverse(x, y, room);
  memset(used, 0, sizeof used);
  // cerr << "check: ans = " << ans << endl;
  for (size_t i = 0; i < room.size(); ++i)
    used[color[room[i]]] = true;
  for (int j = 0; j < ans; ++j)
    assert(used[j]);
  for (size_t i = 0, E = room.size(); i + 1 < E; ++i)
    check(room[i], room[i + 1]);
}

void print_colors() {
  cerr << "color:";
  for (int i = 0; i < n; ++i)
    cerr << " " << color[i];
  cerr << endl;
}

void paint(int x, int y) {
  assert(x < y);
  assert(color[x] >= 0 && color[y] >= 0);
#if 0
  if (color[x] == color[y]) {
    cerr << x << ' ' << y << endl;
    print_colors();
  }
#endif
  assert(color[x] != color[y]);
  if (x + 1 == y)
    return;
  vector<int> room;
  traverse(x, y, room);
  if ((int)room.size() == ans) {
    int cur = 0;
    for (size_t i = 1, E = room.size(); i + 1 < E; ++i) {
      while (cur == color[x] || cur == color[y])
        cur = (cur + 1) % ans;
      color[room[i]] = cur;
      cur++;
    }
  } else {
    for (size_t i = 1, E = room.size(); i + 1 < E; ++i)
      color[room[i]] = (color[room[i - 1]] + 1) % ans;
    if (color[room[room.size() - 2]] == color[room[room.size() - 1]]) {
      swap(color[room[room.size() - 3]], color[room[room.size() - 2]]);
    }
  }
  for (size_t i = 0, E = room.size(); i + 1 < E; ++i)
    paint(room[i], room[i + 1]);
}

void solve() {
  ans = min_room(0, n - 1);
  memset(color, -1, sizeof color);
  assert(ans >= 3);
  color[0] = 0; color[n - 1] = 1;
  paint(0, n - 1);
  check(0, n - 1);
}

void output() {
  printf("Case #%d: %d\n", I + 1, ans);
  for (int x = 0; x < n; ++x) {
    assert(color[x] >= 0);
    if (x > 0)
      printf(" ");
    printf("%d", color[x] + 1);
  }
  printf("\n");
}

int main() {
  cin >> T;
  for (I = 0; I < T; ++I) {
    input();
    solve();
    output();
  }
	return 0;
}

