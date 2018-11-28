#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

typedef struct
{
	int depart;
	int arrival;
	int pos;
	bool used;
} Trip;
vector<Trip> trips;

int turnTime, nA, nB;


bool cmp(const Trip &a, const Trip &b)
{
	if (a.arrival != b.arrival)
		return a.arrival < b.arrival;
	else
		return a.depart < b.depart;
}

int main()
{
	int i, j, k, N;
	scanf("%d", &N);
	for (i = 1; i <= N; i++)
	{
		scanf("%d", &turnTime);
		scanf("%d%d", &nA, &nB);
		int h, m;
		Trip tmp;
		trips.clear();
		for (j = 0; j < nA; j++)
		{
			scanf("%d:%d", &h, &m);
			tmp.depart = h * 60 + m;
			scanf("%d:%d", &h, &m);
			tmp.arrival = h * 60 + m;
			tmp.pos = 0;
			tmp.used = false;
			trips.push_back(tmp);
		}
		for (j = 0; j < nB; j++)
		{
			int h, m;
			Trip tmp;
			scanf("%d:%d", &h, &m);
			tmp.depart = h * 60 + m;
			scanf("%d:%d", &h, &m);
			tmp.arrival = h * 60 + m;
			tmp.pos = 1;
			tmp.used = false;
			trips.push_back(tmp);
		}
		int must[2] = {0, 0};
		sort(trips.begin(), trips.end(), cmp);
		for (j = 0; j < trips.size(); j++)
		{
			if (!trips[j].used)
			{
				must[trips[j].pos]++;
				trips[j].used = true;
				int curArrival = trips[j].arrival;
				int curPos = trips[j].pos;
				for (k = j + 1; k < trips.size(); k++)
				{
					if (!trips[k].used && curArrival + turnTime <= trips[k].depart && trips[k].pos != curPos)
					{
						curPos = trips[k].pos;
						trips[k].used = true;
						curArrival = trips[k].arrival;
					}
				}
			}
		}
		printf("Case #%d: %d %d\n", i, must[0], must[1]);
	}
	return 0;
}

