#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const int LEAVE = 1;
const int READY = 2;
const int AB = 0;
const int BA = 1;

typedef struct train_time_t
{
	int hour;
	int minute;
	int action;
	int type;
} TrainTime;

int cmp(const TrainTime &lhs, const TrainTime &rhs)
{
	return (lhs.hour < rhs.hour) || (lhs.hour == rhs.hour && lhs.minute < rhs.minute) || (lhs.hour == rhs.hour && lhs.minute == rhs.minute && lhs.action == READY);
}

int main()
{
    int a, b;
	int caseNum = 0;
	int n;
	while (cin >> n)
	{
		// Read each test case
		for (int i = 0; i < n; ++i)
		{
			int t;
			cin >> t;

			vector<TrainTime> schedule;
			int na, nb;
			cin >> na >> nb;

			// Read data
			int sz = na + nb;
			for (int j = 0; j < sz; ++j)
			{
				TrainTime leave, enter;
				leave.action = LEAVE;
				enter.action = READY;
				scanf("%d:%d %d:%d", &leave.hour, &leave.minute, &enter.hour, &enter.minute);
				enter.minute += t;
				if (enter.minute >= 60)
				{
					++enter.hour;
					enter.minute -= 60;
				}
				leave.type = enter.type = (j < na ? AB : BA);
				schedule.push_back(enter);
				schedule.push_back(leave);
			}
			sort(schedule.begin(), schedule.end(), cmp);

			// Process
			int curA, curB;
			curA = curB = a = b = 0;
			sz *= 2;
			for (int i = 0; i < sz; ++i)
			{
				TrainTime &t = schedule[i];
				int &start = (t.type == AB ? curA : curB);
				int &end = (t.type == AB ? curB : curA);
				if (t.action == READY)
				{
					++end;
				}
				else if (t.action == LEAVE)
				{
					if (start <= 0)
					{
						if (t.type == AB)
						{
							++a;
							++curA;
						}
						else
						{
							++b;
							++curB;
						}
					}
					--start;
				}
			}
			printf("Case #%d: %d %d\n", ++caseNum, a, b);
		}
	}

    return 0;
}
