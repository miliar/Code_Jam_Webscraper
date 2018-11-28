#include <iostream>
#include <set>
#include <string>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

string name = "b";

long long INF = 1 << 30;

vector<int> m;
int n, p;

int mis[1 << 10];
int cost[20][1 << 10];

long long memo[20][1 << 10][20];

long long find(int p, int x, int ms)
{
	if (p == 0)
	{
		if (ms <= mis[x]) return 0;
		return INF;
	}
	
	if (memo[p][x][ms] >= 0) return memo[p][x][ms];
	long long& res = memo[p][x][ms];
	res = INF;
	
	res = find(p - 1, x * 2, ms) + find(p-1, x*2 + 1, ms) + cost[p][x];
	res = min(res, find(p - 1, x * 2, ms + 1) + find(p-1, x*2 + 1, ms + 1));
	
	return res;
}

void solve()
{
	memset(memo, -1, sizeof memo);
	
	cin >> n;
	p = n;
	n = 1 << n;
	for (int i = 0; i < n; i++)
		cin >> mis[i];
	
	for (int i = 1; i <= p; i++)
	{
		for (int j = 0; j < 1 << (p - i); j++)
			cin >> cost[i][j];
	}
	
	long long res = find(p, 0, 0);
	cout << res << endl;
}

int main()
{
	INF *= 100;
	
	freopen((name + ".in").c_str(), "r", stdin);
	freopen((name + ".out").c_str(), "w", stdout);
	
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		cout << "Case #" << test << ": ";
		solve();
	}
	return 0;
}