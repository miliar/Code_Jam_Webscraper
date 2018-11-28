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
#define ALL(a) (a).begin(),(a).end()
#define forE(elem,v)  for(__typeof__(v.begin()) _it = v.begin(); _it != v.end();++_it) for(int _once=1, _done=0; _once; (!_done) ? (_it=v.end(), --_it) :_it ) for(__typeof__(*_it) & elem = * _it; _once && !(_once=0); _done=1)
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)
typedef vector<int> VRI;
typedef long long LL;
// end insert defines

int n;
VRI nums;

void work()
{
  sort(ALL(nums));
  int xsum = 0;
  forE(num, nums) xsum ^= num;
  if (xsum) cout << "NO" << endl;
  else {
    int sum = 0;
    forE(num, nums) sum += num;
    sum -= nums[0];
    cout << sum << endl;
  }
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
  Rep(CA, tests) {
    cout << "Case #" << CA + 1 << ": ";
    myin();
    work();
  }
  return 0;
}
