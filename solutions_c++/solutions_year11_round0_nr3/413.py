#include <iostream>

using namespace std;

int main()
{
  freopen("c.in", "r", stdin);
  freopen("c.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
		int n;
		cin >> n;
		int m = 1000000000;
		int sum = 0;
		int z = 0;
		for (int i = 0; i < n; i++)
		{
			int c;
			cin >> c;
			sum += c;
			z ^= c;
			if (c < m) m = c;
		}
		if (z)
			cout << "NO";
		else
			cout << sum - m;
    cout << endl;
  }
  return 0;
}