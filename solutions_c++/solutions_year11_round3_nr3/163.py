# include <iostream>
# include <stdio.h>
# include <string>

using namespace std;

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test)
	{
		int n, l, h;
		cin >> n >> l >> h;
		int a[101];
		for (int i = 0; i < n; ++i)
			cin >> a[i];

		bool success = false;
		for (int i = l; i <= h; ++i)
		{
			bool harmony = true;
			for (int j = 0; j < n; ++j)
				if (a[j] % i != 0 && i % a[j] != 0)
				{
					harmony = false;
					break;
				}
			if (harmony)
			{
				success = true;
				cout << "Case #" << test << ": " << i << endl;
				break;
			}
		}
		
		if(!success)
			cout << "Case #" << test << ": NO" << endl;
	}
	return 0;
}