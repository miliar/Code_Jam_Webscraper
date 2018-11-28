#include "stdafx.h"

#include <deque>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int t, tt;
	ifstream f("p6.in");

	f >> t;
	for (int tt = 0; tt < t; tt++)
	{
		int k, n, cnt;
		deque<int> d;
		vector<int> p, q;

		f >> k >> n;
		while (n)
		{
			f >> cnt;
			q.push_back(cnt);
			n--;
		}

		p.resize(k, 0);
		for (int i = 0; i < k; i++)
			d.push_back(i + 1);

		cnt = 0;
		for (int i = 0; i < k; i++)
		{
			for (int j = 0; j < cnt; j++)
			{
				int x = d.front();
				d.pop_front();
				d.push_back(x);
			}

			p[d.front() - 1] = cnt + 1;
			d.pop_front();
			cnt++;
		}

		cout << "Case #" << tt + 1 << ": ";
		for (int i = 0; i < q.size(); i++)
			cout << p[q[i] - 1] << ' ';
		cout << endl;
	}
}
