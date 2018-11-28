#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <map>
#include <sstream>
#include <set>

#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define EPS 1e-9

using namespace std;

typedef pair <int, int> pii;
typedef vector <int> vi;
typedef vector <vi> vvi;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int z = 0; z < t; z++)
	{
		printf("Case #%d: ", z+1);
		int n, m;
		scanf("%d %d ", &n, &m);
		set <string> s;
		for (int i = 0; i < n; i++)
		{
			string t, res = "/";
			cin >> t;
			for (int j = 1; j < sz(t); j++)
			{
				if (t[j] != '/')
				{
					res += t[j];
					continue;
				}
				s.insert(res);
				res += t[j];
			}
			s.insert(res);
		}
		int ans = 0;
		for (int i = 0; i < m; i++)
		{
			string t, res = "/";
			cin >> t;
			for (int j = 1; j < sz(t); j++)
			{
				if (t[j] != '/')
				{
					res += t[j];
					continue;
				}
				if (s.find(res) == s.end()) 
				{
					ans++;
					s.insert(res);
				}
				res += t[j];

			}
			if (s.find(res) == s.end()) 
			{
				ans++;
				s.insert(res);
			}
			
		}
		printf("%d\n", ans);
	}
	return 0;
}
