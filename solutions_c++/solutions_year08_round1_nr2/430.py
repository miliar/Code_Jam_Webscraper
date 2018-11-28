#include <cassert>
#include <iostream>
#include <list>

using namespace std;

int main()
{
	int **a = new int *[2000];

	for (int i = 0; i < 2000; i++)
	{
		a[i] = new int[2000];
	}

	int shakes[2000], maltedId[2000];
	bool state[2000];

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testNum;
	cin >> testNum;

	for (int testId = 1; testId <= testNum; testId++)
	{
		int n, m;
		cin >> n >> m;

		for (int i = 0; i < m; i++)
		{
			memset(a[i], 0, n * sizeof(int));
		}

		memset(shakes, 0, m * sizeof(int));
		memset(state, 0, n * sizeof(bool));

		for (int i = 0; i < m; i++)
		{
			maltedId[i] = -1;
		}

		for (int i = 0; i < m; i++)
		{
			int k;
			cin >> k;

			for (int j = 0; j < k; j++)
			{
				int x, y;
				cin >> x >> y;

				if (y == 0)
				{
					a[i][x - 1] = -1;
					shakes[i]++;
				}
				else
				{
					a[i][x - 1] = 1;
					maltedId[i] = x - 1;
				}
			}
		}

		list<int> zeroShakes;

		for (int i = 0; i < m; i++)
		{
			if (shakes[i] == 0)
			{
				zeroShakes.push_back(i);
			}
		}

		bool impossible = false;

		for (list<int>::const_iterator i = zeroShakes.begin(); i != zeroShakes.end(); i++)
		{
			_ASSERT(shakes[*i] == 0);

			if (maltedId[*i] == -1)
			{
				impossible = true;
				break;
			}

			int malted = maltedId[*i];
			shakes[*i]++;			
			state[malted] = true;

			for (int j = 0; j < m; j++)
			{
				if (a[j][malted] == -1)
				{
					if (--shakes[j] == 0)
					{
						zeroShakes.push_back(j);
					}
				}
				else if (a[j][malted] == 1)
				{
					if (shakes[j] == 0)
					{
						shakes[j]++;
						zeroShakes.remove(j);
					}
				}
			}
		}

		cout << "Case #" << testId << ':';

		if (impossible)
		{
			cout << " IMPOSSIBLE" << endl;
		}
		else
		{
			for (int i = 0; i < m; i++)
			{
				_ASSERT(shakes[i] > 0);
			}

			for (int i = 0; i < n; i++)
			{
				cout << ' ' << state[i] ? 1 : 0;
			}

			cout << endl;
		}
	}

	return 0;
}