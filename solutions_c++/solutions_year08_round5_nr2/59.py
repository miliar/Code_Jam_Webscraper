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
#include <ext/hash_map>
#include <ext/hash_set>
#include <limits>

using namespace std;

using namespace __gnu_cxx;



int mv[4][2] = {
  {-1,0},
  {0,1},
  {1,0},
  {0,-1}
};
int n,m;

bool inside (int x, int y) {
  return x>=0 && x < n && y>=0 && y < m;
}

struct state {
  int x;
  int y;
  int p1x;
  int p1y;
  int p2x;
  int p2y;
  state (int x,int y, int p1x=-1, int p1y=-1, int p2x=-1, int p2y=-1) 
    :x (x), y (y), p1x (p1x),p1y (p1y), p2x (p2x), p2y (p2y) {}
  // state (state rhs) 
  //   : x (rhs.x
  bool operator<(const state& rhs) const {
    return make_pair (make_pair (x,y), make_pair (make_pair (p1x,p1y),
                                                  make_pair (p2x,p2y)))
      <
      make_pair (make_pair (rhs.x,rhs.y), make_pair (make_pair (rhs.p1x,rhs.p1y),
                                                     make_pair (rhs.p2x,rhs.p2y)));
  }
  bool operator==(const state& rhs) const {
    return x == rhs.x &&
      y == rhs.y &&
      p1x == rhs.p1x &&
      p1y == rhs.p1y &&
      p2x == rhs.p2x &&
      p2y == rhs.p2y;
  }
  
      
};

namespace __gnu_cxx {

  template<> struct hash<state>
  { size_t operator()(const state& __x) const { return __x.x + 23* __x.y + 23*23*__x.p1x + 23*23*23*__x.p1y +  47*__x.p2x + 59*__x.p2y;
  }
  };
  
}


int main() {
  int num_cases ;
  cin >> num_cases;
  for (int case_num = 1; case_num <= num_cases; ++case_num) {
    cout << "Case #" << case_num << ": ";
    cin >> n >> m;
    vector<string> board (n);
    int sx=-1,sy=-1;
    int cx=-1,cy=-1;
    for (int i = 0; i < n; ++i) {
      cin >> board[i];
      for (int j = 0; j < m; ++j) {
        if (board[i][j] == 'O') {
          board[i][j] = '.';
          sx = i;
          sy = j;
        }
        if (board[i][j] == 'X') {
          board[i][j] = '.';
          cx=i;
          cy=j;
        }
      }
    }
    // cerr << sx << " " << sy << "\n";
    hash_map<state,int> dist;
    state start (sx,sy);
    dist[start] = 0;
    queue<state> q;
    q.push (start);
    int best_dist = numeric_limits<int>::max();
    
    while (!q.empty()) {
      state curr = q.front();
      q.pop();
      int cdist = dist[curr];
      if (cdist >= best_dist) continue;
      if (curr.x == cx && curr.y == cy) 
        best_dist = min (best_dist, cdist);
        
      // try to use tele

      if(curr.p1x != -1 && curr.p2x != -1) {
        if (curr.x == curr.p1x && curr.y == curr.p1y) {
          state new_state = curr;
          new_state.x = curr.p2x;
          new_state.y = curr.p2y;
          if (dist.find (new_state) == dist.end() ||
              dist[new_state] > cdist + 1) {
            dist[new_state] = cdist + 1;
            q.push (new_state);
          }
        }
        if (curr.x == curr.p2x && curr.y == curr.p2y) {
          state new_state = curr;
          new_state.x = curr.p1x;
          new_state.y = curr.p1y;
          if (dist.find (new_state) == dist.end() ||
              dist[new_state] > cdist + 1) {
            dist[new_state] = cdist + 1;
            q.push (new_state);
          }
        }
      }
      
      
      // shoot 
      for (int i = 0; i < 4; ++i) {
        int px = curr.x;
        int py = curr.y;
        int nx = px + mv[i][0];
        int ny = py + mv[i][1];
        while (inside (nx,ny) && board[nx][ny] == '.') {
          px = nx;
          py = ny;
          nx = px + mv[i][0];
          ny = py + mv[i][1];
        }
        state new_state (curr.x,curr.y, px,py, curr.p2x, curr.p2y);
        if (dist.find (new_state) == dist.end() ||
            dist[new_state] > cdist) {
          dist[new_state] = cdist;
          q.push (new_state);
        }
        new_state = state (curr.x,curr.y, curr.p1x, curr.p1y, px,py);
        if (dist.find (new_state) == dist.end() ||
            dist[new_state] > cdist) {
          dist[new_state] = cdist;
          q.push (new_state);
        }
      }
      // move
      for (int i = 0; i < 4; ++i) {
        int nx = curr.x + mv[i][0];
        int ny = curr.y + mv[i][1];
        if (inside (nx,ny) && board[nx][ny] == '.') {
          state new_state = curr;
          new_state.x = nx;
          new_state.y = ny;
          if (dist.find (new_state) == dist.end() ||
              dist[new_state] > cdist + 1) {
            dist[new_state] = cdist + 1;
            q.push (new_state);
          }
        }
      }
    }
    if (best_dist == numeric_limits<int>::max()) {
      cout << "THE CAKE IS A LIE\n";
    } else {
      cout << best_dist << "\n";
    }
    
  }
}

