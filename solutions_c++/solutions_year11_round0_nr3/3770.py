#include <iostream>

using namespace std;

int main()
{
  int T;
  cin >> T;

  for (int i = 0; i < T; ++i)
  {
    int N;
    cin >> N;
    long sum = 0;
    long mi = 1 << 30;
    long xo = 0;

    for (int j = 0; j < N; ++j)
    {
      long c;
      cin >> c;

      sum += c;
      mi = min(mi, c);
      xo ^= c;
    }

    if (xo)
      cout << "Case #" << (i + 1) << ": NO" << endl;
    else
      cout << "Case #" << (i + 1) << ": " << (sum - mi) << endl;
  }

  return 0;
}
