#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
using namespace std;

int N, n;
vector <int> a, o, b;
int uk1, uk2, now_o, now_b, k;

void make_move()
{
	bool q = false;

	if (uk1 < o.size())
	{
		if (o[uk1] > now_o)
			now_o++;
		else if (o[uk1] < now_o)
			now_o--;
		else if (o[uk1] == now_o && a[k] > 0)
		{
			q = true;
			uk1++;
		}
	}
	
	if (uk2 < b.size())
	{
		if (b[uk2] > now_b)
			now_b++;
		else if (b[uk2] < now_b)
			now_b--;
		else if (b[uk2] == now_b && a[k] < 0)
		{
			q = true;
			uk2++;
		}
	}

	if (q)
		k++;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> N;

	for (int t = 1; t <= N; t++)
	{
		cin >> n;
		a.clear();
		o.clear();
		b.clear();

		now_o = 1;
		now_b = 1;
		uk1 = 0;
		uk2 = 0;
		k = 0;

		for (int i = 0; i < n; i++)
		{
			char c;
			int x;
			cin >> c >> x;
			
			if (c == 'O')
			{
				a.push_back(x);
				o.push_back(x);
			}
			if (c == 'B')
			{
				a.push_back(-x);
				b.push_back(x);
			}
		}

		int res = 0;

		while (uk1 < o.size() || uk2 < b.size())
		{
			make_move();
			res++;
		}
		cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}