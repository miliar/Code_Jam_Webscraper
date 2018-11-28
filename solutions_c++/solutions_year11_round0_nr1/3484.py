# include <iostream>
# include <cmath>
# include <algorithm>
# include <list>
# include <string>
# include <vector>
# include <map>
using namespace std;



int main()
{
#ifndef ONLINE_JUDGE
	freopen("test.in", "rt", stdin);
	freopen("test.out", "wt", stdout);
#endif
	int t;
	scanf("%d ", &t);
	for (int i = 0; i < t; i++)
	{
		bool work[105] = {false};
		work[0] = true;
		vector < pair <int, int> > O;
		vector < pair <int, int> > B;
		int n;
		scanf("%d ", &n);
		char k;
		int buf;
		for (int j = 0; j < n; j++)
		{
			scanf("%c %d ", &k, &buf);
			if (k == 'O')
				O.push_back(make_pair(buf, j + 1));
			else
				B.push_back(make_pair(buf, j + 1));
		}
		int res = 0;
		int dels = 0;
		int a = 1,b = 1;
		int ai = 0, bi = 0;
		bool f = false;
		while (dels < n)
		{
			f = false;
			int dd;
			if (!O.empty() && ai < O.size())
			{
				if (a < O[ai].first)
					a++;
				else if (a > O[ai].first)
					a--;
				else if (a == O[ai].first)
				{
					if (work[O[ai].second - 1])
					{
						dd = O[ai].second;
						ai++;
						f = true;
					}
				}
			}
			if (!B.empty() && bi < B.size())
			{
				if (b < B[bi].first)
					b++;
				else if (b > B[bi].first)
					b--;
				else if (b == B[bi].first)
				{
					if (work[B[bi].second - 1])
					{
						dd = B[bi].second;
						bi++;
						f = true;
					}
				}
			}
			if (f)
			{
				dels++;
				work[dd] = true;
			}
			res++;
		}
		printf("Case #%d: %d\n", i + 1, res);
	}
	return 0;
}