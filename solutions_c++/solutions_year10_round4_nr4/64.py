#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "D"

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

double dist(const pii& a, const pii& b) {
  return hypot(a.first - b.first, a.second - b.second);
}

double GetSegmentArea(double r, double angle) {
  return 0.5 * r * r * (angle - sin(angle));
}

double GetTwoCirclesIntersection(const pii& o1, const pii& o2, const pii& a) {
  double r1 = dist(o1, a);
  double r2 = dist(o2, a);
  double d = dist(o1, o2);
  double angle1 = 2 * acos((r1 * r1 + d * d - r2 * r2) / (2 * r1 * d));
  double angle2 = 2 * acos((r2 * r2 + d * d - r1 * r1) / (2 * r2 * d));
  return GetSegmentArea(r1, angle1) + GetSegmentArea(r2, angle2);
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    
    int N, M;
    cin >> N >> M;
    vector<pii> P(N);
    vector<pii> Q(M);
    for (int i = 0; i < N; ++i) {
      scanf("%d%d", &P[i].first, &P[i].second);
    }
    for (int i = 0; i < M; ++i) {
      scanf("%d%d", &Q[i].first, &Q[i].second);
    }
    cout << "Case #" << test_index + 1 << ":";
    for (int qi = 0; qi < Q.size(); ++qi) {
      double area = GetTwoCirclesIntersection(P[0], P[1], Q[qi]);
      printf(" %.12lf", area);
    }
    printf("\n");
  }
  return 0;
}

