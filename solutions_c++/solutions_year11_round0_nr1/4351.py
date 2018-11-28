/* Rajat Goel (C++) */
#include <algorithm>
#include <iostream>
#include <iterator>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <list>
#include <map>
#include <set>
using namespace std;
typedef pair<int,int>  pii;
typedef long long      LL;
typedef long double    LD;
const int  INF  =      INT_MAX / 2 - 1;
const LL   LINF =      LLONG_MAX / 2 - 1;
const LD   EPS  =      1e-7;
#define loop(i, n)     for (int i = 0; i < int(n); ++i)
#define foreach(i, a)  for (typeof((a).begin()) i = (a).begin();i != (a).end(); ++i)
template<typename T>
inline int fCMP(T x, T y = 0, T tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int main(int argc, char *argv[]) {
	int T; scanf(" %d", &T);
	for (int X = 1; X <= T; ++X) {
    int n; scanf(" %d", &n);
    int o_pos = 1, b_pos = 1;
    list<int> o_mark, b_mark;
    vector<char> next(n, ' ');

    loop (i, n) {
      char ch; int p;
      scanf(" %c %d\n", &ch, &p);

      next[i] = ch;
      ch == 'O' ? o_mark.push_back(p) : b_mark.push_back(p);
    }

    int indx = 0, step = 0;
    while (!o_mark.empty() || !b_mark.empty()) {
      bool o_moved = false, b_moved = false;

      if (!o_mark.empty()) {
        if (o_pos < *o_mark.begin()) {
          ++o_pos; o_moved = true;
        } else if (o_pos > *o_mark.begin()) {
          --o_pos; o_moved = true;
        }
      }

      if (!b_mark.empty()) {
        if (b_pos < *b_mark.begin()) {
          ++b_pos; b_moved = true;
        } else if (b_pos > *b_mark.begin()) {
          --b_pos; b_moved = true;
        }
      }

      if (next[indx] == 'O') {
        if (!o_moved && o_pos == *o_mark.begin()) {
          ++indx;
          o_mark.erase(o_mark.begin());
        }
      } else {
        if (!b_moved && b_pos == *b_mark.begin()) {
          ++indx;
          b_mark.erase(b_mark.begin());
        }
      }

      ++step;
    }

		printf("Case #%d: %d\n", X, step);
	}
	return 0;
}
