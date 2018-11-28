#include <iostream>
#include <vector>
#include <string>
#include <cstdio>

using namespace std;

int move(int cur, int dest) 
{
	if (dest > cur)
		return cur + 1;
	return cur - 1;
}


int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T;
	cin >> T;
	string str;
	for (int t = 1; t <= T; ++t) 
	{
		int n;
		cin >> n;
		vector<pair<int, int> > o, b;
		for (int i = 0; i < n; ++i) 
		{
			int k;
			cin >> str >> k;
			if (str[0] == 'O') o.push_back(make_pair(k, i));
			else b.push_back(make_pair(k, i));
		}
		
		int o_cell = 1, b_cell = 1;
		int o_order = 0, b_order = 0;
		int timer = 0;

		for (int cur_order = 0; cur_order < n; ++timer)
		{
			bool ob = (o_order < o.size()) && (o_cell == o[o_order].first);
			bool bb = (b_order < b.size()) && (b_cell == b[b_order].first);

			if (ob && !bb)
			{
				if (cur_order == o[o_order].second)
				{
					++o_order;
					++cur_order;
				}
				if (b_order < b.size())
					b_cell = move(b_cell, b[b_order].first);
			}
			else if (!ob && bb)
			{
				if (cur_order == b[b_order].second)
				{
					++b_order;
					++cur_order;
				}
				if (o_order < o.size())
					o_cell = move(o_cell, o[o_order].first);
			}
			else if (ob && bb)
			{
				if (o[o_order].second == cur_order)
				{
					++o_order;
					++cur_order;
				}
				else
				{
					++b_order;
					++cur_order;
				}
			}
			else
			{
				if (o_order < o.size())
					o_cell = move(o_cell, o[o_order].first);
				if (b_order < b.size())
					b_cell = move(b_cell, b[b_order].first);
			}
		}
		cout << "Case #" << t << ": " << timer << endl;
	}
	return 0;
}