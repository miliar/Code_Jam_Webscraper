#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

char adj[400][400];
int adjlist[400][400];
int nadj[400];
int best[2][400][400];
int n;

vector <int> bfs(int start) {
  vector <int> dists(n, -1); dists[start] = 0;
  queue <int> q; q.push(start);
  while (!q.empty()) {
    int i = q.front(); q.pop();
    for (int j = 0; j < n; j++)
      if (adj[i][j] && dists[j] == -1) {
	dists[j] = dists[i]+1;
	q.push(j);
      }
  }
  return dists;
}

int main(void)
{
  int T; cin >> T;
  for (int test = 1; test <= T; test++) {
    int m; cin >> n >> m;
    memset(adj, 0, sizeof(adj));
    memset(nadj, 0, sizeof(nadj));
    for (int e = 0; e < m; e++) {
      int i, j; char c;
      cin >> i >> c >> j;
      adj[i][j] = adj[j][i] = 1;
      adjlist[i][nadj[i]++] = j;
      adjlist[j][nadj[j]++] = i;
    }
    for (int i = 0; i < n; i++) adj[i][i] = 1;
    vector <int> dists0 = bfs(0);
    vector <int> dists1 = bfs(1);
    int d = dists0[1];
    for (int i = 0; i < n; i++)
      if (dists0[i]+dists1[i] != d)
	dists0[i] = -1;
    
    memset(best[0], 0, sizeof(best[0]));
    best[0][0][0] = 1; // self
    for (int i = 1; i < n; i++)
      if (adj[0][i])
	best[0][0][0]++;

    int r = 0;
    for (int d0 = 1; d0 < d; d0++) {
      memset(best[1-r], 0, sizeof(best[1-r]));
      for (int i = 0; i < n; i++)
	for (int j = 0; j < n; j++)
	  if (best[r][i][j])
	    for (int k = 0; k < n; k++)
	      if (adj[j][k] && dists0[k] == d0) {
		int cur_score = best[r][i][j];
		for (int x = 0; x < nadj[k]; x++) {
		  int l = adjlist[k][x];
		  cur_score += !adj[i][l] && !adj[j][l];
		}
		if (cur_score > best[1-r][j][k])
		  best[1-r][j][k] = cur_score;
	      }
      r = 1-r;
    }
    int d2 = 0;
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
	d2 = max(d2, best[r][i][j]);

    printf("Case #%d: %d %d\n", test, d-1, d2-d);
  }
}
