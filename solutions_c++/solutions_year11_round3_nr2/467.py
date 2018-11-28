#include <inttypes.h>

#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;
namespace {
void PrintOutput(size_t iter, size_t result) {
  cout << "Case #" << iter+1 << ": " << result << endl;
}
} //namespace

int main() {
  size_t T;
  cin >> T;

  for (size_t iter = 0; iter < T; ++iter) {
    int64_t L, t, N, C;
    cin >> L >> t >> N >> C;

    vector<int64_t> distance;
    int64_t one_iteration = 0;
    for (size_t c = 0; c < C; ++c) {
      int64_t a_c;
      cin >> a_c;
      distance.push_back(a_c);
      one_iteration += a_c;
    }

    int64_t result = 0;
    int64_t nokori = t;
    while (nokori >= one_iteration * 2) {
      if (N >= C) {
        nokori -= one_iteration * 2;
        result += one_iteration * 2;
        N -= C;
      } else {
        for (size_t i = 0; i < N; ++i)
          result += distance[i] * 2;
        N = 0;
        break;
      }
    }

    vector<int64_t> all_distance;
    size_t i = 0;
    while (nokori > 0 && N > 0) {
      if (distance[i] * 2 <= nokori) {
        nokori -= distance[i] * 2;
        result += distance[i] * 2;
      } else {
        result += nokori;
        all_distance.push_back(distance[i] * 2 - nokori);
        nokori = 0;
      }
      --N;
      ++i;
    }

    for (size_t j = 0; j < N; ++j) {
      if (i == C) i = 0;
      all_distance.push_back(distance[i] * 2);
      ++i;
    }

    sort(all_distance.begin(), all_distance.end(), greater<int64_t>());

    for (size_t j = 0; j < L; ++j) {
      result += all_distance[j] / 2;
    }

    for (size_t j = L; j < all_distance.size(); ++j) {
      result += all_distance[j];
    }
    
    PrintOutput(iter, result);
  }
  return 0;
}
