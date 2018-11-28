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
#define forE(elem,v)  for(__typeof__(v.begin()) _it = v.begin(); _it != v.end();++_it) for(int _once=1, _done=0; _once; (!_done) ? (_it=v.end(), --_it) :_it ) for(__typeof__(*_it) & elem = * _it; _once && !(_once=0); _done=1)
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)
template <class T> void PV(T &x) {for(__typeof__((x).begin()) i = (x).begin(); i != (x).end(); i++) cout << *i << " "; cout << endl;}
#define CR clear
#define PB push_back
typedef vector<int> VRI;
#define VR vector
// end insert defines

int n;
VRI nums;
VR<double> f;
VR<VR<double> > prob;
VR<double> reciprocal_A;

void init()
{
  reciprocal_A.CR();
  reciprocal_A.PB(1.0);
  Rep(i, 1010) reciprocal_A.PB(reciprocal_A.back() / double(i + 1));
  //  PV(reciprocal_A);
  // forE(a, reciprocal_A)
  //   cout << 1 / a << ' ';
  // cout << endl;
}

double calc_probability(int a, int n)
{
  double &ret = prob[a][n];
  if (ret > -0.5) return ret;
  ret = 0.0;
  double sign = 1;
  Rep(i, n - a + 1) {
    ret += reciprocal_A[i] * sign;
    sign = -sign;
  }
  ret *= reciprocal_A[a];
  return ret;
}

double dp(int n)
{
  double &ret = f[n];
  if (ret > -0.5) return ret;
  if (n == 1 || n == 0) return ret = 0.0;
  ret = 0.0;
  for (int i = 1; i <= n; i++) {
    ret += calc_probability(i, n) * (dp(n - i));
  }
  ret += 1.0;
  //  cout << ret << endl;
  ret /= (1.0 - calc_probability(0, n));
  return ret;
}

void work()
{
  int ds = 0;
  Rep(i, n) if (nums[i] != i + 1) ds++;
  f.assign(n + 1, -1.0);
  prob.assign(n + 1, VR<double>(n + 1, -1.0));
  double ans = dp(ds);
  cout << setiosflags(ios::fixed) << setprecision(6) << ans << endl;
}

void myin()
{
  cin >> n;
  nums.resize(n);
  Rep(i, n) cin >> nums[i];
}

int main()
{
  int tests;
  cin >> tests;
  init();
  Rep(CA, tests) {
    cout << "Case #" << CA + 1 << ": ";
    myin();
    work();
  }
  return 0;
}
