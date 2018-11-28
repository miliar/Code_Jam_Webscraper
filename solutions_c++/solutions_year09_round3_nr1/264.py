// BEGIN CUT HERE
#include "cout.h"
// END CUT HERE
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <cmath>
#include <queue>
#include <list>
#include <complex>
#include <iomanip>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef long long LL;
typedef complex<double> CMP;
#define Fill(a, b) memset((a), (b), sizeof(a))
#define REP(a, b) for (size_t (a) = 0; (a)<(size_t)(b); ++(a))
#define sz size()
#define Tr(c, i) for(typeof((c).begin()) i= (c).begin(); (i) != (c).end(); ++(i))
#define All(c) (c).begin(), (c).end()
#define Present(c, x) ((c).find(x) != (c).end()) // for Map or Set
#define CPresent(c, x) (find(All(c), x) != end()) // for vector

#include <assert.h>

long long ipow(int a, int b) {
  long long ret = 1LL;
  REP(i, b)
    ret *= a;
  return ret;
}

int main(void)
{
  int T;
  cin >> T;

  REP(i, T) {
    string l, l2;
    map< char, int > m;
    long long a = 0LL;
    cin >> l;
    l2 = l;
    sort(All(l));
    string::iterator end_it = unique(All(l));
    l.erase(end_it, l.end());
    int base = l.sz;
    if (base == 1) {
      base = 2;
    }
    int l2sz = l2.sz;
    int count = 1;
    REP(j, l2.sz) {
      char c = l2[j];
      int t;
      long long r;
      if (Present(m, c)) {
        t = m[c];
      } else {
        m[c] = count;
        t = count;
        if (count == 1) {
          count = 0;
        } else if (count == 0) {
          count = 2;
        } else {
          count++;
        }
      }
      r = ipow(base, l2sz - j - 1);
      a += r * t;
    }
    cout << "Case #" << (i+1) << ": " << a << endl;
  }
  return 0;
}



