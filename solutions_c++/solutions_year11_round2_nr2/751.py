#include <float.h>

#include <iostream>
#include <vector>
#include <set>

using namespace std;
namespace {
void PrintOutput(size_t iter, double result) {
  cout << "Case #" << iter+1 << ": " << result <<  endl;
}
} //namespace

int main() {
  size_t T;
  cin >> T;

  for (size_t t = 0; t < T; ++t) {
    size_t C;
    int D;
    cin >> C >> D;

    std::vector<pair<int, size_t> > pv;
    for (size_t c = 0; c < C; ++c) {
      int P;
      size_t V;
      cin >> P >> V;
      pv.push_back(make_pair(P, V));
    }

    double max_time = - DBL_MAX;
    for (size_t low = 0; low < pv.size(); ++low) {
      size_t people = 0;
      for (size_t up = low; up < pv.size(); ++up) {
        people += pv[up].second;
        int diff = pv[up].first - pv[low].first;
        double time = (D * ((int)people - 1) - diff) / 2.0;

        if (max_time < time)
          max_time = time;
      }
    }

    if (max_time  < 0.0)
      max_time = 0.0;
    PrintOutput(t, max_time);
  }

  return 0;
}
