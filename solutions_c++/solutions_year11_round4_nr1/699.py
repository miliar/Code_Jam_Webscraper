#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

typedef struct
{
	int B, E;
	int speed;
} WW;

bool operator < (const WW &a, const WW &b)
{
	return a.speed < b.speed;
}

void solve_case ()
{
	int X, S, R, t, N;
	WW data[1100];

	cin >> X >> S >> R >> t >> N;
	for (int i=0 ;i<N ;i++)
	{
		cin >> data[i].B >> data[i].E >> data[i].speed;
	}

	double total = 0;
	sort (data, data+N);
	double left = t;

	for (int i=0 ;i<N ;i++)
	{
		X -= data[i].E - data[i].B;
	}

	int L = X;
	double walk_time = (double)L / (S);
	double run_time = (double)L / (R);

	if (left > 0)
	{
		if (left > run_time)
		{
			left -= run_time;
			total += run_time;
		}
		else
		{
			double run_dist = left * (R);
			total += left;
			walk_time = ((double)L - run_dist) / (S);
			total += walk_time;
			left = 0;
		}
	}
	else
		total += walk_time;

	for (int i=0 ;i<N ;i++)
	{
		int L = data[i].E - data[i].B;
		
		double walk_time = (double)L / (data[i].speed + S);
		double run_time = (double)L / (data[i].speed + R);

		if (left > 0)
		{
			if (left > run_time)
			{
				left -= run_time;
				total += run_time;
			}
			else
			{
				double run_dist = left * (data[i].speed + R);
				total += left;
				walk_time = ((double)L - run_dist) / (data[i].speed + S);
				total += walk_time;
				left = 0;
			}
		}
		else
			total += walk_time;

		X -= L;
	}


	printf ("%.7lf\n", total);
}

int main ()
{
	int total_cases;

	cin >> total_cases;
	for (int cases=1 ;cases<=total_cases ;cases++)
	{
		cout << "Case #" << cases << ": ";
		solve_case ();
	}

	return 0;
}
