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

int main() {
  // COUNTER CODE STARTS HERE

  int cases, i;

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

int N, K, B, T;
long X[105], V[105], F[105], S[105];

void _main() {
  cin >> N >> K >> B >> T;

  int i, j, k;

  For (i, N) { cin >> X[i]; }
  For (i, N) { cin >> V[i]; }
  For (i, N-1) For (j, N-2-i) {
    if (X[j] == X[j+1] && V[j] < V[j+1]) {
      long t = V[j]; V[j] = V[j+1]; V[j+1] = t;
    }
  }

  For (i, N) { F[i] = X[i] + T * V[i]; }

  j = k = 0;
  i = N-1;
  Clear(S);

  while (i >= 0 && K > 0) {
    if (F[i] >= B) {
      K--;
    } else {
      j++;
    }
    i--;
  }

  if (K > 0) { cout << "IMPOSSIBLE"; return; }

  j = i+1;
  for (i=j; i<N; i++) {
    S[i] = S[i-1];
    if (F[i] >= B) {
      S[i]++;
    }
  }

  k = 0;
  for (i=j; i<N; i++) {
    if (F[i] < B) {
      k += S[i];
    }
  }

  cout << k;
}
