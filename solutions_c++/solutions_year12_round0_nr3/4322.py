// PRESENTING THE SLOWEST CODE EVER TO GET 20 POINTS
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

bool ok(int a, int b) {
  stringstream ss;
  ss << a;
  stringstream tt;
  tt << b;
  string s = ss.str();
  string t = tt.str();
  
  rep(i, t.length()) {
    stringstream uu;
    uu << string(t.c_str() + i);
    uu << string(t.c_str(), t.c_str() + i);
    if (uu.str() == s) return true;;
  }
  return false;
  
}

int solve(int a, int b) {
  int res = 0;
  F(n, a, b+1) {
    F(m, n + 1, b + 1) {
      if (ok(n, m)) res++;
    }
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  rep(t,T) {
    int A, B;
    cin >> A >> B;
    printf("Case #%d: %d\n", t+1, solve(A,B));
  }

}
