#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

struct Data
{
	int priority, button;
};

int main()
{
	int ncase, t, n, i;
	char ch;

	cin >> t;
	for (ncase = 1; ncase <= t; ncase++)
	{
		vector<Data> or, bl;

		cin >> n;
		for (i = 0; i < n; i++)
		{
			Data d;
			d.priority = i;

			cin >> ch >> d.button;
			if (ch == 'O')
				or.push_back(d);
			else
				bl.push_back(d);
		}

		vector<Data>::iterator or_iter = or.begin();
		vector<Data>::iterator bl_iter = bl.begin();
		int tm = 0;
		int or_pos = 1;
		int bl_pos = 1;

		while(or_iter != or.end() || bl_iter != bl.end())
		{
			if (or_iter != or.end() && bl_iter != bl.end())
			{
				if (or_iter->priority < bl_iter->priority)
				{
					int diff = abs(or_pos - or_iter->button) + 1;
					tm += diff;
					or_pos = or_iter->button;

					if (bl_pos <= bl_iter->button)
					{
						if (bl_pos + diff < bl_iter->button)
						{
							bl_pos += diff;
						}
						else // if (bl_pos + diff >= bl_iter->button)
						{
							bl_pos = bl_iter->button;
						}
					}
					else // bl_pos > bl_iter->button
					{
						if (bl_pos - diff > bl_iter->button)
						{
							bl_pos -= diff;
						}
						else
						{
							bl_pos = bl_iter->button;
						}
					}

					or_iter++;
				}
				else // bl_iter->priority < or_iter->priority
				{
					int diff = abs(bl_pos - bl_iter->button) + 1;
					tm += diff;
					bl_pos = bl_iter->button;

					if (or_pos <= or_iter->button)
					{
						if (or_pos + diff < or_iter->button)
						{
							or_pos += diff;
						}
						else // if (or_pos + diff >= or_iter->button)
						{
							or_pos = or_iter->button;
						}
					}
					else // or_pos > or_iter->button
					{
						if (or_pos - diff > or_iter->button)
						{
							or_pos -= diff;
						}
						else
						{
							or_pos = or_iter->button;
						}
					}

					bl_iter++;
				}
			}
			else if (or_iter != or.end())
			{
				int diff = abs(or_pos - or_iter->button) + 1;
				tm += diff;
				or_pos = or_iter->button;

				or_iter++;
			}
			else // bl_iter != bl.end()
			{
				int diff = abs(bl_pos - bl_iter->button) + 1;
				tm += diff;
				bl_pos = bl_iter->button;

				bl_iter++;
			}
		}

		cout << "Case #" << ncase << ": " << tm;
		cout << endl;
	}

	return 0;
}
