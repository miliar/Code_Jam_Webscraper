#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

struct event
{
	int arrive, time, where;
	event(int arrive, int time, int where) : arrive(arrive), time(time), where(where) {}
};

bool operator< (const event &a, const event &b)
{
	if (a.time != b.time)
		return a.time > b.time;
	return a.arrive < b.arrive;
}

int main()
{
	int kases, kase = 0;
	for (scanf("%d", &kases); kases; kases--)
	{
		int time, na, nb;
		priority_queue<event> pq;
		scanf("%d%d%d", &time, &na, &nb);
		for (int i = 0; i < na; i++)
		{
			int h, m;
			scanf("%d:%d", &h, &m);
			pq.push(event(0, 60*h + m, 0));
			scanf("%d:%d", &h, &m);
			pq.push(event(1, 60*h + m + time, 1));
		}
		for (int i = 0; i < nb; i++)
		{
			int h, m;
			scanf("%d:%d", &h, &m);
			pq.push(event(0, 60*h + m, 1));
			scanf("%d:%d", &h, &m);
			pq.push(event(1, 60*h + m + time, 0));
		}

		int needed[2] = {0}, reserve[2] = {0};
		while (!pq.empty())
		{
			event e = pq.top();
			pq.pop();
			if (e.arrive == 1)
				reserve[e.where]++;
			else
			{
				if (reserve[e.where])
					reserve[e.where]--;
				else
					needed[e.where]++;
			}
		}
		printf("Case #%d: %d %d\n", ++kase, needed[0], needed[1]);
	}
	return 0;
}
