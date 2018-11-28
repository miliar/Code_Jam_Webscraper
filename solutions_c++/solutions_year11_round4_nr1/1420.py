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
typedef long long LL;
#define PR pair
template<typename S, typename T> ostream& operator<<(ostream& os, pair<S,T> p){ return os << "(" << p.first << "," << p.second << ")"; };
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)
#define ND second
#define FS first
typedef vector<int> VRI;
#define VR vector
// end insert defines

struct Seg
{
  double len, w;
  friend bool operator < (const Seg &l, const Seg &r)
  {
    return l.w < r.w;
  }
};

VR<Seg> segs;
double x, s, r, t;
int n;

void work()
{
  sort(ALL(segs));
  double ans = 0.0;
  Rep(i, n) {
    Seg seg = segs[i];
    if (ans + seg.len / (r + seg.w) >= t) {
      double rl = seg.len - (r + seg.w) * (t - ans);
      ans = t;
      ans += rl / (s + seg.w);
      for (int j = i + 1; j < n; j++) {
        ans += segs[j].len / (s + segs[j].w);
      }
      break;
    }
    else {
      ans += seg.len / (r + seg.w);
    }
  }
  cout << setiosflags(ios::fixed) << setprecision(10);
  cout << ans << endl;
}

void myin()
{
  cin >> x >> s >> r >> t >> n;
  segs.resize(n);
  double sum = 0.0;
  forE(s, segs) {
    double b, e;
    cin >> b >> e >> s.w;
    s.len = e - b;
    sum += s.len;
  }
  n++;
  segs.resize(n);
  segs[n - 1].len = x - sum;
  segs[n - 1].w = 0;
}

int main()
{
  int tests;
  scanf("%d", &tests);
  for (int Ca = 0; Ca < tests; Ca++) {
    printf("Case #%d: ", Ca + 1);
    myin();
    work();
  }
  return 0;
}

