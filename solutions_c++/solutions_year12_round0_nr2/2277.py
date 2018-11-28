#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		int N, S, p;
		cin >> N >> S >> p;

		int y = 0;
		for (int i = 0; i < N; i++)
		{
			int t;
			cin >> t;

			if (t >= 28)
			{
				y++;
				continue;
			}

			switch (t % 3)
			{
			case 0:
				if (t / 3 >= p)
					y++;
				else if (S && t / 3 && t / 3 == p - 1)
					S--, y++;
				break;
			case 1:
				if (t / 3 + 1 >= p)
					y++;
				break;
			case 2:
				if (t / 3 + 1 >= p)
					y++;
				else if (S && t / 3 == p - 2)
					S--, y++;
				break;
			};
		}

		cout << "Case #" << nTestCase << ": " << y << endl;
	}

	return 0;
}
