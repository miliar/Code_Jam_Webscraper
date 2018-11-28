#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;


vector <int> s;
vector <pair<int,int>> sr;

int ans = 0;

int dfs(int u)
{
	if (u == s.size())
	{
		if (sr.size() == 0)  return 0;
		int vs = sr[0].second;
		for (int i = 1; i < sr.size(); i ++)
			vs = min(vs, sr[i].second);
		ans = max(ans, vs);
		return 0;
	}
	for (int i = 0; i < sr.size(); i ++)
		if (sr[i].first + 1 == s[u])
		{
			sr[i].first = s[u];
			sr[i].second ++;
			dfs(u + 1);
			sr[i].first --;
			sr[i].second --;
		}
	sr.push_back(pair<int,int>(s[u], 1));
	dfs(u + 1);
	sr.pop_back();
	return 0;
}

int work()
{
	int N;
	cin >> N;
	s.clear();  sr.clear();
	for (int i = 0, x; i < N; i ++)
	{
		cin >> x;
		s.push_back(x);
	}
	sort(s.begin(), s.end());
	ans = 0;
	dfs(0);
	return ans;
}

int main()
{
	freopen("b1.txt", "r", stdin);
	freopen("b1.ans", "w", stdout);
	int T;
	cin >> T;
	for (int k = 1; k <= T; k ++)
		cout << "Case #" << k << ": " << work() << endl;
	return 0;
}