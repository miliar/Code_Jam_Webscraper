#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minimun(vector<int>& vx,
			vector<int>& vy)
{
	sort(vx.begin(), vx.end());
	sort(vy.begin(), vy.end());

	vector<int>::const_iterator i = vx.begin();
	vector<int>::reverse_iterator j = vy.rbegin();

	int ret = 0;
	while (i != vx.end() && j != vy.rend())
	{
		ret += ((*i) * (*j));
		++i;
		++j;
	}

	return ret;
}

int main()
{
	int T;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		int n;
		cin >> n;

		vector<int> vx, vy;
		for (int j = 0; j < n; ++j)
		{
			int x;
			cin >> x;
			vx.push_back(x);
		}
		for (int j = 0; j < n; ++j)
		{
			int y;
			cin >> y;
			vy.push_back(y);
		}

		cout << "Case #" << i + 1 << ": ";
		cout << minimun(vx, vy) << "\n";
	}

	return 0;
}