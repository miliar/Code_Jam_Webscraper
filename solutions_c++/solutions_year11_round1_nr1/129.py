#include <iostream>

using namespace std;

int gcd (int a, int b)
{
	while (a && b)
	{
		int c = a%b;
		a = b;
		b = c;
	}
	return a + b;
}

int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
		int n, d, g;
		cin >> n >> d >> g;
		if (d > 0 && g == 0)
		{
			cout << "Broken";
		}
		else if (d < 100 && g == 100)
		{
			cout << "Broken";
		}
		else
		{
			if (100 / gcd(d, 100) <= n)
				cout << "Possible";
			else
				cout << "Broken";
		}
    cout << endl;
  }
  return 0;
}