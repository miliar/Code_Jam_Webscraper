#include <inttypes.h>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>

typedef long long ll;

using namespace std;

namespace {

void PrintOutput(size_t iter, const double result) {
  printf("Case #%d: %10.10f\n", iter+1, result);
}
} //namespace

int main() {
  size_t T;
  cin >> T;

  for (size_t i = 0; i < T; ++i) {
    double X, S, R, t, N;
    cin >> X >> S >> R >> t >> N;

    double result = 0.0;
    double sum_walk = 0.0;
    vector<pair<double, pair<double, double> > > walks;
    for (size_t n = 0; n < N; ++n) {
      double B, E, w;
      cin >> B >> E >> w;

      sum_walk += E - B;
      walks.push_back(make_pair(w, make_pair(B, E)));
    }

    sort(walks.begin(), walks.end());

    double remind = X - sum_walk;
    if (remind / R > t) {
      result += t;
      remind -= t * R;
      t = 0.0;

      result += remind / S;
    } else {
      result += remind / R;
      t -= remind / R;
    }
    
    for (size_t wa = 0; wa < walks.size(); ++wa) {
      double start = walks[wa].second.first;
      double end = walks[wa].second.second;
      double dist = end - start;

      double w = walks[wa].first;
      if (t > 0.0) {

        if (dist / (R + w) > t) {
          result += t;
          dist -= t * (R + w);
          t = 0.0;

          result += dist / (S + w);
        } else {
          result += dist / (R + w);
          t -= dist / (R + w);
        }
      } else {
        result += dist / (S + w);
      }
    }

    PrintOutput(i, result);
  }
  return 0; 
}
