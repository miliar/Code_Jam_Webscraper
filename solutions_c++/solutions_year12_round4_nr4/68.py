#include <iostream>
#include <cstdio>
#include <set>
#include <map>
#include <vector>
using namespace std;

typedef pair<int, int> state;

int dfs(state const& S, map<pair<state, int>, vector<state>> const& neigh, set<state>& done)
{
  if (done.count(S)) return 0;
  done.insert(S);
  int res = 1;
  for (int i = 0; i < 3; i++) {
    auto it = neigh.find({S, i});
    if (it == neigh.end()) continue;
    for (state const& T: it->second) {
      res += dfs(T, neigh, done);
    }
  }
  return res;
}

int dfs2(pair<state, state> const& S, map<pair<state, int>, vector<state>> const& neigh, set<pair<state, state>>& done)
{
  if (done.count(S)) return 0;
  done.insert(S);
  int res = 1;
  for (int i = 0; i < 3; i++) {
    state const& S1 = S.first;
    state const& S2 = S.second;
    auto it1 = neigh.find({S1, i});
    if (it1 == neigh.end()) continue;
    auto it2 = neigh.find({S2, i});
    if (it2 == neigh.end()) continue;
    for (state const& T1: it1->second) {
      for (state const& T2: it2->second) {
        res += dfs2({T1, T2}, neigh, done);
      }
    }
  }
  return res;
}

pair<int, bool> solve(state const& S, vector<vector<char>> const& plan, map<pair<state, int>, vector<state>> const& neigh)
{
  int r = plan.size();
  int c = plan[0].size();
  set<state> done;
  int n = dfs(S, neigh, done);
  set<pair<state, state>> done2;
  int n2 = dfs2({S, S}, neigh, done2);
  return {n, n2 == n*n};
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int case_ = 1; case_ <= t; case_++) {
    int r, c;
    scanf("%d %d", &r, &c);
    vector<vector<char>> plan(r, vector<char>(c, '?'));
    vector<state> caves;
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        scanf(" %c", &plan[i][j]);
        if (plan[i][j] >= '0' && plan[i][j] <= '9') {
          int k = plan[i][j] - '0';
          if (caves.size() <= k) caves.resize(k+1);
          caves[k] = {i, j};
        }
      }
    }

    map<pair<state, int>, vector<state>> neigh;
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if (plan[i][j] == '#') continue;
        if (plan[i+1][j] != '#') neigh[make_pair(make_pair(i+1, j), 0)].push_back({i, j});
        else neigh[make_pair(make_pair(i,j), 0)].push_back({i, j});
        if (plan[i][j+1] != '#') neigh[make_pair(make_pair(i, j+1), 1)].push_back({i, j});
        else neigh[make_pair(make_pair(i,j), 1)].push_back({i, j});
        if (plan[i][j-1] != '#') neigh[make_pair(make_pair(i, j-1), 2)].push_back({i, j});
        else neigh[make_pair(make_pair(i,j), 2)].push_back({i, j});
      }
    }

    printf("Case #%d:\n", case_);
    int nc = caves.size();
    for (int i = 0; i < nc; i++) {
      auto p = solve(caves[i], plan, neigh);
      printf("%d: %d %s\n", i, p.first, p.second ? "Lucky" : "Unlucky");
    }
  }
  return 0;
}
