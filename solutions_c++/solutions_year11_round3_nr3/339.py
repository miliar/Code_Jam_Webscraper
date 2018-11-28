#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	int n, l, h;
	vector<int> v;
	for(int test = 1; test <= t; test++)
	{
		cin >> n >> l >> h;
		v.clear();
		v.resize(n);
		for(int i = 0; i < n; i++)
			cin >> v[i];
		int res = -1;
		for(int i = l; i <= h; i++)
		{
			bool f = true;
			for(int j = 0; j < v.size(); j++)
			{
				if(v[j] % i != 0 && i % v[j] != 0)
				{
					f = false;
					break;
				}
			}
			if(f)
			{
				res = i;
				break;
			}
		}
		cout << "Case #" << test << ": ";
		if(res == -1)
			cout << "NO" << endl;
		else
			cout << res << endl;
	}
	return 0;
}