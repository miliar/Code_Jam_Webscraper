#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <complex>
using namespace std;

// begin insert defines
template <class T> void PV(T &x) {for(__typeof__((x).begin()) i = (x).begin(); i != (x).end(); i++) cout << *i << " "; cout << endl;}
#define forE(elem,v)  for(__typeof__(v.begin()) _it = v.begin(); _it != v.end();++_it) for(int _once=1, _done=0; _once; (!_done) ? (_it=v.end(), --_it) :_it ) for(__typeof__(*_it) & elem = * _it; _once && !(_once=0); _done=1)
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)
#define CR clear
#define PB push_back
typedef vector<string> VRS;
#define VR vector
// end insert defines

int c, o, n;
VRS combine;
VRS opposed;
string ins;
VR<char> stk;

bool check_combine(VR<char> &stk, char &rc)
{
  int c0 = stk.back(), c1 = stk[stk.size() - 2];
  forE(c, combine) {
    if (c0 == c[0] && c1 == c[1]
        || c1 == c[0] && c0 == c[1]) {
      rc = c[2];
      return true;
    }
  }
  return false;
}

bool check_opposed(VR<char> &stk)
{
  int c0 = stk.back();
  Rep(i, stk.size() - 1) {
    char c1 = stk[i];
    forE(o, opposed) {
      if (c0 == o[0] && c1 == o[1]
          || c1 == o[0] && c0 == o[1])
        return true;
    }
  }
  return false;
}

void work()
{
  stk.CR();
  forE(c, ins) {
    stk.PB(c);
    int has_combine = 0;
    char tc;
    while (stk.size() >= 2 && check_combine(stk, tc)) {
      has_combine = 1;
      stk.pop_back();
      stk.pop_back();
      stk.PB(tc);
    }
    if (!has_combine && check_opposed(stk)) {
      stk.CR();
    }
  }
  cout << "[";
  Rep(i, stk.size()) {
    if (i) cout << ", ";
    cout << stk[i];
  }
  cout << "]" << endl;
}

void myin()
{
  combine.CR();
  opposed.CR();
  cin >> c;
  combine.resize(c);
  Rep(i, c) cin >> combine[i];
  cin >> o;
  opposed.resize(o);
  Rep(i, o) cin >> opposed[i];
  cin >> n;
  cin >> ins;
}

int main()
{
  int tests;
  cin >> tests;
  Rep(CA, tests) {
    cout << "Case #" << CA + 1 << ": ";
    myin();
    work();
  }
  return 0;
}
