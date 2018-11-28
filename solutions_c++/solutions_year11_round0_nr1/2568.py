// BotTrust.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for (int ncase = 1; ncase <= T; ++ncase) {
		int n;
		char c;
		int p;
		cin >> n;
		vector<pair<int, int> > bots[2];
		int priority = 0;
		for (int i = 0; i < n; ++i) {
			cin >> c >> p;
			int bot = 0;
			if (c == 'O')
				bot = 1;
			bots[bot].push_back(make_pair(p, priority++));
		}
		bots[0].push_back(make_pair(1000,100));
		bots[1].push_back(make_pair(1000,100));

		int nsteps = 0;
		int task = 0;
		int bot_tasks[2] = {0, 0};
		int bot_positions[2] = {1, 1};
		while (task < priority) {
			++nsteps;
			bool increase_task = false;
			for (int bot = 0; bot <= 1; ++bot) {
				if (bots[bot][bot_tasks[bot]].first > bot_positions[bot])
					++bot_positions[bot];
				else if (bots[bot][bot_tasks[bot]].first < bot_positions[bot])
					--bot_positions[bot];
				else {
					if (bots[bot][bot_tasks[bot]].second == task) {
						increase_task = true;
						++bot_tasks[bot];
					}
				}
			}
			if (increase_task)
				++task;
		}
		cout << "Case #" << ncase << ": " << nsteps << endl;
	}
	return 0;
}

