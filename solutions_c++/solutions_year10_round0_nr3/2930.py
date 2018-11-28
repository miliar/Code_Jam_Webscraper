#include <iostream>
#include <deque>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test)
	{
		int r, k, n;
		cin >> r >> k >> n;
		deque<int> q;
		for (int i = 0; i < n; ++i)
		{
			int t;
			cin >> t;
			q.push_back(t);
		}
		int res = 0;
		for (int i = 0; i < r; ++i)
		{
			int c = 0, j = 0;
			while (c + q.front() <= k && j < (int)q.size())
			{
				++j;
				c += q.front();
				q.push_back(q.front());
				q.pop_front();
			}
			res += c;
		}
		cout << "Case #" << test << ": " << res << endl;
	}
	return 0;
}