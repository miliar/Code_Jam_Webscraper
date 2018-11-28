#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

bool g[8][8];

vector<vector<int> > cycles;
int ss[10], ssidx;

int n, m;
bool here[10];

void dfs(int v, int parent){
  here[v] = true;
  ss[ssidx++] = v;
  FOR (i, n)
    if (i != parent && g[v][i]){
      if (here[i]){
        vector<int> a;
        int idx = ssidx - 1;
        a.pb(i);
        while (ss[idx] != i)
          a.pb(ss[idx--]);
        cycles.pb(a);
      }
      else
        dfs(i, v);
    }
  here[v] = false;
  ssidx--;
}

int used[8], color[8], ret, cntUsed;

bool poss;

bool check(){
  FOR (i, cycles.sz){
    vector<int> cycle = cycles[i];
    bool y[ret];
    int c = 0;
    SET(y, 0);
    FOR (j, cycle.sz){
      int col = color[cycle[j]];
      if (!y[col]){
        y[col] = true;
        c++;
      }
    }

    if (c != ret)
      return false;
  }
  
  return true;
}

void find(int v){
  if (poss)
    return;
  
  if (v == n){
    if (cntUsed != ret)
      return;
    if (check())
      poss = true;
    return;
  }
  
  FOR (col, ret){
    int c = color[v];
    if (c != -1){
      used[c]--;
      if (!used[c])
        cntUsed--;
    }
    if (!used[col])
      cntUsed++;
    used[col]++;
    color[v] = col;
    find(v + 1);
    if (poss)
      break;
  }
}

int main(){
  freopen("Cs.out","wt", stdout);
  freopen("Cs.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  int a, b;
  FOR (test, tests){
    cin >> n >> m;
    SET(g, 0);
    FOR (i, n)
      g[i][(i + 1) % n] = g[(i + 1) % n][i] = true;
    
    int a1[m], a2[m];
    FOR (i, m){
      cin >> a1[i];
      a1[i]--;
    }
    FOR (i, m){
      cin >> a2[i];
      a2[i]--;
    }
    FOR (i, m)
      g[a1[i]][a2[i]] = g[a2[i]][a1[i]] = true;

    SET(here, 0);
    ssidx = 0;
    cycles.clear();
    dfs(0, -1);

    int mi = 1 << 20;
    FOR (i, cycles.sz)
      mi <?= cycles[i].sz;
    
    poss = false;
    for (ret = mi; ret > 1; ret--){
      SET(used, 0);
      SET(color, 255);
      cntUsed = 0;
      find(0);
      if (poss)
        break;
    }

    cout << "Case #" << (test + 1) << ": ";
    cout << ret << "\n";
    FOR (i, n)
      cout << color[i] + 1 << " ";
    cout << endl;
  }
  return 0;
}
