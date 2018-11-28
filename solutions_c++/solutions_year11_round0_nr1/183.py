#include <iostream>
#include <algorithm>

using namespace std;

int solve()
{
	int n;
	cin >> n;
	int ans = 0;
	int pos[2] = {1, 1};
	int time[2] = {0, 0};
	for (int i = 0; i < n; ++i)
	{
		char c;
		int r, p;
		cin >> c >> p;
		r = c == 'O' ? 0 : 1;
		int t = abs(pos[r] - p) + 1;
		cerr << "time = " << "{" << time[0] << ", " << time[1] << "} t = " << t << endl;
		ans += time[r ^ 1];
		if (t <= time[r ^ 1])
			time[r] = 1;
		else
			time[r] += t - time[r ^ 1];
		pos[r] = p;
		time[r ^ 1] = 0;
	}
	return ans + time[0] + time[1];
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		cout << "Case #" << i << ": " << solve() << endl;
	return 0;
}
