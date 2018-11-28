#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct HHMM
{
	int hour, min;
	int compare(HHMM hhmm)
	{
		if(hour>hhmm.hour || (hour==hhmm.hour && min>hhmm.min)) return 1;
		else if(hour==hhmm.hour && min==hhmm.min) return 0;
		else return -1;
	}

	HHMM operator+(int mm)
	{
		HHMM hhmm;
		hhmm.min=min+mm;
		hhmm.hour=hour+(hhmm.min/60);
		hhmm.min%=60;
		return hhmm;
	}

	bool operator<=(HHMM hhmm)
	{
		if(hour>hhmm.hour || (hour==hhmm.hour && min>hhmm.min)) return false;
		else return true;
	}

};

struct Train
{
	char from;
	HHMM dep, arr;
	bool linked;

	//Train();

};

Train train[220];
int turn_time, NA, NB, ansA, ansB;

void readin(void)
{
	int n1, n2, m1, m2;
	scanf("%d %d\n", &NA, &NB);
	ansA=NA; ansB=NB;
	for(int i=0;i<NA;i++)
	{
		scanf("%d:%d %d:%d\n", &n1, &n2, &m1, &m2);
		train[i].arr.hour=n1; train[i].arr.min=n2;
		train[i].dep.hour=m1; train[i].dep.min=m2;
		train[i].from='A';
		train[i].linked=0;
	}
	for(int i=NA;i<NA+NB;i++)
	{
		scanf("%d:%d %d:%d\n", &n1, &n2, &m1, &m2);
		train[i].arr.hour=n1; train[i].arr.min=n2;
		train[i].dep.hour=m1; train[i].dep.min=m2;
		train[i].from='B';
		train[i].linked=0;
	}
}

int compare(const void * a, const void * b)
{
	Train ta=*(Train*)a;
	Train tb=*(Train*)b;
	return ta.arr.compare(tb.arr);	
}

void proc(void)
{
	for(int i=0;i<NA+NB-1;i++)
		for(int j=i+1;j<NA+NB;j++)
			if(train[i].from!=train[j].from && !train[j].linked && train[i].dep+turn_time<=train[j].arr)
			{
				train[j].linked=1;
				train[j].from=='A'? ansA-- : ansB--;
				break;
			}
}

int main()
{
	freopen("B-large.in","r",stdin);
	//freopen("B-small.in","r",stdin);
	freopen ("B-large.out","w",stdout);
	int cases;
	scanf("%d\n", &cases);

	for(int i=1;i<=cases;i++)
	{
		scanf("%d\n", &turn_time);
		readin();
		qsort(train, NA+NB, sizeof(Train), compare);
		proc();  
		printf("Case #%d: %d %d\n", i, ansA, ansB);
		
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}