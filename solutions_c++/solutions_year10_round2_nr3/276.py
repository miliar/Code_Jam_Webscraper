// In Brother Chun we trust...
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

#define _DEBUG_MODE_

#ifdef _DEBUG_MODE_
#define db(X) cerr << "* DEBUG [L" << __LINE__ << "]: " << #X << " = " << X << endl;
#define db_arr(X) cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=0; __i__<sizeof(X)/sizeof(X[0]); __i__++) cerr << X[__i__] << " "; cerr << endl;
#define db_arrM(X, M) cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=0; __i__<M; __i__++) cerr << X[__i__] << " "; cerr << endl;
#define db_arrMN(X, M, N) cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=M; __i__<N; __i__++) cerr << X[__i__] << " "; cerr << endl;
#else
#define db(X)
#define db_arr(X)
#define db_arrM(X, M)
#define db_arrMN(X, M, N)
#endif

#define For(i, n) for(i=0;i<(n);i++)
#define ForL(i, m, n) for(i=(m);i<(n);i++)

#define Clear(X) memset( (X), 0, sizeof( (X) ) )
#define Fill(X) memset( (X), -1, sizeof( (X) ) )

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef unsigned long ulong;

void _main();
void precalc();
ulong v[1000];
ulong dp[1000][1000];

int main() {
  // COUNTER CODE STARTS HERE

  int cases, i;

  precalc();

  cin >> cases;

  For (i, cases) {
    printf("Case #%d: ", i+1);
    _main();
    cout << endl;
  }

  // COUNTER CODE ENDS HERE

  return 0;
}

// ACTUAL CODE STARTS BELOW
ulong ncr[1000][1000];

void precalc() {
  Clear(dp); Clear(v); Clear(ncr);

  long i, j, k, maxp, p, t;

  For (i, 501) ncr[i][0] = 1;
  for (i=1; i<501; i++) {
    for (j=1; j<=i; j++) {
      ncr[i][j] = (ncr[i-1][j-1] + ncr[i-1][j]) % 100003;
    }
  }

  ForL (i, 2, 501) {
    dp[i][1] = 1;
  }

  for (i=3; i<501; i++) {
    maxp = i-1;

    for (p=2; p<=maxp; p++) { // i @ pos p
      t = 0;

      for (j=1; j<p; j++) {
	t = (t + dp[p][j] * ncr[i-p-1][p-j-1]) % 100003;
      }
      dp[i][p] = t;
    }
  }

  ForL (i, 2, 501) {
    ForL (j, 1, i) {
      v[i] = (v[i] + dp[i][j]) % 100003;
    }
  }
}

void _main() {
  int n;
  cin >> n;
  cout << v[n];
}
