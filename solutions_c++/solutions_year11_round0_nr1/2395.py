#include <iostream>
#include <stack>
#include <vector>
#include <cstdio>

using namespace std;

int 
main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-small-attempt0.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i)
	{
		int n;
		cin >> n;
		vector<pair<char, int> > st(n);
		stack <int> o;
		stack <int> b;
		
		for(int j = 0; j < n; ++j)
		{
			cin >> st[j].first >> st[j].second;
		}
		for(int j = n - 1; j >= 0; --j)
		{
			if(st[j].first == 'O')
			{
				o.push(st[j].second);
			}
			else
			{
				b.push(st[j].second);
			}
		}
		int ans = 0;
		bool f;
		int x1 = 1;
		int x2 = 1;
		for(int j = 0; j < n; ++j)
		{
			if(st[j].first == 'O')
			{
				f = true;
			}
			else
			{
				f = false;
			}
			if(f == true)
			{
				int m = o.top();
				o.pop();
				m = abs(m - x1) + 1;
				x1 = st[j].second;
				ans += m;
				if(!b.empty())
				{
					int h_m = abs(b.top() - x2);
					if(m >= h_m && h_m != 0)
					{
						x2 = b.top();
					}
				
					else
					{
						if(b.top() > x2)
						{
							x2 += m;
						}
						else if(b.top() < x2)
						{
							x2 -= m;
						}
					}
				}
			}
			else
			{
				int m = b.top();
				b.pop();
				m = abs(m - x2) + 1;
				x2 = st[j].second;
				ans += m;
				if(!o.empty())
				{
					int h_m = abs(o.top() - x1);
					if(m >= h_m && h_m != 0)
					{
						x1 = o.top();
					}
					else
					{
						if(o.top() > x1)
						{
							x1 += m;
						}
						else if(o.top() < x1)
						{
							x1 -= m;
						}
					}
				}
			}
		}
		cout << "Case #" << i + 1<<": " << ans << endl;
	}
	return 0;
}