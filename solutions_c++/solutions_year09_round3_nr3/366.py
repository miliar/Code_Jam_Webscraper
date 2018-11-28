#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>

using namespace std;

#define INF (2000000000)

const int nmax = 10010;

int a[nmax];
bool b[nmax];
int c[nmax];
int p, q;

int check()
{
	memset(b, 0, sizeof(b));
	b[0] = b[p + 1] = true;
	int i, x, tL, tR;
	int ans = 0;
	for(i = 0; i < q; ++i)
	{
		x = a[ c[i] ];
		for(tL = x - 1; tL >= 0; --tL)
		{
			if (b[tL] == true)
			{
				break;
			}
		}
		for(tR = x + 1; tR < nmax; ++tR)
		{
			if (b[tR] == true)
			{
				break;
			}
		}
		ans += tR - tL - 2;
		b[x] = true;
	}
	return ans;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, tt;
	scanf("%d", &t);
	for(tt = 0; tt < t; ++tt)
	{
		scanf("%d%d", &p, &q);
		int i, x;
		memset(b, 0, sizeof(b));
		set<int> s;
		for(i = 0; i < q; ++i)
		{
			scanf("%d", &x);
			a[i] = x;
			s.insert(x);
		}
		b[0] = b[p + 1] = true;
/*
		s.insert(0);
		s.insert(p + 1);
		int j;
		int L, R;
		int tL, tR, g;
		stack<int> st;
		for(i = 0; i < q; ++i)
		{
			int mn = INF;
			for(set<int>::const_iterator cit = s.begin(); cit != s.end(); ++cit)
			{
				if (*cit != p + 1 && *cit)
				{
					tL = *s.lower_bound(*cit);
					tR = *s.upper_bound(*cit);
					g = tR - tL;
					if (g < mn)
					{
						mn = g;
						R = tR;
						L = tL;
						x = *cit;
					}
				}
			}
			st.push(x);
			s.erase(x);
		}
		int ans = 0;
		while(!st.empty())
		{
			x = st.top();
			st.pop();
			for(tL = x - 1; tL >= 0; --tL)
			{
				if (b[tL] == true)
				{
					break;
				}
			}
			for(tR = x + 1; tR < nmax; ++tR)
			{
				if (b[tR] == true)
				{
					break;
				}
			}
			ans += tR - tL - 2;
			b[x] = true;
		}
		*/
		int ans = INF;
		for(i = 0; i < q; ++i)
		{
			c[i] = i;
		}
		do
		{
			ans = min(ans, check());
		}while(next_permutation(c, c + q));
		printf("Case #%d: %d\n", tt + 1, ans);
		cerr << "finished " << tt + 1 << "\n";
	}
	return 0;
}