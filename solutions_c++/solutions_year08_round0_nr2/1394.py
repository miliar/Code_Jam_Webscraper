#include <vector>
#include <algorithm>
#include <functional>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <queue>

using namespace std;

class pir {
  public:
	int	first, second;
	pir(int i, int j)
	{
		first = i; second = j;
	}
	friend bool operator <(const pir &x, const pir &y)
	{
		if (x.first < y.first)
			return false;
		else if (x.first == y.first && x.second < y.second)
			return false;
		else
			return true;
	}
};

int	res[2];

void 	calc(priority_queue<pir> &atob, priority_queue<pir> &btoa, int t)
{
	priority_queue<int, vector<int>, greater<int> >	aa;
	priority_queue<int, vector<int>, greater<int> >	ab;

	res[0] = res[1] = 0;
	aa.push(INT_MAX); ab.push(INT_MAX);

	while (!atob.empty() && !btoa.empty())
	{
		if (atob.top().first < btoa.top().first)
		{
			if (aa.top() <= atob.top().first)
			{
				aa.pop();
			}
			else
			{
				res[0]++;
			}
			ab.push(atob.top().second + t);
			atob.pop();
		}
		else
		{
			if (ab.top() <= btoa.top().first)
			{
				ab.pop();
			}
			else
			{
				res[1]++;
			}
			aa.push(btoa.top().second + t);
			btoa.pop();
		}
	}

	if (!atob.empty())
	{
		while (!atob.empty())
		{
			if (aa.top() <= atob.top().first)
			{
				aa.pop();
			}
			else
			{
				res[0]++;
			}
			atob.pop();
		}
	}
	else if (!btoa.empty())
	{
		while (!btoa.empty())
		{
			if (ab.top() <= btoa.top().first)
			{
				ab.pop();
			}
			else
			{
				res[1]++;
			}
			btoa.pop();
		}
	}
}

int main()
{
	int	n, nt, a, b, i, j;
	int	h1, m1, h2, m2, t1, t2;

	cin >> n; cin.ignore(256, '\n');

	for (i=0;i<n;i++)
	{
		priority_queue<pir>	atob;
		priority_queue<pir>	btoa;

		cin >> nt; cin.ignore(256, '\n');
		cin >> a >> b; cin.ignore(256, '\n');
		for (j=0;j<a;j++)
		{
			scanf("%d:%d", &h1, &m1);
			t1 = (h1 * 60 + m1);
			scanf("%d:%d", &h2, &m2);
			t2 = (h2 * 60 + m2);
			atob.push(pir(t1, t2));
		}
		for (j=0;j<b;j++)
		{
			scanf("%d:%d", &h1, &m1);
			t1 = (h1 * 60 + m1);
			scanf("%d:%d", &h2, &m2);
			t2 = (h2 * 60 + m2);
			btoa.push(pir(t1, t2));
		}
		calc(atob, btoa, nt);
		cout << "Case #" << (i+1) << ": " << res[0] << " " << res[1] << endl;
	}

	return 0;
}
