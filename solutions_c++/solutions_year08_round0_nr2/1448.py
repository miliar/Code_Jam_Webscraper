#include<stdio.h>
#include<stdlib.h>
#define SIZE	500
#define A	1
#define B	2

struct time
{
	int hrs;
	int min;
};

typedef struct time Time;

struct timetable
{
	Time sttime;
	Time endtime;
	int ststation;
	int endstation;
};

typedef struct timetable TimeTable;

TimeTable content[SIZE];

int mark[SIZE],turntime,na,nb;

int difference(Time t1,Time t2)
{
	int min1,min2;

	min1 = t1.hrs*60+t1.min;
	min2 = t2.hrs*60+t2.min;

	return (min1-min2);
}


int sort_function(const void *a,const void *b)
{
	TimeTable *x = (TimeTable *)a;
	TimeTable *y = (TimeTable *)b;

	if(x->sttime.hrs != y->sttime.hrs)
		return (x->sttime.hrs - y->sttime.hrs);
	else
		return (x->sttime.min - y->sttime.min);
	

}

void init(int nA,int nB)
{
	int i;
	for(i=0;i<nA+nB;i++)
	{
		mark[i] = 0;
	}
}



bool decision(int i,int index)
{
	Time t1 = content[i].sttime;
	Time t2 = content[index].endtime;

	if(difference(t1,t2) >= turntime)
		return true;
	return false;
}

void markthesets(int index,int nA,int nB)
{
	
	int i;
	mark[index] = 1;
	
	//printf("%2d:%2d   %2d:%2d   %d\n",content[index].sttime.hrs,content[index].sttime.min,content[index].endtime.hrs,content[index].endtime.min,content[index].ststation);
	
	for(i=index+1;i<nA+nB;i++)
	{
		if(mark[i] == 0 && content[i].ststation == content[index].endstation)
		{
			if(decision(i,index))
			{
				index = i;
				mark[i] = 1;
				//printf("%2d:%2d   %2d:%2d   %d\n",content[i].sttime.hrs,content[i].sttime.min,content[i].endtime.hrs,content[i].endtime.min,content[i].ststation);
			}
		}
	}
	//printf("\n");
}

void dfs(int nA,int nB)
{
	int i;
	init(nA,nB);
	na = nb =0;
	for(i=0;i<nA+nB;i++)
	{
		if(mark[i] == 0)
		{
			markthesets(i,nA,nB);
			if(content[i].ststation == A)	na++;
			else							nb++;
		}
	}

}

int main(void)
{
	int t,nA,nB,i,j;

	freopen("B-large.in","r",stdin);
	freopen("out2.txt","w",stdout);

	scanf("%d",&t);

	for(i=1;i<=t;i++)
	{
		scanf("%d",&turntime);
		scanf("%d %d",&nA,&nB);

		for(j=0;j<nA;j++)
		{
			scanf("%d%*c%d %d%*c%d",&content[j].sttime.hrs,&content[j].sttime.min,&content[j].endtime.hrs,&content[j].endtime.min);
			content[j].ststation = A;
			content[j].endstation = B;
		}

		for(j=nA;j<nA+nB;j++)
		{
			scanf("%d%*c%d %d%*c%d",&content[j].sttime.hrs,&content[j].sttime.min,&content[j].endtime.hrs,&content[j].endtime.min);
			content[j].ststation = B;
			content[j].endstation = A;
		}

		qsort(content,nA+nB,sizeof(content[0]),sort_function);

		/*for(j=0;j<nA+nB;j++)
		{
			printf("%2d:%2d   %2d:%2d   %d\n",content[j].sttime.hrs,content[j].sttime.min,content[j].endtime.hrs,content[j].endtime.min,content[j].ststation);
		}*/
		dfs(nA,nB);
		printf("Case #%d: %d %d\n",i,na,nb);
	}
	return 0;
}