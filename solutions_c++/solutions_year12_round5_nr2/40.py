#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <numeric>
#include <utility>

using namespace std;

char board[6016][6016];
int color[6016][6016];
int ncolors;
int moves_x[10000], moves_y[10000];
int S;
const int dx[] = {0, 1, 1, 0, -1, -1};
const int dy[] = {1, 1, 0, -1, -1, 0};

void bfs(void) {
  memset(color, -1, sizeof(color));
  ncolors = 0;
  for (int x = 1; x <= 2*S-1; x++)
    for (int y = 1; y <= 2*S-1; y++)
      if (1-S <= x-y && x-y <= S-1 && color[x][y] == -1) {
	queue < pair <int, int> > q;
	char board_xy = board[x][y];
	color[x][y] = ncolors;
	q.push(make_pair(x, y));
	while(!q.empty()) {
	  pair <int, int> p = q.front(); q.pop();
	  int cx = p.first, cy = p.second;
	  for (int k = 0; k < 6; k++) {
	    int nx = cx+dx[k], ny = cy+dy[k];
	    if (board[nx][ny] == board_xy && color[nx][ny] == -1) {
	      color[nx][ny] = ncolors;
	      q.push(make_pair(nx, ny));
	    }
	  }
	}
	ncolors++;
      }
}

void set_board(int nmoves) {
  for (int m = 0; m < nmoves; m++)
    board[moves_x[m]][moves_y[m]] = 1;
}

void unset_board(int nmoves) {
  for (int m = 0; m < nmoves; m++)
    board[moves_x[m]][moves_y[m]] = 0;
}

int check_done(int nmoves) {
  //cerr << "checking " << nmoves << endl;
  set_board(nmoves);

  bfs();

  int ans = 0;
  
  map < int, set <int> > color_to_edge, color_to_corner;
  set <int> bound_colors;

  int x = 1, y = 1;
  for (int k = 0; k < 6; k++)
    for (int i = 0; i < S-1; i++) {
      if (i == 0) { // corner
	if (board[x][y] == 1) {
	  color_to_corner[color[x][y]].insert(k);
	  //cerr << "color to corner " << x << "," << y << ": " << color[x][y] << " -> " << k << endl;
	}
      }
      else {
	if (board[x][y] == 1)
	  color_to_edge[color[x][y]].insert(k);
      }
      if (board[x][y] == 0)
	bound_colors.insert(color[x][y]);
      x += dx[k];
      y += dy[k];
    }
  
  for (__typeof(color_to_corner.begin()) it = color_to_corner.begin();
       it != color_to_corner.end(); it++) {
    if (it->second.size() >= 2) ans |= 1;
  }

  for (__typeof(color_to_edge.begin()) it = color_to_edge.begin(); it != color_to_edge.end();
       it++) {
    if (it->second.size() >= 3) ans |= 2;
  }
  
  for (int x = 1; x <= 2*S-1; x++)
    for (int y = 1; y <= 2*S-1; y++)
      if (1-S <= x-y && x-y <= S-1 && board[x][y] == 0 && !bound_colors.count(color[x][y]))
	ans |= 4;

  unset_board(nmoves);

  return ans;
}

void set_boundaries(void) {
  int x = 0, y = 0;
  for (int k = 0; k < 6; k++)
    for (int i = 0; i < S; i++) {
      board[x][y] = -1;
      x += dx[k];
      y += dy[k];
    }
}

int main(void) {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    memset(board, 0, sizeof(board));
    int M; cin >> S >> M;
    for (int m = 0; m < M; m++) {
      int x, y; cin >> x >> y;
      bool unfilled_nbr = false;
      for (int k = 0; k < 6; k++)
	if (!board[x+dx[k]][y+dy[k]])
	  unfilled_nbr = true;
      if (!unfilled_nbr) { // cancel the move
	x += dx[0];
	y += dy[0];
      }
      board[x][y] = 1;
      moves_x[m] = x;
      moves_y[m] = y;
    }
    unset_board(M);
    
    set_boundaries();

    int lo = 0, hi = M+1; // no connection after lo moves; connection after hi moves
    int ans_mask = 0;
    while (hi-lo > 1) {
      int mid = (lo+hi)/2;
      int mid_ans_mask = check_done(mid);
      if (mid_ans_mask) {
	hi = mid;
	ans_mask = mid_ans_mask;
      }
      else
	lo = mid;
    }
    if (hi == M+1) {
      printf("Case #%d: none\n", t);
    }
    else {
      string ans;
      if (ans_mask & 1) ans += "-bridge";
      if (ans_mask & 2) ans += "-fork";
      if (ans_mask & 4) ans += "-ring";
      printf("Case #%d: %s in move %d\n", t, ans.substr(1).c_str(), hi);
    }
  }
}
