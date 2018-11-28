#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;

struct Line {
  int katamuki;
  int y_a, y_b;
  Line(int y_a_arg, int y_b_arg) {
    y_a = y_a_arg;
    y_b = y_b_arg;
    katamuki = y_b - y_a;
  }
  bool is_cross(Line l) {
    return (y_a < l.y_a && y_b > l.y_b);
  }
};

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    int N;
    scanf("%d", &N);
    vector<Line> lines;
    for (int i = 0; i < N; ++i) {
      int A, B;
      scanf("%d %d", &A, &B);
      lines.push_back(Line(A, B));
    }
    int count = 0;
    for (int i = 0; i < lines.size(); ++i) {
      for (int j = 0; j < lines.size(); ++j) {
	if (i == j) continue;
	if (lines[i].is_cross(lines[j])) ++count;
      }
    }
    
    printf("Case #%d: %d\n", t, count);
  }
}
