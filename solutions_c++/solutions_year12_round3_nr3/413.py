#include <iostream>
#include <map>
#include <algorithm>
#include <sstream>
#include <vector>
#include <iomanip>
#include <cassert>
#include <queue>
using namespace std;
typedef vector<pair<long long, long long> > VP;
long long sol;
void solve(long long aix, long long bix, VP& a, VP& b, long long &score)
{
  if (aix == a.size() - 1 && bix == b.size() - 1) {
    long long v = 0; // final resource
    if (a[aix].second == b[bix].second) {
      v = min(a[aix].first, b[bix].first);
    }
    sol = max(sol, score+v);
    return;
  }
  if (aix != a.size() - 1) {
    long long v = 0; // minus resource
    if (a[aix].second == b[bix].second) {
      v = min(a[aix].first, b[bix].first);
      score += v;
      a[aix].first -= v; b[bix].first -= v;
    }
    aix++;
    solve(aix, bix, a, b, score);
    aix--;
    if (v > 0) {
      score -= v;
      a[aix].first += v; b[bix].first += v;
    }
  }
  if (bix != b.size() - 1) {

    long long v = 0; // minus resource
    if (a[aix].second == b[bix].second) {
      v = min(a[aix].first, b[bix].first);
      score += v;
      a[aix].first -= v; b[bix].first -= v;
    }
    bix++;
    solve(aix, bix, a, b, score);
    bix--;
    if (v > 0) {
      score -= v;
      a[aix].first += v; b[bix].first += v;
    }
  }
}
int main()
{
  long long sz, now = 1;
  cin >> sz;
  for (long long sz_i = 0; sz_i < sz; ++sz_i) {
    long long N, M; cin >> N >> M;
    vector<pair<long long, long long> > a; // box type pair
    vector<pair<long long, long long> > b; // toy type pair
    for (long long i = 0; i < N; ++i) {
      long long a1, a2; cin >> a1 >> a2;
      a.push_back(make_pair(a1, a2));
    }
    for (long long i = 0; i < M; ++i) {
      long long b1, b2; cin >> b1 >> b2;
      b.push_back(make_pair(b1, b2));
    }
    long long a_ix = 0, b_ix = 0;
    long long score = 0;
    sol = 0;
    solve(a_ix, b_ix, a, b, score);

    stringstream ss;
    ss << "Case #" << now++ << ": ";
    cout << ss.str() << sol << endl;
  }
}
