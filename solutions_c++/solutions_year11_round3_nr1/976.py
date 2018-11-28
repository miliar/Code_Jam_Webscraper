#include <iostream>
#include <cstdio>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <functional>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <string>
#include <sstream>
#include <fstream>
#include <complex>
#include <iterator>
#include <memory>
#include <utility>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define rep(i,s,n) for(int i=s;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define MP(a, b) make_pair((a), (b))
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long double ld;
typedef long long ll;

int T, R, C;
char pic[55][55];

const char red[2][2] = {
  {'/', '\\'},
  {'\\', '/'}
};

ll gcd(ll a, ll b) {
  return a == 0 ? b : gcd(b % a, a);
}

bool IsValid(int r, int c) {
  return (r >= 0) && (r < R) && (c >= 0) && (c < C);
}

bool IsAbleToReplace(int r, int c) {
  for (int rr = 0; rr < 2; ++rr) {
    for (int cc = 0; cc < 2; ++cc) {
      if (!IsValid(r+rr, c+cc)) return false;
      if (pic[r+rr][c+cc] != '#') return false;
    }
  }
  return true;
}

bool IsPossible() {
  for (int r = 0; r < R; ++r) {
    for (int c = 0; c < C; ++c) {
      if (pic[r][c] == '#') return false;
    }
  }
  return true;
}

void PrintPic() {
  for (int r = 0; r < R; ++r) {
    printf("%s\n", pic[r]);
  }
}

int main() {
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> R >> C;

    for (int r = 0; r < R; ++r) {
      scanf("%s", pic[r]);
    }

    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c) {
	if (pic[r][c] == '#') {
	  if (IsAbleToReplace(r, c)) {
	    for (int rr = 0; rr < 2; ++rr) {
	      for (int cc = 0; cc < 2; ++cc) {
		pic[r+rr][c+cc] = red[rr][cc];
	      }
	    }
	  }
	}
      }
    }

    if (IsPossible()) {
      printf("Case #%d:\n", t);
      PrintPic();
    } else {
      printf("Case #%d:\nImpossible\n", t);
    }
  }
}
