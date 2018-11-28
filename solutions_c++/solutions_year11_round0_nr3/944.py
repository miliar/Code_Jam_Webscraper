#include <iostream>

using namespace std;

int main()
{
	int t, tn = 1;

	cin >> t;

	while (tn <= t)
	{
		int n, m = 0, s = 0, x = 0, t = 0;

		cin >> n >> m;
		s = x = m;
		for (int i = 1; i < n; i++)
		{
			cin >> t;
			s += t;
			m = min(m, t);
			x ^= t;
		}

		cout << "Case #" << tn << ": ";
		if (x != 0)
			cout << "NO\n";
		else
			cout << s - m << endl;
		tn++;
	}

	return 0;
}
