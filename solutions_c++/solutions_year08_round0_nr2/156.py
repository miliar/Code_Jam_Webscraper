#include <iostream>
#include <cstdio>
#include <set>
#include <algorithm>
using namespace std;

struct Train
{
	int	arrival;
	int	departure;
	int	start;

	bool operator < (const Train &t) const
	{
		if(departure != t.departure)
			return departure < t.departure;
		else
			return arrival < t.arrival;
	}
};

Train	trains[1000];
int	total_trains;

int main()
{
	multiset <int>	s[2];
	int		c[2];
	int		T,cs;
	int		tt;
	int		NA,NB,i;
	int		h1,m1,h2,m2;
	int		t1,t2,t;

	scanf("%d",&T);

	for(cs = 1; cs <= T; cs++)
	{
		scanf("%d",&tt);

		scanf("%d %d",&NA,&NB);
		total_trains = 0;

		for(i = 0; i < NA; i++)
		{
			scanf("%d%*c%d %d%*c%d",&h1,&m1,&h2,&m2);
			t1 = h1 * 60 + m1;
			t2 = h2 * 60 + m2;

			if(t2 < t1) swap(t1,t2);

			trains[total_trains].arrival = t2;
			trains[total_trains].departure = t1;
			trains[total_trains].start = 0;
			total_trains++;
		}

		for(i = 0; i < NB; i++)
		{
			scanf("%d%*c%d %d%*c%d",&h1,&m1,&h2,&m2);
			t1 = h1 * 60 + m1;
			t2 = h2 * 60 + m2;

			if(t2 < t1) swap(t1,t2);

			trains[total_trains].arrival = t2;
			trains[total_trains].departure = t1;
			trains[total_trains].start = 1;
			total_trains++;
		}

		sort(trains,trains + total_trains);
		s[0].clear();
		s[1].clear();

		c[0] = c[1] = 0;

		for(i = 0; i < total_trains; i++)
		{
//			printf("i: %d\n",i);
			t = trains[i].departure;
			int	mt;

			if(s[trains[i].start].size() > 0)
				mt = *s[trains[i].start].begin();
			else
				mt = t + 1;

			if(mt <= t)
				s[trains[i].start].erase(s[trains[i].start].begin());
			else
				c[trains[i].start]++;

			s[1 - trains[i].start].insert(trains[i].arrival + tt);
		}

		printf("Case #%d: %d %d\n",cs,c[0],c[1]);
	}

	return 0;
}
