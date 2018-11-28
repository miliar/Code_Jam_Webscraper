#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);

	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		int posB = 1;
		int moveB = 0;
		int posO = 1;
		int moveO = 0;

		int n;
		cin >> n;

		for (int j = 0; j < n; j++)
		{
			int a;
			string c;
			cin >> c >> a;

			if (c[0] == 'O')
			{
				moveO += abs(posO - a);
				if (moveO < moveB) moveO = moveB;
				moveO++;
				posO = a;
			}
			else
			{
				moveB += abs(posB - a);
				if (moveB < moveO) moveB = moveO;
				posB = a;
				moveB++;
			}

		}

		cout << "Case #" << i + 1 << ": " << (moveO > moveB ? moveO : moveB) << "\n";	}

	return 0;
}
