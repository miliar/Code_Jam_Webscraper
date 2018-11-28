#include <iostream>
#include <deque>
using namespace std;
int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t;
	cin >> t;
	deque<int> g;
	for (int i = 1; i <= t; i++)
	{
		int n, k, r;
		cin >> r >> k >> n;
		g.clear();
		g.resize(n);
		for (int j = 0; j < n; j++)
			cin >> g[j];
		int total = 0;
		for (int j = 0; j < r; j++)
		{
			int x = 0, in = 0;
			while (x < n && in <= k)
			{
				int tmp = g.front();
				in += tmp;
				if (in > k)
					break;
				x++;
				total += tmp;
				g.pop_front();
				g.push_back(tmp);
			}
		}
		cout << "Case #" << i << ": " << total << endl; 
	}
	return 0;
}