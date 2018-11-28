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

  int i, N;
  cin >> N;

  for (i=1; i<=N; ++i) {
    cout << "Case #" << i << ": ";
    _main();
    cout << endl;
  }

  // COUNTER CODE ENDS HERE

  return 0;
}

// ACTUAL CODE STARTS BELOW

void _main() {
  ull N, D, G;

  cin >> N >> D >> G;

  if ( (D < 100 && G == 100) || (D > 0 && G == 0)) {
    cout << "Broken"; return;
  }

  if (N >= 100) {
    cout << "Possible"; return;
  }

  ull i;

  for (i=1; i<=N; ++i) {
    if ( i*D%100 == 0) {
      cout << "Possible"; return;
    }
  }

  cout << "Broken";
}
