#include <iostream>
#include <cstdlib>

using namespace std;

int main(int argc, char* argv[])
{
  int N, T;
  int sum, min, xorVal;
  int tmp;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    cin >> N;
    xorVal = sum = 0;
    min = 1000000;
    for (int j = 0; j < N; ++j) {
      cin >> tmp;
      sum += tmp;
      if (tmp < min)
        min = tmp;
      xorVal ^= tmp;
    }
    if (xorVal)
      cout << "Case #" << (i+1) << ": " << "NO" << endl;
    else
      cout << "Case #" << (i+1) << ": " << (sum - min) << endl;
  }
  return 0;
}
