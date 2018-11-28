#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <utility>
#include <string>
#include <queue>
#include <map>
#include <bitset>
#include <climits>

#ifdef _DEBUG_MODE_
#define db(X) { cerr << "* DEBUG [L" << __LINE__ << "]: " << #X << " = " << X << endl; }
#define db_arr(X) { cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=0; __i__<sizeof(X)/sizeof(X[0]); ++__i__) cerr << X[__i__] << " "; cerr << endl; }
#define db_arrM(X, M) { cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=0; __i__<M; ++__i__) cerr << X[__i__] << " "; cerr << endl; }
#define db_arrMN(X, M, N) { cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=M; __i__<N; ++__i__) cerr << X[__i__] << " "; cerr << endl; }
#else
#define db(X)
#define db_arr(X)
#define db_arrM(X, M)
#define db_arrMN(X, M, N)
#endif

#define For(i, n) for(i=0;i<(n);++i)
#define ForL(i, m, n) for(i=(m);i<(n);++i)

#define Clear(X) memset( (X), 0, sizeof( (X) ) )
#define Fill(X) memset( (X), -1, sizeof( (X) ) )

#define ArraySize(X) (sizeof(X)/sizeof(X[0]))

template <typename T> void xchg(T &a, T &b) { T c=a; a=b; b=c; }

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef unsigned long ulong;

void _main();

int main() {
  // COUNTER CODE STARTS HERE
  int i, T;
  cin >> T;
  
  For (i, T) {
    printf("Case #%d: ", i+1);
    _main();
    putchar('\n');
  }

  // COUNTER CODE ENDS HERE

  return 0;
}

// ACTUAL CODE STARTS BELOW
int t[100][3];
int T[100];

inline bool cmp(register int i, register int j) {
  return j < i;
}

void _main() {
  int i, j, n, s, p;
  Clear(t); Clear(T);

  cin >> n >> s >> p;

  For (i, n) {
    cin >> T[i];
  }

  sort(T, T+n, cmp);

  For (i, n) {
    t[i][0] = t[i][1] = t[i][2] = T[i] / 3;
    j = T[i] % 3;

    switch (j) {
    case 2:
      ++t[i][1];
    case 1:
      ++t[i][0];
    case 0:
      break;
    }

    T[i] = j;
  }

  for (i=0; s && i < n; ++i) {
    if (T[i] == 0 && t[i][0] == p-1 && t[i][2] > 0) {
      --s;
      --t[i][2];
      ++t[i][0];
    }

    if (T[i] == 2 && t[i][0] == p-1 && t[i][1] > 0) {
      --s;
      --t[i][1];
      ++t[i][0];
    }
  }

  j = 0;

  For (i, n) {
    if (t[i][0] >= p) ++j;
  }

  cout << j;
}
