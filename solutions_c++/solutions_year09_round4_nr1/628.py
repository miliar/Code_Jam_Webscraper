#include<algorithm>
#include<cmath>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<utility>
#include<sstream>
#include<vector>
using namespace std;

template<class A, class B> void conv_(A& x, B& y) { stringstream s; s << x; s >> y; }

typedef unsigned int uint;
typedef unsigned long long int ullong;
#define for_(i, a, b) for(int i=(a);i<(b);++i)
#define set_(a, n) memset(a, n, sizeof a)

int main(void) {
  int t;
  cin >> t;

  for_(k, 1, t+1) {

    int n; cin >> n;
    vector<int> m(n);
    for_(i,0,n) {
      m[i] = -1;
      for_(j, 0, n) {
        char x; cin >> x;
        if (x == '1') m[i] = j;
      }
    }

    int res = 0;

    while (true) {
      bool b = false;

      for_(i, 0, n) {
        if (m[i] <= i) continue;
        b = true;
        int j = i+1;
        while (j < n)
          if (m[j] <= i) break;
          else ++j;
        for (int k = j; k > i; --k) {
          swap(m[k],m[k-1]);
          ++res;
        }
      }

      if (!b) break;
    }

    cout << "Case #" << k << ": " << res << endl;
  }

  return 0;
}
