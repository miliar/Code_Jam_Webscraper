#include <iostream>

using namespace std;

int main()
{
	int t, tn = 1;
	string s;

	cin >> t;

	while (tn <= t)
	{
		int n;
		int b = 1, o = 1, ans = 0, tb = 0, to = 0;
		char c;
		int t;

		cin >> n;

		for (int i = 0; i < n; i++)
		{
			cin >> c >> t;

			if (c == 'B')
			{
				tb = max(ans, tb + abs(b - t)) + 1;
				ans = max(ans, tb);
				b = t;
			}
			else
			{
				to = max(ans, to + abs(o - t)) + 1;
				ans = max(ans, to);
				o = t;
			}
		}

		cout << "Case #" << tn << ": " << ans << endl;
		tn++;
	}

	return 0;
}
