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
typedef vector <pii> vpii;

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
		long long n, k, b, time;
		scanf("%lld %lld %lld %lld", &n, &k, &b, &time);
		vi x(n);
		vi v(n);
		for (int i = 0; i < n; i++)
			scanf("%d ", &x[i]);
		for (int i = 0; i < n; i++)
			scanf("%d ", &v[i]);
		int res = 0;
		for (int i = 0; i < n; i++)
		{
			if (x[i] + v[i]*time >= b) res++; 
		}
		if (res < k)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		vi can;
		int ans = 0;
		for (int i = 0; i < sz(x); i++)
		{
			if (x[i] + v[i]*time < b) continue;
			can.push_back(x[i]);
			x.erase(x.begin() + i);
			v.erase(v.begin() + i);
			i--;
		}
		vi canK;
		for (int i = 0; i < k; i++)
			canK.push_back(can[sz(can) - 1 - i]);
		for (int i = 0; i < sz(x); i++)
		{
			for (int j = 0; j < sz(canK); j++)
				if (x[i] > canK[j]) ans++;
		}
		printf("%d\n", ans);
		
	}
	return 0;
}
