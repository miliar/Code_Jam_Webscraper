#include <iostream>
using namespace std;

int RecyclePairs(int n, int b)
{
	int found[10];
	int ret = 0;

	int leftFactor = 1;
	for (int y = n; y > 0; y /= 10)
		leftFactor *= 10;

	int left = 0;
	int right = n;
	for (int digitFactor = 1; right >= 10; digitFactor *= 10)
	{
		leftFactor /= 10;
		int digit = (right % 10);
		right /= 10;
		left += digit * digitFactor;
		if (digit != 0)
		{
			int m = left * leftFactor + right;
			if (n < m && m <= b)
			{
				for (int i = 0; i < ret; ++i)
				{
					if (found[i] == m)
						goto already_found;
				}
				found[ret++] = m;
already_found:
				;
			}
		}
	}
	return ret;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int a, b;
		cin >> a >> b;
		int ret = 0;
		for (int x = a; x <= b; ++x)
		{
			ret += RecyclePairs(x, b);
		}
		cout << "Case #" << (t+1) << ": " << ret << endl;
	}
	return 0;
}
