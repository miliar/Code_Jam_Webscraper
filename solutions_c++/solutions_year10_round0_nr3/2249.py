#include <iostream>
#include <queue>
#include <cstdlib>

using namespace std;

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	int T;
	cin >> T;

	int R, k, N;

	queue<int> q;
	queue<int> d;
	for ( int i = 1; i <= T; i++)
	{
		long long count = 0;
		while (!q.empty())
		{
			q.pop();
		}

		while (!d.empty())
		{
			d.pop();
		}

		cin >> R >> k >> N;
		int g;
		for ( int j = 0; j < N; j++)
		{
			cin >> g;
			q.push(g);
		}

		for ( int l = 0; l < R; l++)
		{
			int c = 0;
			while ( !q.empty() && c + q.front() <= k)
			{
				c += q.front();
				d.push(q.front());
				q.pop();
			}
			count += c;
			while ( !d.empty())
			{
				q.push(d.front());
				d.pop();
			}
		}

		cout << "Case" << " " << "#" << i << ":" << " " << count << endl;
	}
}