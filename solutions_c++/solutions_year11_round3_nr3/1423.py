#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	freopen("C.txt","r",stdin);
	freopen("cout.txt","w",stdout);

	int t, n, l, h;
	int i, j, k;
	int a[10000];
	bool fail;
	bool su;
	cin >> t;
	for (int ca = 1; ca <=t; ++ca)
	{
		fail = false;
		cin >> n >> l >> h;
		for (i = 0; i < n; ++i)
			cin >> a[i];

		for (i = l; i <=h; ++i)
		{
			for (j = 0; j < n; ++j)
			{
				if (i % a[j] == 0 || a[j] % i == 0)
					continue;
				else
					break;
			}

			if (j == n)
				break;
		}

		cout << "Case #" << ca << ": ";

		if (j == n)
		{
			cout << i << endl;
		}
		else
		{
			cout << "NO" << endl;
		}
	}
	return 0;
}