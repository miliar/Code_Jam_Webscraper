/*
 * a.cpp
 *
 *  Created on: 2011-5-7
 *      Author: acer
 */

#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	int tn;
	cin >> tn;
	for (int ti = 1; ti <= tn; ++ti)
	{
		int pre[2];
		int idle[2];
		int n;
		cin >> n;

		int cost(0);
		pre[0] = pre[1] = 1;
		idle[0] = idle[1] = 0;

		for (int i = 0; i < n; ++i)
		{
			string op;
			int id, pos;
			cin >> op >> pos;
			if (op[0] == 'O')
			{
				id = 0;
			}
			else
			{
				id = 1;
			}
			int currentcost = abs(pre[id] - pos) - idle[id] + 1;
			if (currentcost < 1)
			{
				currentcost = 1;
			}
			cost += currentcost;
			idle[id] = 0;
			pre[id] = pos;
			idle[id ^ 1] += currentcost;
		}

		cout << "Case #" << ti << ": " << cost << endl;
	}


	return 0;
}
