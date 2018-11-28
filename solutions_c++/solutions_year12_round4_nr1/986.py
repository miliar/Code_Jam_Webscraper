#include <iostream>
#include <queue>
using namespace std;

#define min(a, b) ((a) < (b) ? (a) : (b))

const int MAX = 10001;
int ds[MAX];
int rs[MAX];
priority_queue< pair<int, int> > ropes; // first = -d, second = radius

void add(int d, int r)
{
	ropes.push(pair<int, int>(-d, r));
}

int furthest(int d)
{
	pair<int, int> res;
	while (!ropes.empty() && -ropes.top().first + ropes.top().second < d)
	{
		ropes.pop();
	}

	if (ropes.empty())
	{
		return -1;
	}

	return -ropes.top().first;
}

int main()
{
	int cases;
	cin >> cases;

	for (int c = 1; c <= cases; c++)
	{
		ropes = priority_queue< pair<int, int> >();

		int n;
		cin >> n;

		for (int i = 0; i < n; i++)
		{
			cin >> ds[i] >> rs[i];
		}
		cin >> ds[n];

		int start;
		add(ds[0], ds[0]);

		for (int i = 0; i <= n; i++)
		{
			start = furthest(ds[i]);
			if (start == -1) break;

			if (i < n) add(ds[i], min(rs[i], ds[i] - start));
		}


		cout << "Case #" << c << ": ";

		if (start == -1)
		{
			cout << "NO\n";
		}
		else
		{
			cout << "YES\n";
		}
	}

	return 0;
}
