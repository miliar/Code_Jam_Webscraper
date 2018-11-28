#include <iostream>
#include <vector>

using namespace std;

int c;
int n, k;
double b, T;
int result;
int will_arrive;
int current;
vector<double> pos, v, t;

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);

	cin >> c;

	for (int i = 0; i < c; i++)
	{
		cin >> n >> k >> b >> T;

		result = 0;

		pos.clear();
		v.clear();
		t.clear();

		pos.resize(n);
		v.resize(n);
		t.resize(n);

		for (int j = 0; j < n; j++)
			cin >> pos[j];

		for (int j = 0; j < n; j++)
			cin >> v[j];

		for (int j = 0; j < n; j++)
		{
			t[j] = (b - pos[j]) / v[j];
		}

		current = 0;
		will_arrive = 0;

		for (int j = n - 1; j >= 0; j--)
		{
			if (t[j] > T)
				current++;
			else
			{
				result += current;
				will_arrive++;
			}

			if (will_arrive >= k)
				break;
		}

		cout << "Case #" << i + 1 << ": ";

		if (will_arrive < k)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << result << endl;
	}

	return 0;
}