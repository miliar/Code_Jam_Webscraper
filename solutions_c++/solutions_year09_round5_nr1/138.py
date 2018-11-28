#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;

typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;

int R, C;
vector<string> grid;

VI GetState(char ch) {
  VI ret;
  for (int r = 0; r < R; r++) {
    for (int c = 0; c < C; c++) {
      if (grid[r][c] == ch || grid[r][c] == 'w') {
	ret.push_back(r*C+c);
      }
    }
  }
  sort(ret.begin(), ret.end());
  return ret;
}

int ABS(int x) {
  if (x < 0) return -x;
  return x;
}

bool Dangerous(const VI &state) {
  if (state.size() == 1) return false;
  for (int i = 0; i < state.size(); i++) {
    bool dangerous = true;
    int ri = state[i] / C, ci = state[i] % C;
    for (int j = 0; dangerous && j < state.size(); j++) {
      if (i == j) continue;
      int rj = state[j] / C, cj = state[j] % C;
      if (ABS(ri - rj) + ABS(ci - cj) == 1) dangerous = false;
    }
    if (dangerous) return true;
  }
  return false;
}

int dr[] = {0, 1, 0, -1};
int dc[] = {1, 0, -1, 0};

void Print(const VI &x) {
  for (int i = 0; i < x.size(); i++) {
    cerr << "(" << x[i] / C << "," << x[i] % C << ")";
  }
  cerr << endl;
}

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    cin >> R >> C;
    grid.resize(R);
    for (int i = 0; i < R; i++)
      cin >> grid[i];

    VI start = GetState('o');
    VI end = GetState('x');    

    cout << "Case #" << (t+1) << ": ";

    //Print(start);
    //Print(end);

    queue<pair<int, VI> > Q;
    set<VI> seen;
    Q.push(make_pair(0, start));
    seen.insert(start);
    
    bool found = false;
    while (!Q.empty()) {
      int steps = Q.front().first;
      VI q = Q.front().second;
      Q.pop();

      if (q == end) {
	cout << steps << endl;
	found = true;
	break;
      }
      
      bool was_dangerous = Dangerous(q);
      //cerr << "Current state (" << was_dangerous << "): " << steps << ", "; Print(q);

      for (int i = 0; i < q.size(); i++) {
	int r = q[i] / C;
	int c = q[i] % C;

	for (int d = 0; d < 4; d++) {
	  VI qq(q);
	  int nr = r + dr[d];
	  int nc = c + dc[d];
	  qq[i] = nr * C + nc;
	  int nnr = r - dr[d];
	  int nnc = c - dc[d];
	  
	  //cerr << "Considering: "; Print(qq);

	  if (nr < 0 || nc < 0 || nr >= R || nc >= C) continue;
	  if (nnr < 0 || nnc < 0 || nnr >= R || nnc >= C) continue;
	  if (grid[nr][nc] == '#') continue;
	  if (grid[nnr][nnc] == '#') continue;
	  bool overlap = false;
	  for (int j = 0; !overlap && j < q.size(); j++) {
	    if (j == i) continue;
	    if (q[j] == nr * C + nc) overlap = true;
	    if (q[j] == nnr * C + nnc) overlap = true;
	  }
	  if (overlap) continue;
	  if (was_dangerous) {
	    if (Dangerous(qq)) continue;
	  }

	  sort(qq.begin(), qq.end());
	  if (seen.find(qq) != seen.end()) continue;
	  seen.insert(qq);

	  Q.push(make_pair(steps + 1, qq));
	}
      }
    }

    if (!found) {
      cout << -1 << endl;
    }

  }
}
