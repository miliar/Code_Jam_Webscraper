#include <cstdio>
#include <algorithm>
#include <utility>

using namespace std;

#define ARRIVAL 0
#define DEPART  1

struct ttime
{
	int time;
	int type;	
};

struct order_by_time
{
	inline bool operator () (const ttime &l, const ttime &r) const
	{ return (l.time < r.time || !(r.time < l.time) && l.type < r.type); }
};

inline int get_min_depart(ttime *t, int num)
{
	int depart = 0, arrival = 0, lastTime = -1;
	for (ttime *pos = t, *end = t+num; pos != end; ++pos)
	{
		switch (pos->type)
		{
		case DEPART:
			if (0 < arrival) { --arrival; }
			else { ++depart; }
			break;
		
		case ARRIVAL:
			++arrival;
			break;
		}
		
		lastTime = pos->time;
	}
	
	return depart;
}

int main(void)
{
	char line[80];	
	fgets(line, 80, stdin);
	
	ttime ttA[200];
	ttime ttB[200];
	int nA, nB, nttA, nttB, turnAround;	
	int hh[2], mm[2];
	
	int cases = atoi(line);
	for (int c = 0; c < cases; ++c)
	{
		fgets(line, 80, stdin);
		turnAround = atoi(line);
		
		fgets(line, 80, stdin);
		sscanf_s(line, "%d %d", &nA, &nB);
		
		nttA = 0;
		nttB = 0;
		
		for (int i = 0; i < nA; ++i)
		{
			fgets(line, 80, stdin);			
			sscanf_s(line, "%d:%d %d:%d", hh, mm, hh + 1, mm + 1);
			
			ttA[nttA].time = hh[0] * 60 + mm[0];
			ttA[nttA].type = DEPART;
			++nttA;
			
			ttB[nttB].time = hh[1] * 60 + mm[1] + turnAround;
			ttB[nttB].type = ARRIVAL;
			++nttB;
		}
		
		for (int i = 0; i < nB; ++i)
		{
			fgets(line, 80, stdin);			
			sscanf_s(line, "%d:%d %d:%d", hh, mm, hh + 1, mm + 1);
			
			ttB[nttB].time = hh[0] * 60 + mm[0];
			ttB[nttB].type = DEPART;
			++nttB;
			
			ttA[nttA].time = hh[1] * 60 + mm[1] + turnAround;
			ttA[nttA].type = ARRIVAL;
			++nttA;
		} 
		
		sort(ttA, ttA + nttA, order_by_time());
		sort(ttB, ttB + nttB, order_by_time());

		printf("Case #%d: %d %d\n", c+1, 
			get_min_depart(ttA, nttA), 
			get_min_depart(ttB, nttB));
	}
	
	return 0;
}