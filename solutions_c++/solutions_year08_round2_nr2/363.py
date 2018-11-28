#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <set>
#include <stack>
#include <string>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

#define FOR(i, k, n) for(int i = (k); i < (n); i++)
#define FORZ(i, n) FOR(i, 0, n)
#define pb push_back
#define sz(x) x.size()
#define all(x) x.begin(), x.end()
#define cl(x) memset(x, 0, sizeof(x))

vector <vector <int> > arr;

int gcd(int a, int b)
{
	while(a > 0)
	{
		if(a < b)
			swap(a, b);
		a = a % b;
	}
	return b;
}

bool Prime(int x)
{
	FOR(i, 2, x)
		if(x % i == 0)
			return false;
	return true;
}

int Int(int a, int b)
{
	int ans = -1;
	int c = gcd(a, b);
	FOR(i, 2, c+1)
		if(c % i == 0)
			if(Prime(i))
				ans = i;
	return ans;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n, a, b, p;
	scanf("%d", &n);
	arr.resize(1001);
	FORZ(i, n)
	{
		int ans = 0;
		FORZ(j, 1001)
		{
			arr[j].clear();
			arr[j].pb(j);
		}
		scanf("%d%d%d", &a, &b, &p);
		bool flag = true;
		while(flag)
		{
			flag = false;
			FOR(j, a, b+1)
			{
				if(sz(arr[j]) == 0)
					continue;
				FOR(k,j+1,b+1)
				{
					if(sz(arr[k]) == 0)
						continue;
					FORZ(x, sz(arr[j]))
						FORZ(y, sz(arr[k]))
							if(Int(arr[j][x], arr[k][y]) >= p)
							{
								flag = true;
								FORZ(l, sz(arr[k]))
									arr[j].pb(arr[k][l]);
								arr[k].clear();
							}
				}
			}
		}
		FOR(j, a, b+1)
			if(sz(arr[j]) > 0)
				ans++;
		printf("Case #%d: %d\n", i+1, ans);
	}
	return 0;
}