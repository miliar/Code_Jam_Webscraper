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

int p10[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};

inline int digits(register int n) {
  register int r = 0;

  while (n) {
    ++r;
    n /= 10;
  }

  return r;
}

inline int minPerm(register int v) {
  register int min = v, n, d;
  n = d = digits(v)-1;
  while (n--) {
    v = (v%10)*p10[d] + v/10;
    if (v >= p10[d] && v < min) min = v;
  }

  return min;
}

int mp[2000001];

void init() {
  register int i;

  ForL (i, 1, 2000001) {
    mp[i] = minPerm(i);
  }
}

int main() {
  // COUNTER CODE STARTS HERE
  init();

  int T, i;
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

int A, B;
int C[2000001];

inline ll sum(register int n) {
  if (n <= 1) return 0;
  return (n*(n-1)) >> 1;
}

void _main() {
  cin >> A >> B;
  Clear(C);

  register int i;
  ll c = 0;

  for (i = A; i <= B; ++i) {
    ++C[mp[i]];
  }

  for (i = 0; i < 2000001; ++i) {
    c += sum(C[i]);
  }

  cout << c;
}
