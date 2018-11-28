#include <iostream>
using namespace std;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("BLarge.out", "w", stdout);
	int t;
	const int AB = 26;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		char combine[AB][AB];
		bool opposed[AB][AB];
		char str[4];
		for (int j = 0; j < AB; j++)
			for (int k = 0; k < AB; k++)
			{
				combine[j][k] = 0;
				opposed[j][k] = false;
			}
		int c, d, n;
		cin >> c;
		for (int j = 0; j < c; j++)
		{
			cin >> str;
			combine[str[0] - 'A'][str[1] - 'A'] = str[2];
			combine[str[1] - 'A'][str[0] - 'A'] = str[2];
		}
		cin >> d;
		for (int j = 0; j < d; j++)
		{
			cin >> str;
			opposed[str[0] - 'A'][str[1] - 'A'] = true;
			opposed[str[1] - 'A'][str[0] - 'A'] = true;
		}
		char series[101];
		char list[101];
		int size = 0;
		cin >> n;
		cin >> series;
		for (int j = 0; series[j]; j++)
			if (j && combine[series[j] - 'A'][list[size - 1] - 'A'])
				list[size - 1] = combine[series[j] - 'A'][list[size - 1] - 'A'];
			else
			{
				list[size++] = series[j];
				for (int k = 0; k < size - 1; k++)
					if (opposed[series[j] - 'A'][list[k] - 'A'])
						size = 0;
			}
		cout << "Case #" << i + 1 << ": [";
		for (int j = 0; j < size; j++)
		{
			if (j)
				cout << ", ";
			cout << list[j];
		}
		cout << "]\n";
	}
	return 0;
}