#include <iostream>

using namespace std;

int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
    int n, k;
    cin >> n >> k;
    if((k+1)%(1<<n) == 0)
      cout << "ON";
    else
      cout << "OFF";
    cout << endl;
  }
  return 0;
}