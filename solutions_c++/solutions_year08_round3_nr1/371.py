#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testNum;
	cin >> testNum;

	for (int testId = 1; testId <= testNum; testId++)
	{
		int maxLen, keyNum, letNum;
		cin >> maxLen >> keyNum >> letNum;

		vector<int> freq;
		freq.resize(letNum);

		for (int i = 0; i < letNum; i++)
		{
			cin >> freq[i];
		}

		sort(freq.begin(), freq.end(), greater<int>());

		long long res = 0;
		long long loop = 1;
		bool impossible = false;

		for (int i = 0; i < letNum; i++)
		{
			if (loop > maxLen)
			{
				impossible = true;
				break;
			}

			res += freq[i] * loop;

			if ((i + 1) % keyNum == 0)
			{
				loop++;
			}
		}

		cout << "Case #" << testId << ": ";

		if (impossible)
		{
			cout << "Impossible" << endl;
		}
		else
		{
			cout << res << endl;
		}
	}

	return 0;
}