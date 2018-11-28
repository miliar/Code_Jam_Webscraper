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

int mas[1001][1001];

int start(int t)
{
	int f = 0;
	for(int i = 1; i <= 1000; ++i)
	{
		for(int j = 1; j <= 1000; ++j)
			if(mas[i][j] == 1)
			{
				f = 1;
				break;
			}
		if(f)
			break;
	}
	if(f == 0)
		return t;
	for(int i = 1000; i > 0; --i)
		for(int j = 1000; j > 0; --j)
			if(mas[i][j])
			{
				if(mas[i - 1][j] == 0 && mas[i][j - 1] == 0)
					mas[i][j] = 0;
			}
			else
			{
				if(mas[i - 1][j] == 1 && mas[i][j - 1] == 1)
					mas[i][j] = 1;
            }
	return start(t + 1);
}

int Solution()
{
	int c;
	scanf("%d", &c);
	for(int i = 1; i <= c; ++i)
	{
		int r;
		scanf("%d", &r);
		for(int j = 1; j <= 1000; ++j)
			for(int k = 1; k <= 1000; ++k)
				mas[j][k] = 0;
		for(int j = 0; j < r; ++j)
		{
			int x1, x2, y1, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for(int k = y1; k <= y2; ++k)
				for(int l = x1; l <= x2; ++l)
					mas[k][l] = 1;
		}
		int res = start(0);
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
