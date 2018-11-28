#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

int top[2001];
int h[2001];

bool solve(int begin, int end) {
  //cerr << "solver " << begin << ' ' << end << endl;
  vector<int> tb;
  int i = begin;
  while (i != end) {
    tb.push_back(i);
    i = top[i];
    if (i > end) return false;
  }
  tb.push_back(i);
  for (i = 0; i < tb.size() - 1; ++i) {
    if (tb[i] + 1 < tb[i+1]) {
      if (!solve(tb[i] + 1, tb[i+1])) {
        return false;
      }
      for (int k = 1; k < tb[i+1] - tb[i]; ++k) {
        h[tb[i+1] - k] -= k;
      }
    }
  }
  return true;
}

int main()
{
  int tcase = 0;
  cin >> tcase;
  for (int tind = 1; tind <= tcase; tind++) {
    int i,j;
    int n;
    cin >> n;
    for (i = 1; i < n; ++i) {
      cin >> top[i];
    }
    mset(h, 0);
    bool ans = solve(1, n);
    cout << "Case #" << tind << ":";
    if (!ans) cout << " Impossible";
    else {
      int minh = h[1];
      for (i = 1; i <= n; ++i) {
        if (h[i] < minh) {
          minh = h[i];
        }
      }
      for (i = 1; i <= n; ++i)
        cout << ' ' << h[i]-minh+1;
    }
    cout << endl;
  }
  return 0;
}
