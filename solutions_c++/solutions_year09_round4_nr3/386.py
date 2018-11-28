#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>

using namespace std;

struct state {
  int n;
  int mx;
  int v[100];
};

int solve_rec(int n, int edge[100][100], int m, int mx, int v[100])
{
  if (n == m) {
    return mx;
  }
  int result = 200;
  
  for (int i = 0; i < mx; i++) {
    int j;
    for (j = 0; j < m; j++) {
      if (v[j] == i && edge[j][m]) break;
      //cout << cur.v[j] << " " << i << " " << edge[j][cur.n] << endl; 
    }
    if (j == m) {
      v[m] = i;
      result = min(result, solve_rec(n, edge, m+1, mx, v));
    }
  }
  if (mx + 1 < result) {
    v[m] = mx;
    result = min(result, solve_rec(n, edge, m+1, mx+1, v));
  }
  return result;
}

int solve(int n, int edge[100][100])
{
  int v[100];
  return solve_rec(n, edge, 0, 0, v);
#if 0
  int result = 200;
  vector<state> stk;

  state s;
  s.n = 0;
  s.mx = 0;

  stk.push_back(s);

  while (stk.size() > 0) {
    state cur = stk.back();
    stk.pop_back();

    if (cur.n == n) {
      if (cur.mx < result) {
        //for (int i = 0; i < n; i++) {
        //  cout << cur.v[i] << " ";
        //}
        //cout << endl;
        result = cur.mx;
      }
      continue;
    }

    //cout << cur.n << " " << cur.mx << endl;
    for (int i = 0; i < cur.mx; i++) {
      int j;
      for (j = 0; j < cur.n; j++) {
        if (cur.v[j] == i && edge[j][cur.n]) break;
        //cout << cur.v[j] << " " << i << " " << edge[j][cur.n] << endl; 
      }
      if (j == cur.n) {
        state nw = cur;
        nw.n++;
        nw.v[cur.n] = i;
        stk.push_back(nw);
      }
    }
    if (cur.mx + 1 < result) {
      state nw = cur;
      nw.n++;
      nw.v[cur.n] = cur.mx;
      nw.mx++;
      stk.push_back(nw);
    }
  }
  return result;
#endif
}

int main()
{
  int cas;
  int N;

  cin >> N;

  for (cas = 1; cas <= N; cas++) {
    int n, k;
    cin >> n >> k;
    int v[100][26];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < k; j++) {
        int x;
        cin >> x;
        v[i][j] = x;
      }
    }

    int edge[100][100] = {{0}};
    for (int i = 0; i < n; i++) {
      for (int j = i+1; j < n; j++) {
        for (int l = 0; l < k-1; l++) {
          bool cross = false;
          int y0 = v[i][l];
          int y1 = v[i][l+1];
          int y2 = v[j][l];
          int y3 = v[j][l+1];
          if (y0 == y2 || y1 == y3) {
            cross = true;
          } else if (y0 > y2 && y1 < y3) {
            cross = true;
          } else if (y0 < y2 && y1 > y3) {
            cross = true;
          }
          if (cross) {
            //cout << i << "," << j << endl;
            edge[i][j] = edge[j][i] = 1;
            break;
          }
        }
      }
    }

    int color = solve(n, edge);
    cerr << cas << endl;
    cout << "Case #" << cas << ": " << color << endl;
  }

  return 0;
}

