#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <string>
#include <set>
#include <vector>
#include <utility>

#define r first
#define c second

#define MAXR 55
#define MAXC 55

using namespace std;

namespace {

  char a[MAXR][MAXC];
  int R, C, r, c;

  typedef pair<int, int> Point;
  
  const Point dp[] = { Point(-1, 0), Point(0, -1), Point(0, 1), Point(1, 0),
		      Point(1, 1)};

  Point operator+(const Point& a, const Point& b) {
    return Point(a.r + b.r, a.c + b.c);
  }

  bool valid(const Point& p) {
    return p.r >= 0 && p.r < R && p.c >= 0 && p.c < C;
  }

  char at(const Point& p) {
      if (valid(p))
	return a[p.r][p.c];
      return '.';
  }

    bool isCorner(const Point& p) {
      return at(p + dp[0]) != '#' && at(p + dp[1]) != '#' && at(p) == '#' &&
	at(p + dp[2]) == '#' && at(p + dp[3]) == '#' && at(p + dp[4]) == '#';
    }

    void fillCorner(const Point& p) {
      a[p.r][p.c] = a[p.r + 1][p.c + 1] = '/';
      a[p.r + 1][p.c] = a[p.r][p.c + 1] = '\\';
    }


  void print() {
    for (int i = 0; i < R; ++i)
      printf("%s\n", a[i]);
  }

  bool isAllFilled() {
    for (int r = 0; r < R; ++r)
      for (int c = 0; c < C; ++c)
	if (a[r][c] == '#')
	  return false;
    return true;
  }

  bool fillOne() {
    for (int r = 0; r < R - 1; ++r)
      for (int c = 0; c < C - 1; ++c) {
	Point p(r, c);
	if (isCorner(p)) {
	  fillCorner(p);
	  return true;
	}
      }
    return false;
  }


  void input() {
    scanf("%d%d", &R, &C);
    for (int i = 0; i < R; ++i)
      scanf("%s", a[i]);
    
  }

  void solve(int test_case) {
    input();

    while (fillOne()) {
      //print();
    }

    if (isAllFilled()) {
      printf("Case #%d:\n", test_case);
      print();
    }
    else {
      printf("Case #%d:\nImpossible\n", test_case);
    }
  }
}

int main() {
  int n_tc; scanf("%d", &n_tc);
  for (int i = 1; i <= n_tc; ++i)
    solve(i);
  return 0;
}
