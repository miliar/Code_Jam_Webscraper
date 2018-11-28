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
#define PROBLEM_ID "A"

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long double ld;
typedef pair<int, int> pii;

const ld eps = 1e-8;

vector<pii> ReadPolyline(int points) {
  vector<pii> polyline(points);
  for (int i = 0; i < points; ++i) {
    cin >> polyline[i].first >> polyline[i].second;
  }
  return polyline;
}

double GetAreaUnder(const vector<pii>& polyline, double left, double right) {
  double result = 0;
  for (int i = 0; i + 1 < polyline.size(); ++i) {
    if (polyline[i + 1].first < left - eps) {
      continue;
    }
    if (polyline[i].first > right + eps) {
      continue;
    }
    double leftx, lefty, rightx, righty;
    if (polyline[i].first > left - eps) {
      leftx = polyline[i].first;
      lefty = polyline[i].second;
    } else {
      leftx = left;
      lefty = polyline[i].second + (polyline[i + 1].second - polyline[i].second) * (left - polyline[i].first) / (polyline[i + 1].first - polyline[i].first);
    }
    if (polyline[i + 1].first < right + eps) {
      rightx = polyline[i + 1].first;
      righty = polyline[i + 1].second;
    } else {
      rightx = right;
      righty = polyline[i].second + (polyline[i + 1].second - polyline[i].second) * (right - polyline[i].first) / (polyline[i + 1].first - polyline[i].first);
    }
    result += (rightx - leftx) * (lefty + righty);
  }
  return result / 2;
}

double GetAreaBetween(const vector<pii>& lower, const vector<pii>& upper, double left, double right) {
  return GetAreaUnder(upper, left, right) - GetAreaUnder(lower, left, right);
}

vector<double> DivideIntoEqualParts(const vector<pii>& lower, const vector<pii>& upper, int parts, int width) {
  double left = 0;
  double right = width;
  double all = GetAreaBetween(lower, upper, left, right);
  double one_piece = all / parts;
  vector<double> result;
  for (int i = 0; i < parts - 1; ++i) {
    double low = left;
    double up = right;
    while (low < up - eps) {
      double mid = (low + up) / 2;
      double cur_area = GetAreaBetween(lower, upper, left, mid);
      if (cur_area < one_piece) {
        low = mid;
      } else {
        up = mid;
      }
    }
    result.push_back(low);
    left = low;
  }
  return result;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int width, low_points, up_points;
    cin >> width >> low_points >> up_points;
    int parts;
    cin >> parts;
    vector<pii> lower = ReadPolyline(low_points);
    vector<pii> upper = ReadPolyline(up_points);
    vector<double> answer = DivideIntoEqualParts(lower, upper, parts, width);
    cout << "Case #" << test_index + 1 << ": " << endl;
    cerr << "Case #" << test_index + 1 << ": " << endl;
    for (int i = 0; i < answer.size(); ++i) {
      printf("%.10lf\n", answer[i]);
      fprintf(stderr, "%.10lf\n", answer[i]);
    }
  }
  return 0;
}
