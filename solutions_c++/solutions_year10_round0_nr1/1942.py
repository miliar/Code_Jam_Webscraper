#include <iostream>
using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
  {
    int N, K;
    cin >> N >> K;
    if ((K + 1) % (1 << N) == 0)
      cout << "Case #" << i << ": ON" << endl;
    else
      cout << "Case #" << i << ": OFF" << endl;
  }
  return 0;
}
