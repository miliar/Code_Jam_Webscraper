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

int buy[2100];

int Solution()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
	{
		int p;
		scanf("%d", &p);
		int s = 1 << p;
		vector<int> mas(s);
		for(int j = 0; j < s; ++j)
			scanf("%d", &mas[j]);
		s /= 2;
		vector<vector<int> > cost(p, vector<int>(s));
		for(int j = 0; j < p; j++)
		{
			int x;
			for(int k = 0; k < s; ++k)
				scanf("%d", &x);
			s /= 2;
		}
		int res = 0;
		for(int j = 0; j < 2010; ++j)
			buy[j] = 0;
		for(int j = 0; j < 1 << p; ++j)
		{
			int c = 0, ind = (j - 2 + (1 << p)) / 2;
			for(int k = p; k > 0; k--, ind = (ind - 1) / 2)
				if(buy[ind])
					c++;
			if(p - c > mas[j])
			{
				int cnt = p - c - mas[j];
				int ind = (j - 2 + (1 << p)) / 2;
				vector<int> index;
				for(int k = p; k > 0; k--, ind = (ind - 1) / 2)
					index.pb(ind);
				for(int k = index.size() - 1; k >= 0; --k)
					if(buy[index[k]] == 0)
					{
						buy[index[k]] = 1;
						res++;
						cnt--;
						if(cnt == 0)
							break;
					}
			}
		}
		printf("Case #%d: %d\n", i, res);
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
