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
    int N; scanf(" %d", &N);
    vector<int> C(N, -1);
    loop (i, N) {
      scanf(" %d", &C[i]);
    }

    int mx = -1;
    for (int i = 1; i < (1<<N) - 1; ++i) {
      int sean = 0, patrick = 0, sean_4_patrick = 0;
      for (int j = 0; j < N; ++j) {
        if (i & (1 << j)) {
          sean += C[j];
          sean_4_patrick ^= C[j];
        } else {
          patrick ^= C[j];
        }
      }

      if (patrick == sean_4_patrick && sean > mx) {
        mx = sean;
      }
    }
    
		printf("Case #%d: ", X);
    if (mx == -1) {
      printf("NO\n");
    } else {
      printf("%d\n", mx);
    }
	}
	return 0;
}
