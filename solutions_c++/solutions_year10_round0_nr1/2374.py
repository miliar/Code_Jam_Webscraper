
/**
 *
 *  Time-stamp:<2010/05/08 09:10:00>
 **/

#include <functional>
#include <algorithm>
#include <iostream>
#include <complex>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <cctype>
#include <queue>
#include <cmath>
#include <set>
#include <map>
using namespace std;

#define For(i, s, n) for(int i = (int)(s); i < (int)(n); ++i)
#define rep(i, n) For(i, 0, n)
#define iter(c) __typeof((c).begin())
#define each(c, i) for(iter(c) i = (c).begin(); i != (c).end(); ++i)
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define mp make_pair

int main()
{
  int t, n, k;

  cin >> t;
  rep(cnt, t) {
    bool res = true;
    cin >> n >> k;

    if(k == 0) res = false;
    else if(n == 1) res = (k % 2 == 1) ? true : false;
    else {
      for(int i = 0; i < n; ++i) k -= pow(2.0, i);
      if(k < 0) res = false;
      else if(k != 0 and (k % (int)pow(2.0, n)) ) res = false;
    }

    cout << "Case #" << cnt+1 << ": ";
    if(res) cout << "ON" << endl;
    else    cout << "OFF" << endl;
  }


  return 0;
}


