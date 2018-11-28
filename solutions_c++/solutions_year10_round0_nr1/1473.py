#include <iostream>

using namespace std;

int main()
{
  int T;
  cin >> T;

  for (int i = 0; i < T; i++)
  {
    long long N, K;
    cin >> N >> K;
    bool test = true;
    for (int j = 0; j < N; j++)
    {
      if (K % 2 == 0)
      {
        test = false;
        break;
      }
      K = K / 2;
    }
    cout << "Case #" << i + 1 << ": " << (test ? "ON" : "OFF") << endl;
  }
}

