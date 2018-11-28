// CPPFLAGS=-std=gnu++0x -W -Wall -g -O2
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define foreach(i,c) for(auto i=(c).begin();i!=(c).end();++i)
template<class T> bool in(T e, const set<T>& s) { return s.find(e) != s.end(); }

int main() {
  int tests; cin >> tests;
  for (int test=1;test<=tests;++test) {
    cout << "Case #" << test << ": ";
    int64_t t; int L, N, C;
    cin >> L >> t >> N >> C;
    vector<int64_t> a(C);
    vector<int64_t> x;
    int i;
    for (i=0;i<C;++i) cin >> a[i];
    int64_t r = 0;
    for (i=0;i<N;++i) {
      r += 2 * a[i%C];
      if (r >= t) {
        x.push_back((r-t)/2);
        r = t;
        ++i;
        break;
      }
//cout << "r=" << r << endl;
    }
    for (;i<N;++i) x.push_back(a[i%C]);
//foreach(xx,x) cout << *xx << " "; cout << endl;
    sort(all(x));
    int n = x.size();
    for (i=0;i<n-L;++i) r += 2 * x[i];
    for (;i<n;++i) r += x[i];
    cout << r << endl;
  }
}
