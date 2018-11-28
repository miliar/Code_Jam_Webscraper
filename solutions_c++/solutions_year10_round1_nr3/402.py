#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <stack>
#include <vector>
#include <queue>
#include <deque>
#include <string>
#include <bitset>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#define pb push_back
#define mp make_pair
typedef long long lint;

using namespace std;

int check(int a, int b)
{
	if(b > a)
	{
		int t = a; a = b; b = t;
	}
	if(a % b == 0)
		if(a != b)
			return 1;
		else
			return 0;
	vector<int> mas;
	while(a % b)
	{
		int now = a / b;
		if(now > 1)
			mas.pb(now);
		else
			if(mas.size())
				if(mas[mas.size() - 1] == 1)
					mas.pop_back();
				else
					mas.pb(1);
			else
				mas.pb(1);
		a %= b;
		int t = a; a = b; b = t;
	}
	if(mas.size() == 0)
		if(a != b)
			return 1;
		else
			return 0;
	if(mas[0] > 1)
		return 1;
	return 0;
}

int Solution()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
	{
		int a1, a2, b1, b2;
		scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
		int res = 0;
		for(int j = a1; j <= a2; ++j)
			for(int k = b1; k <= b2; ++k)
				res += check(j, k);
		printf("Case #%d: %d\n", i, res);
    }
	return 0;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	Solution();
	return 0;
}
