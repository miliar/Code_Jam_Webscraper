#include <iostream>

using namespace std;

int main ()
{
  unsigned T = 0;
  cin >> T;
  for (unsigned t = 1; t <= T; ++t) {
    unsigned N = 0, K = 0;
    cin >> N >> K;
    unsigned mask = (1 << N) - 1;
    cout << "Case #" << t << ": " << (((K & mask) == mask) ? "ON" : "OFF") << "\n";
  }
  
  return 0;
}