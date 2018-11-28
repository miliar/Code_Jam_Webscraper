#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
using namespace std;
int parent[16384];
int rank[16384];
int seen[16384];
int h[128][128];
int m, n;
int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

inline char tochar(int x) {
  return (char)('a' + x);
}

inline int toid(int x, int y) {
  return x * 128 + y;
}

void init() {
  for (int i = 0; i < 16384; ++i) {
    parent[i] = i;
    rank[i] = 0;
  }
}

int find(int x) {
  if (parent[x] == x) return x;
  return parent[x] = find(parent[x]);
}

void merge(int x, int y) {
  int xRoot = find(x);
  int yRoot = find(y);
  if (rank[xRoot] > rank[yRoot]) parent[yRoot] = xRoot;
  else if (rank[xRoot] < rank[yRoot]) parent[xRoot] = yRoot;
  else {
    parent[yRoot] = xRoot;
    ++rank[xRoot];
  }
}

int findDrain(int x, int y) {
  int bestx = -1, besty = -1;
  int curh = h[x][y];
  
  for (int d = 0; d < 4; ++d) {
    int newx = x + dx[d];
    int newy = y + dy[d];
    if (newx >= m || newy >= n || newx < 0 || newy < 0) continue;
    int newh = h[newx][newy];
    if (newh < curh) {
      bestx = newx;
      besty = newy;
      curh = newh;
    }
  }
  if (bestx == -1) return -1;
  return toid(bestx, besty);
}

int main() {
  int numcase;
  cin >> numcase;
  for (int ncase = 1; ncase <= numcase; ++ncase) {
    cin >> m >> n;
    for (int i = 0; i < m; ++i) for (int j = 0; j < n; ++j) cin >> h[i][j];
    init();
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
	int drainTo = findDrain(i, j);
	// cout << "findDrain(" << i << "," << j << ") = " << drainTo << endl;
	if (drainTo != -1) 
	  merge(drainTo, toid(i, j));
      }
    }

    cout << "Case #" << ncase << ":" << endl;
    int idx = 0;
    memset(seen, -1, sizeof(seen));
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
	int root = find(toid(i, j));
	// cout << "root of (" << i << ',' << j << ") = " << root << endl;
	if (seen[root] == -1) {
	  seen[root] = idx++;
	}
	if (j > 0) cout << ' ';
	cout << tochar(seen[root]);
      }
      cout << endl;
    }
  }
}
