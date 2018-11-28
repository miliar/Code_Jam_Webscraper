#include <stdio.h>
#include <conio.h>
#include <vector>
#include <algorithm>

using namespace std;

struct TimeTrainDelta
{
	int time;
	int trainDelta;

	bool operator< (const TimeTrainDelta &rhs)
	{
		return time < rhs.time;
	}

};

int str_to_minutes(char *buffer)
{
	int hours = (buffer[0] - '0') * 10 + (buffer[1] - '0');
	int mins = (buffer[3] - '0') * 10 + (buffer[4] - '0');
	return hours * 60 + mins;
}

int min_trains(vector<TimeTrainDelta> &ttdArray)
{
	int mint = 0;
	int currNumTrains = 0;
	int currTime;
	vector<TimeTrainDelta>::iterator iter = ttdArray.begin();
	for ( ; iter < ttdArray.end(); iter++ )
	{
		currTime = iter->time;
		do
		{
			currNumTrains += iter->trainDelta;
			iter++;
		} while (iter < ttdArray.end() && iter->time == currTime);
		iter--;

		if (currNumTrains < mint) mint = currNumTrains;
	}
	return mint;
}

/*void insert_sorted(list<TimeTrainDelta> &schedule, TimeTrainDelta ttd)
{
	list<TimeTrainDelta>::iterator iter = schedule.begin();
}*/

int main()
{
	const int BUFF_SIZE = 100;
	char buffer[BUFF_SIZE];
	int numCases;

	FILE *fin = fopen("B-large.in", "rt");
	FILE *fout = fopen("B-large.out", "wt");

	fscanf(fin, "%d", &numCases);

	for (int i = 0; i < numCases; i++)
	{
		int turnAround;
		int na, nb;
		vector<TimeTrainDelta> scheduleA;
		vector<TimeTrainDelta> scheduleB;

		fscanf(fin, "%d", &turnAround);
		fscanf(fin, "%d %d", &na, &nb);

		// Read the trip timings for station A
		for (int j = 0; j < na; j++)
		{
			TimeTrainDelta deptA, arrvB;

			fscanf(fin, "%s", buffer);
			deptA.time       = str_to_minutes(buffer);
			deptA.trainDelta = -1;
			//insert_sorted(scheduleA, deptA);
			scheduleA.push_back(deptA);

			fscanf(fin, "%s", buffer);
			arrvB.time       = str_to_minutes(buffer) + turnAround;
			arrvB.trainDelta = 1;
			//insert_sorted(scheduleB, arrvB);
			scheduleB.push_back(arrvB);
		}

		// Read the trip timings for station B
		for (int j = 0; j < nb; j++)
		{
			TimeTrainDelta deptB, arrvA;

			fscanf(fin, "%s", buffer);
			deptB.time       = str_to_minutes(buffer);
			deptB.trainDelta = -1;
			//insert_sorted(scheduleB, deptB);
			scheduleB.push_back(deptB);

			fscanf(fin, "%s", buffer);
			arrvA.time       = str_to_minutes(buffer) + turnAround;
			arrvA.trainDelta = 1;
			//insert_sorted(scheduleA, arrvA);
			scheduleA.push_back(arrvA);
		}

		sort(scheduleA.begin(), scheduleA.end());
		sort(scheduleB.begin(), scheduleB.end());

		// Calculate minimum trains at each station
		int minA, minB;
		minA = min_trains(scheduleA);
		minB = min_trains(scheduleB);

		fprintf(fout, "Case #%d: %d %d\n", i + 1, -minA, -minB);
	}

	fclose(fin);
	fclose(fout);
}