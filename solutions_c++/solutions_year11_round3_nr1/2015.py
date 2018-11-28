#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <stack>
#include <list>
#include <deque>
#include <queue>
#include <sstream>
#include <map>
#include <set>

#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <climits>

using namespace std;

#define FOR(i,s,n) for (int i = (int)(s); i < (int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define MP make_pair
#define PB push_back

#define cerr if (0) cerr

inline
bool inside(const vector<string>& pic, int r, int c)
{
  return r >= 0 && c >= 0 && r < pic.size() && c < pic[0].size();
}

inline
bool canputat(const vector<string>& pic, int row, int col)
{
  const int dr[] = {0, 1, 1};
  const int dc[] = {1, 0, 1};
  REP(i, 3) {
    int nr = row + dr[i];
    int nc = col + dc[i];
    if (inside(pic, nr, nc)) {
      if (pic[nr][nc] != '#')
	return false;
    } else {
      return false;
    }
  }
  return true;
}

inline
bool noroom(const vector<string>& pic)
{
  const int R = pic.size();
  const int C = pic[0].size();

  REP(r, R) REP(c, C) {
    if (pic[r][c] == '#') {
      if (canputat(pic, r, c))
	return false;
    }
  }

  return true;
}

inline
bool finished(const vector<string>& pic)
{
  const int R = pic.size();
  const int C = pic[0].size();
  REP(r, R) REP(c, C) {
    if (pic[r][c] == '#') {
      return false;
    }
  }

  return true;
}

void putredtile(vector<string>& pic, int row, int col)
{
  pic[row  ][col  ] = '/';
  pic[row  ][col+1] = '\\';
  pic[row+1][col  ] = '\\';
  pic[row+1][col+1] = '/';
}

void removeredtile(vector<string>& pic, int row, int col)
{
  pic[row  ][col  ] = '#';
  pic[row  ][col+1] = '#';
  pic[row+1][col  ] = '#';
  pic[row+1][col+1] = '#';
}

void showpic(vector<string>& pic)
{
  const int R = pic.size();
  //const int C = pic[0].size();
  REP(r, R) cerr << pic[r] << endl;
}

bool dfs(vector<string>& pic, int row, int col)
{
  cerr << "try at (" << row << ", " << col << ")" << endl;
  showpic(pic);

  if (noroom(pic)) {
    if (finished(pic))
      return true;
    return false;
  }

  if (canputat(pic, row, col)) {
    cerr << "put at (" << row << ", " << col << ")" << endl;
    putredtile(pic, row, col);
    if (dfs(pic, row, col+2))
      return true;
    removeredtile(pic, row, col);
  } else {
    const int R = pic.size();
    const int C = pic[0].size();
    FOR(r, row, R) {
      FOR(c, r == row ? col+1 : 0, C) {
	if (pic[r][c] != '#') continue;
	if (dfs(pic, r, c))
	  return true;
      }
    }
  }

  return false;
}


int main()
{
  int T, R, C;

  cin >> T;

  REP(tc, T) {
    cin >> R >> C;
    
    vector<string> pic(R);
    REP(i, R) cin >> pic[i];
    
    int row = -1, col = -1;
    REP(i, R) REP(j, C) {
      if (row < 0 && pic[i][j] == '#') {
	row = i;
	col = j;
      }
    }

    bool ans;
    if (row < 0)
      ans = true;
    else
      ans = dfs(pic, row, col);
    
    cout << "Case #" << tc+1 << ":" << endl;
    if (ans) {
      REP(i, R) {
	cout << pic[i] << endl;
      }
    } else {
      cout << "Impossible" << endl;
    }
      
  }

  return 0;
}
