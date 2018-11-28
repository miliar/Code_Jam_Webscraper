#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

void solve(int tc)
{
	int r, k, n;
	cin >> r >> k >> n;
	vector<int> g(2*n);
	for(int i = 0; i < n; i++)
	{
		cin >> g[i];
		g[i+n] = g[i];
	}
	vector<int> next(n);
	vector<int> sum(n);
	for(int i = 0; i < n; i++)
	{
		sum[i] = 0;
		int j = i;
		while (j < i + n && sum[i] + g[j] <= k)
		{
			sum[i] += g[j];
			j++;
		}
		next[i] = j % n;
	}
	vector<int> used(n, -1);
	vector<long long> s(n, 0);
	int pos = 0;
	used[pos] = 0;
	long long ans = 0;
	int step = 0;
	while (r > 0) {
		int nx = next[pos];
		if (used[nx] == -1)
		{
			used[nx] = ++step;
			ans += sum[pos];
			s[nx] = s[pos] + sum[pos];
			pos = nx;
			r--;
		}
		else
		{
			ans += sum[pos];
			r--;
			int len = ++step - used[nx];
			ans += (r / len) * (s[pos] + sum[pos] - s[nx]);
			r = r % len;
			pos = nx;
			used = vector<int>(n, -1);
		}
	}
	printf("Case #%d: ", tc);
	cout << ans << endl;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tc; cin >> tc;
	for(int it = 0; it < tc; it++)
	{
		solve(it+1);
	}
	return 0;
}
