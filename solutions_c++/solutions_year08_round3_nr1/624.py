#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Key
{
	int pos;
	long long freq;
};

int cmp(const Key &lhs, const Key &rhs)
{
	return lhs.freq > rhs.freq;
}

int main()
{
	int N;
	cin >> N;

	int caseNum = 1;

	do
	{
		int P, K, L;

		cin >> P >> K >> L;

		vector<Key> keys;
		for (int i = 0; i < L; ++i)
		{
			Key newKey;
			newKey.pos = i;
			cin >> newKey.freq;
			keys.push_back(newKey);
		}
		sort(keys.begin(), keys.end(), cmp);

		long long result = 0;
		int curKey = 0;
		int curPos = 1;
		bool continued = true;
		while(continued)
		{
			for (int i = 0; i < K; ++i)
			{
				if (curKey == keys.size())
				{
					continued = false;
					break;
				}
				result += keys[curKey++].freq * curPos;
			}
			++curPos;
		}

		printf("Case #%d: %d\n", caseNum++, result);
	} while (caseNum <= N);

	return 0;
}

