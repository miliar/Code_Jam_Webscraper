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

int gcd(int a, int b)
{
	while(a % b)
	{
		a %= b;
		int t = a; a = b; b = t;
	}
	return b;
}

int Solution()
{
	int c;
	scanf("%d", &c);
	for(int i = 1; i <= c; ++i)
	{
		int n;
		scanf("%d", &n);
		vector<int> mas(n);
		for(int j = 0; j < n; ++j)
			scanf("%d", &mas[j]);
		sort(mas.rbegin(), mas.rend());
		int res = mas[0] - mas[1];
		for(int j = 0; j < n; ++j)
			for(int k = j + 1; k < n; ++k)
				if(mas[j] > mas[k])
					res = gcd(res, mas[j] - mas[k]);
		printf("Case #%d: %d\n", i, (mas[0] % res) == 0 ? 0 : res - mas[0] % res);
    }
	return 0;
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	Solution();
	return 0;
}
