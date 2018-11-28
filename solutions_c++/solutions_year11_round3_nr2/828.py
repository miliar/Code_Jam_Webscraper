#include <algorithm>
#include <iostream>
#include <vector>

struct Tuple {
  int pos;
  int dist;
  double time;
  double boost;
  bool boost_on;
};

class BoostComparer {
 public:
  bool operator()(const Tuple &lhs, const Tuple &rhs) const {
    return lhs.boost > rhs.boost;
  }
};

class PosComparer {
 public:
  bool operator()(const Tuple &lhs, const Tuple &rhs) const {
    return lhs.pos < rhs.pos;
  }
};

double update(std::vector<Tuple> &v, int T) {
  double time = 0.0;
  for (int n = 0; n < v.size(); ++n) {
    v[n].time = time;
    v[n].boost = 0.0;
    if (v[n].time >= T) {
      v[n].boost = v[n].dist;
    } else if ((time + (v[n].dist * 2)) > T) {
      v[n].boost = ((time + (v[n].dist * 2)) - T) / 2.0;
    } else {
      v[n].boost = 0.0;
    }
    if (v[n].boost_on) {
      time += (v[n].dist * 2) - v[n].boost;
    } else {
      time += v[n].dist * 2;
    }
  }
  return time;
}

long long solve(int L, int T, int N, const std::vector<int> &a) {
  std::vector<Tuple> v(N);
  v[0].pos = 0;
  v[0].dist = a[0];
  for (int n = 1; n < N; ++n) {
    v[n].pos = v[n - 1].pos + v[n - 1].dist;
    v[n].dist = a[n % a.size()];
    v[n].boost_on = false;
  }

  for (int l = 0; l < L; ++l) {
    update(v, T);
    int max_n = 0;
    double max_boost = -1.0;
    for (int n = 0; n < N; ++n) {
      if (!v[n].boost_on && (v[n].boost > max_boost)) {
        max_n = n;
        max_boost = v[n].boost;
      }
    }
    v[max_n].boost_on = true;
  }

  return update(v, T);
}

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int L;
    double T2;
    int N, C;
    std::cin >> L >> T2 >> N >> C;
    std::vector<int> a(C);
    for (int c = 0; c < C; ++c) {
      std::cin >> a[c];
    }
    std::cout << "Case #" << t << ": " << solve(L, T2, N, a) << std::endl;
  }
  return 0;
}
