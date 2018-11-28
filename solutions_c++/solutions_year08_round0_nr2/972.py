#include <stdio.h>
#include <stdlib.h>

typedef struct TrainTime
{
	int leaveHour;
	int leaveMin;
	int arriveHour;
	int arriveMin;
}TrainTime;

TrainTime tALeave[110];
TrainTime tBLeave[110];
TrainTime tAArrive[110];
TrainTime tBArrive[110];

int n, na, nb;
int i, j;
int timesA, timesB;
int count;
int t;
FILE *out;

int CmpByLeave(const void * a, const void * b)
{
	TrainTime *c = (TrainTime *)a;
	TrainTime *d = (TrainTime *)b;
	
	if(c->leaveHour != d->leaveHour)
		return c->leaveHour - d->leaveHour;
	else
		return c->leaveMin - d->leaveMin;
}

int CmpByArrive(const void * a, const void *b)
{
	TrainTime *c = (TrainTime *)a;
	TrainTime *d = (TrainTime *)b;
	
	if(c->arriveHour != d->arriveHour)
		return c->arriveHour - d->arriveHour;
	else
		return c->arriveMin - d->arriveMin;
}

void AddTime(TrainTime *time)
{
	time->arriveMin += t;
	
	if(time->arriveMin >= 60)
	{
		time->arriveMin -= 60;
		time->arriveHour += 1;
	}
}

int CmpTime(int hourA, int minA, int hourB, int minB)
{
	if(hourA > hourB)
		return 1;
	else if(hourA < hourB)
		return -1;
	else 
	{
		if(minA > minB)
			return 1;
		else if(minA < minB)
			return -1;
		else
			return 0;
	}
}

void Solve()
{
	qsort(tALeave, na, sizeof(tALeave[0]), CmpByLeave);
	qsort(tBLeave, nb, sizeof(tBLeave[0]), CmpByLeave);
	qsort(tAArrive, na, sizeof(tAArrive[0]), CmpByArrive);
	qsort(tBArrive, nb, sizeof(tBArrive[0]), CmpByArrive);
	
	int a = 0, b = 0;
	int numA = na;
	int numB = nb;
	
	for(a = 0; a < na; a++)
	{
		AddTime(&tAArrive[a]);
		
		while(1)
		{
			if(b >= nb)
				break;
			if(CmpTime(tAArrive[a].arriveHour, tAArrive[a].arriveMin, tBLeave[b].leaveHour, tBLeave[b].leaveMin) <= 0)
			{
				numB--;
				b++;
				break;
			}
			else
			{
				b++;
			}
		}
	}
	
	a = 0;
	for(b = 0; b < nb; b++)
	{
		AddTime(&tBArrive[b]);
		
		while(1)
		{
			if(a >= na)
				break;
			
			if(CmpTime(tBArrive[b].arriveHour, tBArrive[b].arriveMin, tALeave[a].leaveHour, tALeave[a].leaveMin) <= 0)
			{
				numA--;
				a++;
				break;
			}
			else
			{
				a++;
			}
		}
	}
	
	fprintf(out, "Case #%d: %d %d\n", count, numA, numB);
}

int main()
{
	scanf("%d", &n);
	
	out = fopen("F:\\ACM\\GoogleCodeJam\\TimeTable.txt", "wt");
	
	for(count = 1; count <= n; count++)
	{
		scanf("%d", &t);
		scanf("%d%d", &na, &nb);
		
		for(i = 0; i < na; i++)
		{
			scanf("%d:%d%d:%d", &tALeave[i].leaveHour, &tALeave[i].leaveMin, &tALeave[i].arriveHour, &tALeave[i].arriveMin);
			tAArrive[i].leaveHour = tALeave[i].leaveHour;
			tAArrive[i].leaveMin = tALeave[i].leaveMin;
			tAArrive[i].arriveHour = tALeave[i].arriveHour;
			tAArrive[i].arriveMin = tALeave[i].arriveMin;
		}
		
		for(i = 0; i < nb; i++)
		{
			scanf("%d:%d%d:%d", &tBLeave[i].leaveHour, &tBLeave[i].leaveMin, &tBLeave[i].arriveHour, &tBLeave[i].arriveMin);
			tBArrive[i].leaveHour = tBLeave[i].leaveHour;
			tBArrive[i].leaveMin = tBLeave[i].leaveMin;
			tBArrive[i].arriveHour = tBLeave[i].arriveHour;
			tBArrive[i].arriveMin = tBLeave[i].arriveMin;
		}
		
		Solve();
	}
	
	return 0;
}