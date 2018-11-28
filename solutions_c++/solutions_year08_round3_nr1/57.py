#include <iostream>

using namespace std;

const int maxL = 1000 + 10;

int N, P, K, L;

int f[maxL];

bool
cmp(int a, int b)
{
  return a > b;
}

int main()
{
  int sum;
  cin >> N;
  for (int e = 1; e <= N; ++e)
  {
    cout << "Case #" << e << ": ";
    cin >> P >> K >> L;
    for (int i = 0; i < L; ++i)
    {
      cin >> f[i];
    }
    sort(f, f + L, cmp);
    sum = 0;
    for (int i = 0; i < L; ++i)
    {
      sum += f[i] * (i / K + 1);
    }
    cout << sum << endl;
  }
  return 0;
}
      
