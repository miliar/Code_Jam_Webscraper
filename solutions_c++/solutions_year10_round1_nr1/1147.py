#include "precompiled.h"
#include <boost/lexical_cast.hpp>


enum {
  R = 1,
  B = 2
};


int search_impl(vector<string>const & v, int x, int dx, int y, int dy, int n);

int search_entirely(vector<string> const & v, int n) {
  int res = 0;
  for (int i = 0; i < v.size(); ++i) {
    for (int j = 0; j < v.size(); ++j) {
      if (v[i][j] != '.') {
	res |= search_impl(v, i, 1, j, -1, n);
	res |= search_impl(v, i, 1, j, 0, n);
	res |= search_impl(v, i, 1, j, 1, n);
	res |= search_impl(v, i, 0, j, 1, n);
      }
    }
  }
  return res;
}


int search_impl(vector<string> const & v, int x, int dx, int y, int dy, int n) {
  if (n == 1) {
    if (v[x][y] == 'R') {
      return R;
    } else if (v[x][y] == 'B') {
      return B;
    } else {
      assert(0);
    }
  }

  if (x+dx < 0 || y+dy < 0 || x+dx >= v.size() || y+dy >= v.size() ||
      v[x][y] != v[x+dx][y+dy])
  {
    return 0;
  }

  return search_impl(v, x+dx, dx, y+dy, dy, n-1);
}



vector<string> rotate(vector<string> const & v) {
  int n = v.size();
  vector<string> newv(n, string(n, '.'));
  for (int i = 0; i < n; ++i) {
    string buf;
    for (int j = 0; j < n; ++j) {
      if (v[i][j] != '.') {
	buf.push_back(v[i][j]);
      }
    }

    for (int j = 0; j < buf.size(); ++j) {
      newv[n-1-j][n-1-i] = buf[buf.size() - j - 1];
    }
  }

  return newv;

}



int main() {
  string buf;
  getline(cin, buf);
  stringstream ss(buf);
  int T;
  ss >> T;

  for (int i = 0; i < T; ++i) {
    getline(cin, buf);
    stringstream ss(buf);
    int N, K;
    ss >> N >> K;

    vector<string> board;
    for (int j = 0; j < N; ++j) {
      getline(cin, buf);
      board.push_back(buf);
    }

    board = rotate(board);
    
    cout << "Case #" << i+1 << ": ";
    switch (search_entirely(board, K)) {
    case 0:
      cout << "Neither\n";
      break;
    case 1:
      cout << "Red\n";
      break;
    case 2:
      cout << "Blue\n";
      break;
    default:
      cout << "Both\n";
      break;
    }



  }

}
