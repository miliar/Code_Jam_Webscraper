#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
#include <list>
#include <queue>
#include <stack>
#include <sstream>
#include <cmath>
#include <deque>
#include <bitset>
#include <string>
using namespace std;

int n, k, b, T, i;
vector<pair<int, int> > a;
vector<bool> canReach;
vector<int> cost;
int notReaching;

bool reachable(int i)
{
	int x = a[i].first;
	int v = a[i].second;
	int reach = x + (long long)v * T;
	return reach >= b;
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	cin >> t;
	for(int TI = 1; TI <= t; ++ TI)
	{
		cin >> n >> k >> b >> T;

		a.resize(n);
		canReach.resize(n);
		cost.resize(n);
		for(i=0;i<n;++i)
			cin >> a[i].first;
		for(i=0;i<n;++i)
			cin >> a[i].second;

		notReaching = 0;
		for(i=n-1;i>=0;--i)
			if(reachable(i))
			{
				canReach[i] = true;
				cost[i] = notReaching;
			}
			else
			{
				canReach[i] = false;
				++ notReaching;
			}

		if(n - notReaching < k)
			cout << "Case #" << TI << ": IMPOSSIBLE" << endl;
		else
		{
			int best = 0;
			i = n - 1;
			while(k)
			{
				if(canReach[i])
					best += cost[i], 
					-- k;
				-- i;
			}


			cout << "Case #" << TI << ": " << best << endl;
		}
	}
	return 0;
}
