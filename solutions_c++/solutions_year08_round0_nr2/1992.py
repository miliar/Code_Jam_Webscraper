#include <iostream>
#include <list>

using namespace std;

const int DEPT = 2;
const int ARR = 1;

struct schedule
{
	int time;
	int type;

public:
	schedule()
	{
	}

	schedule (int t, int ty)
	{
		time = t;
		type = ty;
	}


	bool operator < (schedule& sch)
	{
		if (time == sch.time)
		{
			return type < sch.type;
		}

		return time < sch.time;
	}
};

struct traincnt
{
	int acnt;
	int bcnt;

	traincnt(int a, int b)
	{
		acnt=a;
		bcnt=b;
	}
};


int main()
{
	int nTestCases=0;
	int turnaroundtime=0;
	int nTripsAB=0;
	int nTripsBA=0;
	int hr1, min1, hr2, min2;
	int depttime, arrtime;
	list<schedule> lstNodeASchedule;
	list<schedule> lstNodeBSchedule;
	list<traincnt> lsttraincnt;
	int nodeACnt=0;
	int nodeBCnt=0;
	int tempcnt=0;

	scanf_s ("%d", &nTestCases);

	for (int i=1;i<=nTestCases;++i)
	{
		lstNodeASchedule.clear();
		lstNodeBSchedule.clear();
		nodeACnt = 0;
		nodeBCnt = 0;

		scanf_s ("%d", &turnaroundtime);
		scanf_s ("%d %d", &nTripsAB, &nTripsBA);

		for (int j=1;j<=nTripsAB;++j)
		{
			scanf_s ("%d:%d %d:%d", &hr1, &min1, &hr2, &min2);

			depttime = (hr1 * 60) + min1;

			arrtime = (hr2 * 60) + min2 + turnaroundtime;

			lstNodeASchedule.push_back (schedule(depttime, DEPT));
			lstNodeBSchedule.push_back (schedule(arrtime, ARR));
		}
		for (int j=1;j<=nTripsBA;++j)
		{
			scanf_s ("%d:%d %d:%d", &hr1, &min1, &hr2, &min2);

			depttime = (hr1 * 60) + min1;

			arrtime = (hr2 * 60) + min2 + turnaroundtime;

			lstNodeBSchedule.push_back (schedule(depttime, DEPT));
			lstNodeASchedule.push_back (schedule(arrtime, ARR));
		}

		lstNodeASchedule.sort();
		lstNodeBSchedule.sort();

		tempcnt=0;
		for (list<schedule>::iterator iter = lstNodeASchedule.begin(); iter != lstNodeASchedule.end(); ++iter)
		{
			if (iter ->type == ARR)
			{
				++tempcnt;
			}
			else
			{
				--tempcnt;

				if (tempcnt < 0)
				{
					++nodeACnt;
					tempcnt=0;
				}
			}
		}

		tempcnt=0;

		for (list<schedule>::iterator iter = lstNodeBSchedule.begin(); iter != lstNodeBSchedule.end(); ++iter)
		{
			if (iter ->type == ARR)
			{
				++tempcnt;
			}
			else
			{
				--tempcnt;

				if (tempcnt < 0)
				{
					++nodeBCnt;
					tempcnt=0;
				}
			}
		}

		lsttraincnt.push_back (traincnt(nodeACnt, nodeBCnt));
	}


	tempcnt=1;
	for (list<traincnt>::iterator iter = lsttraincnt.begin(); iter != lsttraincnt.end(); ++iter)
	{
		cout <<"Case #"<<tempcnt<<": "<<iter->acnt<<" "<<iter->bcnt<<"\n";
		++tempcnt;
	}
}