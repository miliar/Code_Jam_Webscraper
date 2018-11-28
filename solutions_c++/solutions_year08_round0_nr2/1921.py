#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

struct event
{
	int time;
	bool dep;
	bool A;
	bool processed;

	event(string time_s, bool dep, bool A, int T = 0):dep(dep), A(A)
	{
		time_s[2] = ' ';
		stringstream ss;
		ss <<time_s;
		int h, m;
		ss >>h >>m;

		time = 60*h + m + T;
		processed = false;
	}
};

bool cmp(const event &a, const event &b)
{
	return a.time < b.time;
}

void main()
{
	ifstream in("B-small-attempt1.in");
	ofstream out("small.out");

	int tc;
	in >>tc;
	for (int cc = 0;cc < tc;cc++)
	{
		int T, AB, BA;
		in >>T >>AB >>BA;

		vector <event> events;

		for (int i = 0;i < AB;i++)
		{
			string d, a;
			in >>d >>a;

			events.push_back(event(d, true, true));
			events.push_back(event(a, false, false, T));
		}

		for (int i = 0;i < BA;i++)
		{
			string d, a;
			in >>d >>a;

			events.push_back(event(d, true, false));
			events.push_back(event(a, false, true, T));
		}

		sort(events.begin(), events.end(), cmp);
		int ra, rb;
		ra = rb = 0;

		int at_a, at_b;
		at_a = at_b = 0;

		for (int i = 0;i < events.size();i++)
		{
			event &e = events[i];

			if (e.processed)
				continue;

			// handle all arrivals on this station at this time
			for (int j = i;j < events.size() && events[j].time == e.time;j++)
				if (!events[j].dep && events[j].A == e.A)	// arrival at this station
				{
					events[j].processed = true;
					if (e.A)
						at_a++;
					else
						at_b++;
				}

			if (e.dep)
			{
				if (e.A)
				{
					if (at_a == 0)
						ra++;
					else
						at_a--;
				}
				else
				{
					if (at_b == 0)
						rb++;
					else
						at_b--;
				}
			}
		}

		out <<"Case #"<<cc + 1 <<": " <<ra <<" " <<rb <<endl;
	}
}
