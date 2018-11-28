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

  int c;

  cin >> c;

  for (int i=1; i<=c; i++) {
    cout << "Case #" << i << ": ";
    _main();
    cout << endl;
  }

  // COUNTER CODE ENDS HERE

  return 0;
}

// ACTUAL CODE STARTS BELOW
ull gcd(ull a, ull b) {
  ull c;

  while (b) {
    c = a%b;
    a = b;
    b = c;
  }

  return a;
}

void _main() {
  int i, j, n;
  ull t[1000], d[1000];

  cin >> n;
  for (i=0; i<n; i++) scanf("%qu", &t[i]);
  sort(t, t+n);
  for (i=0; i<n-1; i++) {
    d[i] = t[i+1] - t[i];
  }

  n--;

  ull m = d[0];

  for (i=1; i<n; i++) {
    m = gcd(m, d[i]);
  }

  db_arrM(t, n+1);
  db_arrM(d, n);
  db(m);

  cout << (m-(t[0]%m))%m;

}
