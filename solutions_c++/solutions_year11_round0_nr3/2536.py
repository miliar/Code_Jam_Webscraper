#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
using namespace std;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int test = 1; test <= t; test++)
	{
		int n;
		cin >> n;
		vector<int> v(n);
		for(int i = 0; i < n; i++)
			cin >> v[i];
		int x = v[0];
		for(int i = 1; i < (int)v.size(); i++)
			x ^= v[i];
		if(x != 0)
		{
			cout << "Case #" << test << ": NO" << endl;
			continue;
		}
		int minc = v[0];
		int sum = v[0];
		for(int i = 1; i < (int)v.size(); i++)
		{
			sum += v[i];
			minc = min(minc, v[i]);
		}
		sum -= minc;
		cout << "Case #" << test << ": " << sum << endl;
	}
	return 0;
}