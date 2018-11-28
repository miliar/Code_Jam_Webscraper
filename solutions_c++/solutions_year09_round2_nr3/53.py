#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string> 
#include <vector>
#include <stack>
#include <stdexcept>

using namespace std;

int gx[] = {-1,0,1,0};
int gy[] = {0,1,0,-1};
int n;
bool inside (int x, int y) {
  return x>=0&&x<n&&y>=0&&y<n;
}


struct state {
  int x;
  int y;
  int val;
  string expr;
};


string solve (vector<string>& board, int query) {
  vector<vector<map<int,string> > > seen_values (n,vector<map<int,string> >(n));
  queue<state> q;
  string best_sol;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (isdigit (board[i][j])) {
        state new_state;
        new_state.x = i;
        new_state.y = j;
        new_state.val = board[i][j]-'0';
        new_state.expr = board[i][j];
        if (new_state.val == query) {
          return new_state.expr;
        }
        q.push (new_state);
        seen_values[i][j][new_state.val] = new_state.expr;
      }
    }
  }
  while (!q.empty()) {
    state curr = q.front();
    q.pop();
    if (!best_sol.empty() && curr.expr.size() >= best_sol.size()) continue;

    for (int i = 0; i < 4; ++i) {
      int nx = curr.x + gx[i];
      int ny = curr.y + gy[i];
      if (!inside (nx,ny)) continue;
      for (int j = 0;j < 4; ++j) {
        int nnx = nx + gx[j];
        int nny = ny + gy[j];
        if (!inside (nnx,nny)) continue;
        state new_state;
        new_state.x = nnx;
        new_state.y = nny;
        new_state.val = curr.val + (board[nx][ny] == '+' ? (board[nnx][nny]-'0') : -(board[nnx][nny]-'0'));
        new_state.expr = curr.expr + board[nx][ny] + board[nnx][nny];

        if (new_state.val == query && (best_sol.empty() || best_sol.size() > new_state.expr.size() || (best_sol.size() >= new_state.expr.size() && best_sol > new_state.expr))) {
          best_sol = new_state.expr;
        }

        map<int,string>::iterator it = seen_values[nnx][nny].find (new_state.val);
        if (it == seen_values[nnx][nny].end() || it->second.size() > new_state.expr.size() || (it->second.size() >=new_state.expr.size() && it->second > new_state.expr)) {
          seen_values[nnx][nny][new_state.val] = new_state.expr;
          q.push (new_state);
        }
      }
    }
  }
  return best_sol;
}

int main() {
  int num_cases;
  cin >> num_cases;
  cin.ignore();
  
  for (int case_num = 1; case_num <=  num_cases; ++case_num) {
    cout << "Case #" << case_num << ":\n";

    int num_queries;
    cin >> n >> num_queries;
    cin.ignore();
    vector<string> board;
    for (int i = 0; i < n; ++i) {
      string line;
      cin >> line;
      board.push_back (line);
    }
    for (int i = 0; i < num_queries; ++i) {
      int query;
      cin >> query;
      cout << solve (board,query) << "\n";
      
    }
    
  }
  
}
