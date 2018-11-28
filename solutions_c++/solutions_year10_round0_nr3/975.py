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
		int r, k, n;
		scanf("%d%d%d", &r, &k, &n);
		vector<int> mas(n);
		for(int j = 0; j < n; ++j)
			scanf("%d", &mas[j]);
		lint res = 0;
		int l = 0, ri = 0, now = 0, cnt = 0;
		vector< pair<int, pair<int, int> > > s;
		while(r)
		{
			now += mas[ri];
			++cnt;
			if(cnt == n || now + mas[(ri + 1) % n] > k)
			{
				pair<int, int> tmp = mp(l, ri);
				pair<int, pair<int, int> > tmp2 = mp(now, tmp);
				int flag = -1;
				for(int x = 0; x < s.size(); ++x)
					if(s[x] == tmp2)
					{
						flag = x;
						break;
					}
				if(flag > -1)
				{
					lint tmp = 0;
					for(int x = flag; x < s.size(); ++x)
						tmp += (lint)s[x].first;
					lint tmp2 = r / (s.size() - flag);
					lint tmp3 = r % (s.size() - flag);
					res += tmp * tmp2;
					for(int x = flag; x < flag + tmp3; ++x)
						res += s[x % n].first;
					break;
				}
				s.pb(tmp2);
				res += now;
				now = 0;
				cnt = 0;
				--r;
				if(ri == n - 1)
					l = 0;
				else
					l = ri + 1;
			}
			if(ri == n - 1)
				ri = 0;
			else
				++ri;
		}
		printf("Case #%d: %I64d\n", i, res);
	}
	return 0;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	Solution();
	return 0;
}
