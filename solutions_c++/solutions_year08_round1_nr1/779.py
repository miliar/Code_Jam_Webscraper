#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int T, n;
	cin >> T;

	int v1[256], v2[256];

	for(int i = 0; i < T; i++)
	{
		cin >> n;

		for(int j = 0; j < n; j++)
		{
			cin >> v1[j];
		}

		for(int j = 0; j < n; j++)
		{
			cin >> v2[j];
		}

		sort<int*>(&v1[0], &v1[n]);
		sort<int*>(&v2[0], &v2[n]);

		int s = 0;
		for(int j = 0; j < n; j++)
		{
			s += v1[j]*v2[n - 1 - j];
		}

		cout << "Case #" << i + 1 << ": " << s << endl;
	}

	return 0;
}