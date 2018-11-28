#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long long int LL;

int f (LL a, LL b, LL r, LL aa, LL bb) {
  if (aa==a && bb==b) return 0;
  if (a*r >= b) return 0;
  LL m = (LL)floor(sqrt(double(a*b)));
  return 1+min(max(f(a,m,r,a,b),f(m,b,r,a,b)),
	       max(f(a,m+1,r,a,b),f(m+1,b,r,a,b))
	     );
}

int main () {
  int T; cin >> T;
  for (int C = 0; C < T; ++C) {
    LL a,b,r; cin >> a >> b >> r;
    cout << "Case #" << C+1 << ": " << f(a,b,r,a-1, b+1) << endl;
  }

}

