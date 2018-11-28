#include <iostream>
#include <list>
using namespace std;

typedef struct
{
	int start;
	int end;
	int direction; //1: A->B   -1: B->A
	bool arranged;
}Schedule;

Schedule sd[200];
int n;  //test cases
int t; //turn around time
int na, nb;
list<int> stationA, stationB;

int na_count, nb_count;

int readTime()
{
	int hour, min;
	cin >> hour;
	getchar();
	cin >> min;
	return hour*100 + min;
}

int compare(const void *arg1, const void *arg2 )
{
	Schedule *e1 = (Schedule*)arg1;
	Schedule *e2 = (Schedule*)arg2;
	if(e1->start != e2->start)
		return e1->start - e2->start;
	else
		return e1->end - e2->end;
}

bool tryUseTrainInStation(Schedule & arg)
{
	list<int>::iterator iter;
	if(arg.direction == 1) //A->
	{
		iter = stationA.begin();
		while(iter != stationA.end())
		{
			if(*iter <= arg.start)
			{
				stationA.erase(iter);
				return true;
			}
			iter ++ ;
		}
	}
	else
	{
		iter = stationB.begin();
		while(iter != stationB.end())
		{
			if(*iter <= arg.start)
			{
				stationB.erase(iter);
				return true;
			}
			iter ++ ;
		}
	}
	return false;
}

void scheduleToOtherSide(Schedule & arg)
{
	if(arg.direction == 1)
		stationB.push_back(arg.end + t);
	else
		stationA.push_back(arg.end + t);
}

int main()
{
	int i, k;
	
	cin >> n;
	for(k=1; k<=n; k++)
	{
		cin >> t;
		cin >> na >> nb;
		memset(sd, 0, sizeof(sd));
		for(i=0; i<na+nb; i++)
		{
			sd[i].start = readTime();
			sd[i].end = readTime();
			if(i<na)
				sd[i].direction = 1; // A->B
			else
				sd[i].direction = -1; // B->A

			sd[i].arranged = false;
		}
		qsort(sd, na+nb, sizeof(Schedule), compare);
		
		stationA.clear();
		stationB.clear();
		na_count = nb_count = 0;
		for(i=0; i<na+nb; i++)
		{
			if(sd[i].arranged)
				continue;
			if( !tryUseTrainInStation(sd[i]) ) //don't have train to use
			{
				if(sd[i].direction == 1)
					na_count++;
				else
					nb_count++;				
			}
			scheduleToOtherSide(sd[i]);
			sd[i].arranged = true;
		}
		cout << "Case #" << k << ": "<< na_count << " " << nb_count << endl;
	}
}