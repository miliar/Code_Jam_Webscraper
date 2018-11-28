#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cassert>

struct Vine {
  long long d;
  long long i;
  Vine(long long d, long long i): d(d), i(i) {}
  bool operator < (const Vine &v) const {
    return d < v.d;
  }

};


bool solve_(const std::vector<Vine> &vines, long long d) {
  std::set<Vine> vines_(vines.begin(), vines.end());
  std::map<long long, long long> q;
  if (vines[0].d > vines[0].i) {
    return false;
  }

  q.insert(std::make_pair(vines[0].d, vines[0].d));
  while (!q.empty()) {
    long long current = q.begin()->first;
    long long length = q.begin()->second;
    q.erase(q.begin());
    auto lo = 
      std::lower_bound(vines.begin(), vines.end(), Vine(current + 1, 0));
    if (current <= d && d <= current + length) {
      return true;
    }

    for (auto i = lo; i != vines.end() && i->d <= current + length; ++i) {
      const Vine &v = *i;
      long long l = std::min(v.i, v.d - current);
      long long d = v.d;
      q[d] = q.find(d) == q.end()? l: std::max(l, q[d]);
    }
  }
  return false;


}

std::string solve(const std::vector<Vine> &vines, long long d) {
  return solve_(vines, d)? "YES": "NO";
}

int main(void) {
  int T;
  std::cin >> T;
  for (int i = 0; i < T; ++i) {
    long long N;
    std::cin >> N;
    std::vector<Vine> vines;
    long long d;
    for (long long j = 0; j < N; ++j) {
      Vine v(0, 0);
      std::cin >> v.d >> v.i;
      vines.push_back(v);
    }
    std::cin >> d;

    std::cout << "Case #" << (i + 1) << ": " << solve(vines, d) << std::endl;
  }
}
