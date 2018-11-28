#include <iostream>
#include <cstdio>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <functional>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <string>
#include <sstream>
#include <fstream>
#include <complex>
#include <iterator>
#include <memory>
#include <utility>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define rep(i,s,n) for(int i=s;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define MP(a, b) make_pair((a), (b))
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long double ld;
typedef long long ll;
static const double PI = atan(1.0) * 4.0;
int in_c() { int c; while ((c = getchar()) <= ' ') { if (!~c) return ~0; } return c; }
int in() {
  int x = 0, c;
  while ((ui)((c = getchar()) - '0') >= 10) { if (c == '-') return -in(); if (!~c) return ~0; }
  do { x = 10 * x + (c - '0'); } while ((ui)((c = getchar()) - '0') < 10);
  return x;
}


const int MN = 2000, MM = MN - 3;
int N, M;
int U[MM], V[MM];

void Input() {
  cin >> N >> M;
  REP(i, M) {
    cin >> U[i];
    --U[i];
  }
  REP(i, M) {
    cin >> V[i];
    --V[i];
  }
}

// split room using wall (U[c], V[c])
vector<vector<int> > Split(int c, const vector<int>& room) {
  vector<vector<int> > res;
  vector<int> left, right;
  FOR(it, room) if (*it != U[c] && *it != V[c]) {
    if (U[c] < *it && *it < V[c]) {
      left.push_back(*it);
    } else {
      right.push_back(*it);
    }
  }
  if (!left.empty()) {
    left.push_back(U[c]);
    left.push_back(V[c]);
    sort(ALL(left));
    res.push_back(left);
  }
  if (!right.empty()) {
    right.push_back(U[c]);
    right.push_back(V[c]);
    sort(ALL(right));
    res.push_back(right);
  }
  return res;
}

vector<vector<int> > Split(const vector<int>& v) {
  REP(i, M) {
    if (binary_search(ALL(v), U[i]) &&
        binary_search(ALL(v), V[i])) {
//       cout << "split: " << U[i] << ", " << V[i] << endl;
//       FOR(jt, v) cout << *jt << ' ';
//       cout << endl;
      vector<vector<int> > vv = Split(i, v);
//       cout << "result: ";
//       FOR(jt, vv) {
//         FOR(kt, *jt) cout << *kt << ' ';
//         cout << endl;
//       }
      if (vv.size() > 1)
        return vv;
    }
  }
  vector<vector<int> > vv;
  vv.push_back(v);
  return vv;
}

vector<vector<int> > Split() {
  vector<int> v;
  REP(i, N) v.push_back(i);
  vector<vector<int> > collection, result;
  collection.push_back(v);
  while (!collection.empty()) {
    vector<int> v = collection.back();
    collection.pop_back();
    vector<vector<int> > vv = Split(v);
    assert(vv.size() >= 1);
    if (vv.size() == 1) {
      copy(ALL(vv), back_inserter(result));
    } else {
      copy(ALL(vv), back_inserter(collection));
    }
  }
  return result;
}

typedef vector<vector<int> > Graph;
int R;
int MIN_ROOM;

struct Sorter {
  bool operator() (const vector<int>& lhs,
                   const vector<int>& rhs) const {
    if (lhs.size() != rhs.size())
      return lhs.size() < rhs.size();
    return lhs < rhs;
  }
};

Graph MakeGraph(const vector<vector<int> >& rooms) {
  R = rooms.size();
  MIN_ROOM = N;
  Graph g(R);
  REP(i, R) {
    MIN_ROOM = min(MIN_ROOM, (int) rooms[i].size());
    FOR(it, rooms[i])
        g[i].push_back(*it);
  }
  return g;
}

int ans;
int color[MN];
map<int, int> room_has_flavors[MN];
vector<vector<int> > rooms;

bool Check(int max_color) {
  FOR(it, rooms) {
    set<int> cs;
    FOR(jt, *it) cs.insert(color[*jt]);
    if (cs.size() != max_color) return false;
  }
  return true;
}

bool Dfs(int i, int max_color) {
  if (i == N) {
    return Check(max_color);
  }
  REP(j, max_color) {
    color[i] = j;
    if (Dfs(i + 1, max_color))
      return true;
  }
  return false;
}

void Solve() {
  Input();
  rooms = Split();
  sort(ALL(rooms), Sorter());
  Graph g = MakeGraph(rooms);
  if (N == 8 && rooms.size() == 1) {
    ans = N;
    REP(i, N) color[i] = i;
  } else {
    for (int i = MIN_ROOM; i > 0; --i) {
      if (Dfs(0, i)) {
        ans = i;
        return;
      }
    }
  }
}


int main() {
  int T;
  cin >> T;
  REP(turn, T) {
    Solve();
    printf("Case #%d: %d\n", turn + 1, ans);
    REP(i, N) printf("%d%c", color[i] + 1, i == N - 1 ? '\n' : ' ');
  }
  return 0;
}
