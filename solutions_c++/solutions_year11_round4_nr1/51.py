#include <algorithm>
#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

struct Segment {
  int a, b, boost;
  int length() const { return b-a; }
};

struct cmp_a {
  bool operator()(const Segment &s1, const Segment &s2) const {
    return s1.a < s2.a;
  }
};

struct cmp_boost {
  bool operator()(const Segment &s1, const Segment &s2) const {
    return s1.boost < s2.boost;
  }
};

int main(void) {
  cin.sync_with_stdio(0);

  int CASES; cin >> CASES;
  for (int tt=1; tt<=CASES; ++tt) { // caret here
    int L, W, R, N;
    double runtimeleft;
    cin >> L >> W >> R >> runtimeleft >> N;

    vector<Segment> walkways(N);
    for (int i=0; i<N; ++i) {
      cin >> walkways[i].a >> walkways[i].b >> walkways[i].boost;
    }
    sort(walkways.begin(), walkways.end(), cmp_a());

    vector<Segment> segments; segments.reserve(2*N+5);
    int lastp = 0;
    for (int i=0; i<N; ++i) {
      if (walkways[i].a > lastp) {
        segments.push_back((Segment){lastp, walkways[i].a, 0});
      }
      segments.push_back(walkways[i]);
      lastp = walkways[i].b;
    }
    if (lastp != L) {
      segments.push_back((Segment){lastp, L, 0});
    }

    sort(segments.begin(), segments.end(), cmp_boost());

    double result = 0;
    for (int i=0; i<(int)segments.size(); ++i) {
      double dist = segments[i].length();
      double trun = min(dist / (R + segments[i].boost), runtimeleft);
      result += trun;
      runtimeleft -= trun;
      dist -= trun * (R + segments[i].boost);
      result += dist / (W + segments[i].boost);
    }

    printf("Case #%d: %.9f\n", tt, result);
  }

  return 0;
}
