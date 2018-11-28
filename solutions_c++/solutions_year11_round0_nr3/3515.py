#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int xor_sum(const vector<int>& vi)
{
	int s = 0;

	if (vi.size() == 0)
		return 0;

	s = vi[0];

	for (int i = 1; i < vi.size(); i++)
	{
		s ^= vi[i];
	}

	return s;
}

int sum(const vector<int>& vi)
{
	int s = 0;

	if (vi.size() == 0)
		return 0;

	s = vi[0];

	for (int i = 1; i < vi.size(); i++)
	{
		s += vi[i];
	}

	return s;
}

bool compare(int a, int b)
{
	int i = 1;

	while(i <= a || i <= b)
	{
		bool fora = (i & a);
		bool forb = (i & b);

		if (fora == false && forb == true)
			return true;
		else if (fora == true && forb == false)
			return false;

		i <<= 1;
	}

	return false;
}

int main()
{
	int c, t, n, i;

	cin >> t;
	for (c = 1; c <= t; c++)
	{
		int m = -1;
		vector<int> num;

		cin >> n;
		num.resize(n);
		for (i = 0; i < n; i++)
		{
			cin >> num[i];
		}

		if (xor_sum(num) == 0)
		{
			for (i = 0; i < num.size(); i++)
			{
				int xors = xor_sum(num) ^ num[i];
				int s = sum(num) - num[i];

				if (xors == num[i] && s > m)
					m = s;
			}
		}

		cout << "Case #" << c << ": ";
		if (m > -1)
			cout << m << endl;
		else
			cout << "NO\n";
	}

	return 0;
}
