//#include "stdafx.h"
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	ifstream f("p2.in");

	int nt;
	f >> nt;
	for (int t = 1; t <= nt; t++)
	{
		int tt, na, nb, u, v;
		char tmp;
		vector<int> la, lb, ta, tb;

		f >> tt >> na >> nb;
		for (int i = 0; i < na; i++)
		{
			f >> u >> tmp >> v;
			la.push_back(u * 60 + v);
			f >> u >> tmp >> v;
			tb.push_back(u * 60 + v + tt);
		}

		for (int i = 0; i < nb; i++)
		{
			f >> u >> tmp >> v;
			lb.push_back(u * 60 + v);
			f >> u >> tmp >> v;
			ta.push_back(u * 60 + v + tt);
		}

		sort(la.begin(), la.end());
		sort(lb.begin(), lb.end());
		sort(ta.begin(), ta.end());
		sort(tb.begin(), tb.end());

		int i = 0, j = 0, c1 = 0, c2 = 0;
		while (i < na && j < nb)
		{
			if (la[i] < ta[j])
				c1++;
			else
				j++;
			i++;
		}
		if (i < na)
			c1 += na - i;

		i = j = 0;
		while (i < na && j < nb)
		{
			if (lb[j] < tb[i])
				c2++;
			else
				i++;
			j++;
		}
		if (j < nb)
			c2 += nb - j;

		cout << "Case #" << t << ": " << c1 << ' ' << c2 << endl;
	}
}
