#include <iostream>
#include <string>
#include <map>
using namespace std;

map<pair<int,int>, int> dp;
int p, n;
int q[300];

int f(int start, int end)
{
	if(end < start) return 0;
	pair<int, int> pr = make_pair(start, end);
	if(dp.find(pr) == dp.end())
	{
		int mn = 1e9;
		for(int i=0;i<n;i++)
		{
			if(q[i] >= start && q[i] <= end)
			{
				mn = min(mn, f(start, q[i]-1) + f(q[i]+1, end));
			}
		}
		if(mn < 1e8) 
		{
			dp.insert(make_pair(pr, end - start + mn));
		}
	}
	return dp[pr];
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int tt;
	cin>>tt;
	for(int t=1;t<=tt;t++)
	{
		dp.clear();
		
		cin>>p>>n;
		for(int i=0;i<n;i++)
		{
			cin>>q[i];
		}
		printf("Case #%d: %I64d\n", t, f(1, p));
	}
	return 0;
}