#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>

using namespace std;

#define Arrive 0
#define Depart 1
	
struct schedule
{
	int time;
	int mode; // 0: Arrive 1: Depart
	int city; // 0: A, 1: B
};

int CompareTimetable(const void *v1, const void *v2)
{
	schedule t1 = *(schedule*)v1;
	schedule t2 = *(schedule*)v2;

	if(t1.time < t2.time)
	{
		return -1;
	}
	else if(t2.time < t1.time)
	{
		return 1;
	}
	else
	{
		if(t1.mode != t2.mode)
		{
			return t1.mode - t2.mode;
		}
		else
		{
			return t1.city - t2.city;
		}
	}
	return 0;
}

#define MAX_SCHEDULE 200
void main()
{
	char buff[256];

	int n; // case
	gets(buff);
	sscanf(buff, "%d", &n);

	for(int i = 1; i <= n; i++) // case i
	{
		int turnaround;
		gets(buff);
		sscanf(buff, "%d", &turnaround);

		schedule timetable[MAX_SCHEDULE];
		int countS = 0; // the number of schedules

		int na, nb;
		gets(buff);
		sscanf(buff, "%d %d", &na, &nb);

		for(int j = 0; j < na; j++) // from A
		{
			gets(buff);
			char dtime[10], atime[10];
			sscanf(buff, "%s %s", dtime, atime);

			int iDTime = ((dtime[0] - '0') * 10 + (dtime[1] - '0')) * 60 + ((dtime[3] - '0') * 10 + (dtime[4] - '0'));
			int iATime = ((atime[0] - '0') * 10 + (atime[1] - '0')) * 60 + ((atime[3] - '0') * 10 + (atime[4] - '0'));
			timetable[countS].time = iDTime;
			timetable[countS].mode = Depart;
			timetable[countS].city = 0;
			countS++;
			timetable[countS].time = iATime + turnaround;
			timetable[countS].mode = Arrive;
			timetable[countS].city = 1;
			countS++;
		}

		for(int j = 0; j < nb; j++) // from B
		{
			gets(buff);
			char dtime[10], atime[10];
			sscanf(buff, "%s %s", dtime, atime);

			int iDTime = ((dtime[0] - '0') * 10 + (dtime[1] - '0')) * 60 + ((dtime[3] - '0') * 10 + (dtime[4] - '0'));
			int iATime = ((atime[0] - '0') * 10 + (atime[1] - '0')) * 60 + ((atime[3] - '0') * 10 + (atime[4] - '0'));
			timetable[countS].time = iDTime;
			timetable[countS].mode = Depart;
			timetable[countS].city = 1;
			countS++;
			timetable[countS].time = iATime + turnaround;
			timetable[countS].mode = Arrive;
			timetable[countS].city = 0;
			countS++;
		}

		qsort(timetable, countS, sizeof(schedule), CompareTimetable);

//		if(i == 2)
//			for(int k = 0; k < countS; k++)
//				cout << timetable[k].time << " " << timetable[k].mode << " " << timetable[k].city << endl;

		int iReq[2]; // # of requested trains of A & B
		iReq[0] = 0, iReq[1] = 0;
		int iFree[2]; // # of free trains of A & B
		iFree[0] = 0, iFree[1] = 0;

		for(int k = 0; k < countS; k++)
		{
			if(timetable[k].mode == Arrive)
			{
				iFree[timetable[k].city]++;
			}
			else // Depart
			{
				if(iFree[timetable[k].city] > 0)
				{
					iFree[timetable[k].city]--;
				}
				else
				{
					iReq[timetable[k].city]++;
				}
			}
			
//			if(i == 2)
//				cout << timetable[k].time << " " << iReq[0] << " " << iReq[1] << " " << iFree[0] << " " << iFree[1] << endl;
		}
		cout << "Case #" << i << ": " << iReq[0] << " " << iReq[1] << endl;
	}
	cout << endl;

}
