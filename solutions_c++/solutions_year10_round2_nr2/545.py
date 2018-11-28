#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

int C, N, K, B, T;
vector<int> locations;
vector<int> speeds;

int calc()
{
	int count = 0;

	for (int i = N - 1; i >= N - K; --i)
	{
		if (speeds[i] * T >= B - locations[i])
			continue;

		bool found = false;
		for (int j = i - 1; j >= 0; --j)
		{
			if (speeds[j] * T >= B - locations[j])
			{
				for (int k = j; k < i; ++k)
				{
					swap(speeds[k], speeds[k + 1]);
					++count;
				}
				found = true;
				break;
			}
		}
		if (!found)
			return -1;
	}

	return count;
}

int main()
{
	cin >> C;

	for (int i = 1; i <= C; ++i)
	{
		cin >> N >> K >> B >> T;

		locations.resize(N);
		for (int j = 0; j < N; ++j)
			cin >> locations[j];

		speeds.resize(N);
		for (int j = 0; j < N; ++j)
			cin >> speeds[j];

		cout << "Case #" << i << ": ";
		int result = calc();
		if (result < 0)
			cout << "IMPOSSIBLE";
		else
			cout << result;
		cout << endl;
	}

	return 0;
}
