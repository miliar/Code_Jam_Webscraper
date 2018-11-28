#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int _a;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) (a).begin(), (a).end()

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;

inline ld sqr(ld a) {
  return a * a;
}

int main() {
  int tests;
  cin >> tests;
  FOT(t, 1, tests+1) {
    int n;
    cin >> n;
    vi x, y, r;
    FOR(i, n) {
      int a, b, c;
      cin >> a >> b >> c;
      x.pb(a); y.pb(b); r.pb(c);
    }
    ld mn = 0, mx = 1000000;
    //    FOR(i, n) mn = max(mn, ld(r[i]));
    //    mn *= 2;
    if(n >= 3) {
    while(mx - mn > 1e-7) {
      ld md = (mn + mx) / 2;
      //      cerr << t << ' ' << md << endl;
      bool good = false;
      for(int i = 0; i < n; i++)
	for(int j = i + 1; j < n; j++)
	  if(sqr(x[i]-x[j])+sqr(y[i]-y[j]) <= sqr(2*md-r[i]-r[j]))
	    good = true;
      if(good) mx = md;
      else mn = md;
    }
    }
    if(n <= 2) {
      mn = 0.00;
      FOR(i, n) mn = max(mn, ld(r[i]));
    }
    cout << "Case #" << t << ": " << mn << endl;
  }
  return 0;
}
