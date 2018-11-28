#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    int N;
    int xorr = 0;
    long long int sum = 0;
    int min = 10000000;
    cin >> N;
    for (int n = 0; n < N; n++) {
      int c;
      cin >> c;
      xorr ^= c;
      sum += c;
      min = std::min(c, min);
      }
    if ((xorr & 0xFFFFF) != 0)
    {
      cout << "Case #" << t << ": NO" << endl;
    }
    else
    {
      cout << "Case #" << t << ": " << sum - min << endl;
    }
  }
  return 0;
}
