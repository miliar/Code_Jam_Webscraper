#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <cassert>

using namespace std;

typedef long long ll;

int n;
vector<int> g[8];
vector<vector<int> > cycles;
int col[8];

bool assign(int cur, int c){
  if(cur == n){
    bool use[c];
    for(int i = 0; i < cycles.size(); ++i){
      fill_n(use, c, false);
      for(int j = 0; j < cycles[i].size(); ++j)
        use[col[cycles[i][j]]] = true;
      if(count(use, use+c, true) != c)
        return false;
    }
    return true;
  }

  for(int i = 0; i < c; ++i){
    col[cur] = i;
    if(assign(cur+1, c))
      return true;
  }
  return false;
}

void dfs(int cur, vector<int> &cycle, int prev = -1){
  for(int i = 0; i < g[cur].size(); ++i)
    if(prev != g[cur][i])
      if(col[g[cur][i]] == 1)
        return;
      else if(col[g[cur][i]] == 2){
        cycle.push_back(cur);
        cycles.push_back(cycle);
        cycle.pop_back();
        return;
      }

  cycle.push_back(cur);
  for(int i = 0; i < g[cur].size(); ++i){
    int j = g[cur][i];
    if(j != prev){
      if(col[j] == -1){
        col[j] = 1;
        dfs(j, cycle, cur);
        col[j] = -1;
      }
      else{
        assert(false);
      }
    }
  }
  cycle.pop_back();
}
void calc_cycle(void){
  fill_n(col, n, -1);
  vector<int> cycle;
  for(int i = 0; i < n; ++i){
    col[i] = 2;
    dfs(i, cycle);
    col[i] = -1;
  }
}

int main(void){
  int t;
  cin >> t;
  for(int k = 0; k < t; ++k){
    cycles.clear();
    int m;
    cin >> n >> m;
    for(int i = 0; i < n; ++i)
      g[i].clear();
    for(int i = 0; i < n; ++i){
      g[i].push_back((i+1)%n);
      g[(i+1)%n].push_back(i);
    }

    int u[m], v[m];
    for(int j = 0; j < m; ++j)
      cin >> u[j];
    for(int j = 0; j < m; ++j){
      cin >> v[j];
      g[u[j]-1].push_back(v[j]-1);
      g[v[j]-1].push_back(u[j]-1);
    }

    // for(int i = 0; i < n; ++i){
    //   for(int j = 0; j < g[i].size(); ++j)
    //     cout << g[i][j] << ' ';
    //   cout << endl;
    // }

    calc_cycle();
    // cout << "--" << endl;
    // for(int i = 0; i < cycles.size(); ++i){
    //   for(int j = 0; j < cycles[i].size(); ++j)
    //     cout << cycles[i][j] << ' ';
    //   cout << endl;
    // }
    // cout << "--" << endl;

    cout << "Case #" << k+1 << ": ";
    for(int c = 5; c >= 1; --c){
      // cout << "assign: " << c << endl;
      if(assign(0, c)){
        cout << c << endl;
        for(int i = 0; i < n; ++i){
          if(i > 0) cout << ' ';
          cout << col[i] + 1;
        }
        cout << endl;
        goto end;
      }
    }
  end:;
  }

  return 0;
}
