
#include <iostream>
#include <map>
#include <queue>
#include <set>

using namespace std;

int R, C, F;
char m[51][51];

struct node {
  int i, j, dig;
  set<pair<int, int> > dug;
  bool operator<(const node & o) const
  {
    if (dig != o.dig) return dig > o.dig;
    if (i != o.i) return i < o.i;
    if (j != o.j) return j < o.j;
    return dug < o.dug;
  }
};

map<node, bool> visited;

bool air_at(node & v, int i, int j) { return m[i][j] == '.' || v.dug.find(make_pair(i, j)) != v.dug.end(); }

int depth(node & v, int i, int j) {
  if (!air_at(v, i, j)) return 0;
  if (i == R) return 1;
  return 1 + depth(v, i+1, j);
}

bool can_dig(node & v, int d) {
  if (!(v.j + d > 0 && v.j + d <= C)) return false;
  return air_at(v, v.i, v.j + d) && !air_at(v, v.i+1, v.j + d);
}

bool valid(node & v) {
  if (!(v.i > 0 && v.j > 0 && v.i <= R && v.j <= C)) return false;
  if (!air_at(v, v.i, v.j)) return false;
  if (depth(v, v.i+1, v.j) > F) return false;
  return true;
}

void solve(int CASE)
{
  cin >> R >> C >> F;
  for (int i = 1; i <= R; i++)
    for (int j = 1; j <= C; j++)
      cin >> m[i][j];

  visited.clear();
  node s;
  s.i = 1;
  s.j = 1;
  s.dig = 0;

  //printf("DEPTH: %d\n", depth(s, 1, 2));

  priority_queue<node> q;
  q.push(s);

  while (!q.empty())
  {
    node v = q.top(); q.pop();
    //printf("%d, %d (%d = %u)\n", v.i, v.j, v.dig, v.dug.size());
    if (visited[v]) continue;
    if (v.i == R) { printf("Case #%d: Yes %d\n", CASE, v.dig); return; }
    visited[v] = true;

    node w = v;
    w.j--;
    if (valid(w)) { while(w.i < R && air_at(w, w.i+1, w.j)) w.i++; q.push(w); }

    w = v;
    w.j++;
    if (valid(w)) { while(w.i < R && air_at(w, w.i+1, w.j)) w.i++; q.push(w); }

    w = v;
    if (can_dig(w, -1)) { w.dig++; w.dug.insert(make_pair(w.i+1, w.j-1)); q.push(w); }

    w = v;
    if (can_dig(w, 1)) { w.dig++; w.dug.insert(make_pair(w.i+1, w.j+1)); q.push(w);  }

  }

  printf("Case #%d: No\n", CASE);
}


int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++)
    solve(i);
  return 0;
}
