#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <valarray>
#include <vector>
#include <ext/algorithm>
#include <ext/hash_map>
#include <ext/hash_set>
#include <ext/numeric>
using namespace std;
using namespace __gnu_cxx;
 
#define F(i,a,b)for(int i=a;i<b;++i)
#define rep(i,n)F(i,0,n)
#define all(a)a.begin(),a.end()
template<class T>vector<T>&operator<<(vector<T>& v,T t){v.push_back(t);return v;} 


int solve(long long c, int l, int t) {
  if (l * c >= t) return 0;
  long long _c = c;
  while (t/c+!!(t%c) > l && t/(c*c) + !!(t%(c*c)) > l) c *= c;
  int a = solve(_c, t/c+!!(t%c), t);
  int b = solve(_c, l, t/c+!!(t%c));
  int max = (a > b) ? a : b;
  c = _c;
  return 1 + max;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int res = 0;
    int L, P, C;
    cin >> L >> P >> C;
    res = solve ((long long) C, L, P); 
    
    printf("Case #%d: %d\n", t, res);
  }
}
