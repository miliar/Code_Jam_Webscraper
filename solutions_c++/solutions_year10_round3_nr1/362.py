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

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N;
    cin >> N;
    int a[N], b[N];
    rep(n,N) {
      cin >> a[n] >> b[n];
    }
    int res = 0;
    rep (i,N) {
      rep (j, N) {
        if (i == j) continue;
        if ((a[i] > a[j] && b[i] < b[j]))
          res++;
      }
    }
    printf("Case #%d: %d\n", t, res);
  }
}
