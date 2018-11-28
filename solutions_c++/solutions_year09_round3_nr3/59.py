#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;

int p, q;
map <int, int> biect;
vector <int> num;
vector <vector <long long> > dp;

long long Func(int l, int r)
{
	if(l + 1 >= r)
		return 0;
	if(dp[l][r] != -1)
		return dp[l][r];
	long long ans = 1e9;
	ans *= 1e9;
	for(int i = l + 1; i < r; i++)
		ans = min(ans, Func(l, i) + Func(i, r) + num[r] - num[l] - 2);
	return dp[l][r] = ans;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		cin >> p >> q;
		dp.assign(q + 3, vector <long long>(q + 3, -1));
		num.clear();
		biect.clear();
		set <int> now;
		for(int j = 0; j < q; j++)
		{
			int x;
			cin >> x;
			now.insert(x);
		}
		int cnt = 0;
		num.push_back(0);
		for(set <int>::iterator it = now.begin(); it != now.end(); it++)
		{
			biect[*it] = cnt++;
			num.push_back(*it);
		}
		num.push_back(p + 1);
		printf("Case #%d: ", i + 1);
		cout << Func(0, q + 1) << endl;
	}
	return 0;
}