#include <iostream>
#include <vector>
#include <map>
using namespace std;

int n, D;
vector< pair<int,int> > v;
map< pair<int,int>, int > dp;

int get(int a, int b)
{
	pair<int,int> p(a,b);
	if (dp.find(p) != dp.end()) return dp[p];
	if (a == v.size()-1) return dp[p] = 1;
	
	int ret = 0;
	for (int i = a+1; i < v.size(); ++i)
		if ( v[i].first - v[a].first <= b )
		{
			ret = get(i, min(v[i].first - v[a].first, v[i].second));
			if (ret) break;
		}
		else break;
	return dp[p] = ret;
}

int main()
{
	int T; cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cin >> n;
		v.resize(n);
		for (int i = 0; i < n; ++i)
			cin >> v[i].first >> v[i].second;
		cin >> D;
		v.push_back(make_pair(D, 0));
		
		dp.clear();
		int ret = get(0, v[0].first);
		cout << "Case #" << t << ": ";
		if (ret) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
}

