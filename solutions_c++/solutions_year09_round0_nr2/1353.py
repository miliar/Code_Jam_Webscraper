#include <iostream>
#include <map>
#include <queue>
#include <cstring>
using namespace std;

const int dr[] = {-1, 0, 0, 1};
const int dc[] = {0, -1, 1, 0};
int d[200][200], ans[200][200], nr, nc;

bool issink(int r, int c) {
  for (int k = 0; k < 4; ++k) {
    int rr = r+dr[k], cc = c+dc[k];
    if (rr >= 0 && rr < nr && cc >= 0 && cc < nc &&
	d[rr][cc] < d[r][c])
      return false;
  }
  return true;
}

bool flows(int sr, int sc, int tr, int tc) {
  if (d[sr][sc] <= d[tr][tc])
    return false;
  
  int bk = -1, mn = 1000000000;
  for (int k = 0; k < 4; ++k) {
    int rr = sr+dr[k], cc = sc+dc[k];
    if (rr >= 0 && rr < nr && cc >= 0 && cc < nc &&
	d[rr][cc] < mn)
      bk = k, mn = d[rr][cc];
  }

  return (sr+dr[bk] == tr && sc+dc[bk] == tc);
}

int main() {
  int n;
  cin >> n;
  for (int C = 1; C <= n; ++C) {
    cin >> nr >> nc;
    for (int i = 0; i < nr; ++i)
      for (int j = 0; j < nc; ++j)
	cin >> d[i][j];

    memset(ans, 0, sizeof ans);

    int cur = 1;
    for (int i = 0; i < nr; ++i)
      for (int j = 0; j < nc; ++j)
	if (!ans[i][j] && issink(i, j)) {
	  queue<int> q;
	  q.push(i), q.push(j);
	  while (q.size()) {
	    int r = q.front(); q.pop();
	    int c = q.front(); q.pop();
	    
	    ans[r][c] = cur;
	    
	    for (int k = 0; k < 4; ++k) {
	      int rr = r+dr[k], cc = c+dc[k];
	      if (rr >= 0 && rr < nr && cc >= 0 && cc < nc &&
		  flows(rr, cc, r, c))
		q.push(rr), q.push(cc);
	    }
	  }
	  ++cur;
	}

    cout << "Case #" << C << ": " << endl;
    map<int, char> mm;
    char nextc = 'a';
    for (int i = 0; i < nr; ++i, cout << endl)
      for (int j = 0; j < nc; ++j) {
	if (mm.find(ans[i][j]) == mm.end())
	  mm[ans[i][j]] = nextc++;
	cout << (j ? " " : "") << mm[ans[i][j]];
      }
  }
}
