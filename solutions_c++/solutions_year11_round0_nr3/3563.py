// qual - 2011, Problem C. Candy splitting
// result:
#include <stdio.h>
#include <math.h>
#include <assert.h>
#include <iostream>
#include <algorithm>
#include <vector>

using std::cin;
using std::cout;
using std::endl;

//const char input[] = "c-input.txt";  const char output[] = "c-output.txt";
//const char input[] = "C-small-attempt2.in";  const char output[] = "C-small-attempt2.out";

const char input[] = "C-large.in";  const char output[] = "C-large.out";

typedef std::vector<int> vi;

template <typename T>
static T Abs(T a) {
  return a > 0 ? a : -(a);
}

void run(const int t) {
  int n;
  cin >> n;
  std::vector<int> candy;
  for (int i = 0; i < n; ++i) {
    int c;
    cin >> c;
    candy.push_back(c);
  }

  std::sort(candy.begin(), candy.end());

  int sean = -1;
  for (size_t i = 1; i < candy.size(); ++i) {
    int s1 = 0;
    int s2 = 0;
    for (size_t k = 0; k < i; ++k) {
      s1 ^= candy[k];
      s2 += candy[k];
    }

    int s3 = 0;
    int s4 = 0;
    for (size_t k = i; k < candy.size(); ++k) {
      s3 ^= candy[k];
      s4 += candy[k];
    }

    if (s1 == s3 && std::max(s2, s4) > sean) {
      sean = std::max(s2, s4);
    }
  }  


  if (sean >= 0)
    cout << "Case #" << t << ": " << sean << endl;
  else
    cout << "Case #" << t << ": NO " << endl;

}

int main() {
  freopen(input, "rt", stdin);
  freopen(output, "wt", stdout);

  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    run(t);
  }
  return 0;
}


