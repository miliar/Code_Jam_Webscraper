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

int Solution()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		if((k + 1) % (1 << n))
			printf("Case #%d: OFF\n", i);
		else
			printf("Case #%d: ON\n", i);
	}
	return 0;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	Solution();
	return 0;
}
