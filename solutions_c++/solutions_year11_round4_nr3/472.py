#include <iostream>

using namespace std;

int t;

int mas[1001];

int cal(int x, int v)
{
	int r = 0;

	while (v >= x)
	{
		v /= x;
		r++;
	}

	return r;
}

int main()
{
	freopen("C1.in", "rt", stdin);
	freopen("C1.out", "wt", stdout);

	cin >> t;

	for (int i = 2; i < 40; i++)
	{
		if (mas[i] == 0)
		{
			for (int j = i*2; j <= 1000; j += i)
			{
				mas[j] = 1;
			}
		}
	}

	int n;

	for (int i = 1; i <= t; i++)
	{
		cin >> n;
		int rez = 0;
		int sk = 0;

		for (int j = 2; j <= n; j++)
		{
			if (mas[j] == 0)
			{
				rez += cal(j, n);
				sk++;
			}
		}

		if (n > 1)
		{
			rez++;
		}

		cout << "Case #" << i << ": " << rez - sk << endl;
	}

	return 0;
}