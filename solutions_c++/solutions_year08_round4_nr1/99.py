#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <vector>
#include <queue>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
const int INF = 1000000000;

typedef pair<int, int> pii;

#define all(s) s.begin(), s.end()

struct node
{
	bool op;
	int and;
	int value;
	int change;
	node () : op(false), value(0) { }
};

vector<node> a;
int n;
int dyn[10003][2];

int rec (int cur, int need)
{
	if (cur > n)
		return need ? INF : 0;

	if (!a[cur].op)
	{
		return a[cur].value == need ? 0 : INF;
	} else
	{
		if (dyn[cur][need] != -1)
			return dyn[cur][need];

		int ans = 2*INF;
		if (a[cur].and)
			if (need)
				ans = rec(2*cur, 1) + rec(2*cur+1, 1);
			else
				ans = min(rec(2*cur, 0), rec(2*cur+1, 0));
		else
			if (!need)
				ans = rec(2*cur, 0) + rec(2*cur+1, 0);
			else
				ans = min(rec(2*cur, 1), rec(2*cur+1, 1));
		
		if (a[cur].change)
		{
			int ans1;
			if (!a[cur].and)
				if (need)
					ans1 = rec(2*cur, 1) + rec(2*cur+1, 1) + 1;
				else
					ans1 = min(rec(2*cur, 0), rec(2*cur+1, 0)) + 1;
			else
				if (!need)
					ans1 = rec(2*cur, 0) + rec(2*cur+1, 0) + 1;
				else
					ans1 = min(rec(2*cur, 1), rec(2*cur+1, 1)) + 1;
			ans = min(ans, ans1);
		}

		if (ans > INF)
			ans = INF;
		return dyn[cur][need] = ans;
	}
}


int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		cerr << test << endl;
		int v;
		cin >> n >> v;
		memset(dyn, 255, sizeof(dyn));
		a.resize(n+1);
		for (int i = 0; i < (n-1)/2; ++i)
		{
			cin >> a[i+1].and >> a[i+1].change;
			a[i+1].op = true;
		}
		
		for (int i = (n - 1)/2; i < n; ++i)
		{
			cin >> a[i+1].value;
			a[i+1].op = false;
		}

		int res = rec(1, v);
		if (res < INF)
			printf("Case #%d: %d\n", test, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", test);
	}

}