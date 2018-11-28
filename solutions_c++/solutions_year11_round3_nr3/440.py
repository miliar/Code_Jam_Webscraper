#include <inttypes.h>

#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;
namespace {
void PrintOutput(size_t iter, size_t result) {
  cout << "Case #" << iter+1 << ": " << result << endl;
}

void PrintOutput(size_t iter, const char* result) {
  cout << "Case #" << iter+1 << ": " << result << endl;
}
} //namespace

int main() {
  size_t T;
  cin >> T;

  for (size_t t = 0; t < T; ++t) {
    size_t N;
    int64_t L, H;
    cin >> N >> L >> H;

    vector<int64_t> frequencies;
    for (size_t n = 0; n < N; ++n) {
      int64_t frequency;
      cin >> frequency;
      frequencies.push_back(frequency);
    }

    bool check2 = true;
    for (size_t i = L; check2 && i <= H; ++i) {
      bool check = true;
      for (size_t n = 0; n < N; ++n) {
        if (i % frequencies[n] != 0 && frequencies[n] % i != 0) {
          check = false;
          break;
        }
      }

      if (check) {
        PrintOutput(t, i);
        check2 = false;
      }
    }

    if (check2)
      PrintOutput(t, "NO");
  }
  return 0;
}
