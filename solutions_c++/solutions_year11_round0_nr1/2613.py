#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <memory.h>
#include <deque>
#include <cstdio>

using namespace std;

int main()
{
	int test;
	freopen("input.txt", "rt", stdin);
	freopen("ouput.txt", "wt", stdout);
	scanf("%d", &test);
	for (int t = 0; t < test; t++)
	{
		int n;
		scanf("%d", &n);
		deque<int> b, o;
		deque<pair<int, char> > v;
		int bpos = 1, opos = 1;
		for (int i = 0; i < n; i++)
		{
			int c;
			char s[4];
			scanf("%s", s);
			scanf("%d", &c);
			v.push_back(make_pair(c, s[0]));
			if (s[0] == 'O')
			{
				o.push_back(c);
			}
			else
				b.push_back(c);
		}
		int ans = 0;
		while (!v.empty())
		{
			if (b.empty())
			{
				ans += abs(opos - o[0]) + 1;
				opos = o[0];
				o.pop_front();
				v.pop_front();
				continue;
			}
			if (o.empty())
			{
				ans += abs(bpos - b[0]) + 1;
				bpos = b[0];
				b.pop_front();
				v.pop_front();
				continue;
			}
			int w;
			if (v[0].second == 'O')
			{
				w = abs(opos - o[0]);
				ans += w;
				opos = o[0];
				o.pop_front();
				int ww = abs(bpos - b[0]);
				bpos = b[0] + ww;
				bpos -= w;
				if (bpos < b[0])
					bpos = b[0];
				++ans;
				if (bpos > b[0])
					--bpos;
				v.pop_front();
			}
			else
			{
				w = abs(bpos - b[0]);
				ans += w;
				bpos = b[0];
				b.pop_front();
				opos = o[0] + abs(opos - o[0]);
				opos -= w;
				if (opos < o[0])
					opos = o[0];
				++ans;
				if (opos > o[0])
					--opos;
				v.pop_front();
			}


		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
  return 0;
}
