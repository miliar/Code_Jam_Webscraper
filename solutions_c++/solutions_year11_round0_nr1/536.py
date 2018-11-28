#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int>	PII;
typedef vector<PII>		VPII;

int get_next(int t, int p, const VPII &task)
{
	while (p < task.size())
	{
		if (task[p].first == t)
			return task[p].second;
		p++;
	}
	return 0;
}

int main()
{
	int kases;
	string line;
	getline(cin, line);
	stringstream buf(line);
	buf >> kases;
	for (int kase = 1; kase <= kases; kase++)
	{
		getline(cin, line);
		stringstream buf(line);
		int pos;
		buf >> pos;
		string rob;
		VPII task;
		while (buf >> rob >> pos)
		{
			if (rob == "O")
				task.push_back(PII(0,pos));
			else
				task.push_back(PII(1,pos));
		}

		int time = 0;
		int pos0 = 1;
		int pos1 = 1;
		for (int i = 0; i < task.size(); i++)
		{
			int np0 = get_next(0, i, task);
			int np1 = get_next(1, i, task);

			if (task[i].first == 0)
			{
				int step = abs(pos0 - np0) + 1;
				time += step;
				pos0 = np0;
				if (abs(pos1 - np1) <= step)
					pos1 = np1;
				else if (np1 > pos1)
					pos1 += step;
				else
					pos1 -= step;
			}
			else
			{
				int step = abs(pos1 - np1) + 1;
				pos1 = np1;
				time += step;
				if (abs(pos0 - np0) <= step)
					pos0 = np0;
				else if (np0 > pos0)
					pos0 += step;
				else
					pos0 -= step;
			}
		}
		cout << "Case #" << kase << ": " << time << endl;
	}
	return 0;
}
