// Train Timetable.cpp : Defines the entry point for the console application.
//

#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

bool Sort(pair < int, int > a, pair < int, int > b)
{
	if (a.first < b.first)
		return true;

	if (a.first == b.first)
	{
		if (a.second < b.second)
			return true;
	}

	return false;
}

int main(void)
{
	char                         time[8];
	ifstream                     input;
	int                          caseCount       = 0;
	int                          i               = 0;
	int                          k               = 0;
	int                          t               = 0;
	int                          table[2][1501]  = {0};
	int                          trainsAtA       = 0;
	int                          trainsNeededAtA = 0;
	int                          trainsNeededAtB = 0;
	int                          trainsAtB       = 0;
	int                          tripsA          = 0;
	int                          tripsB          = 0;
	int                          turnaroundTime  = 0;
	ofstream                     output;
	pair < int, int >            timePair;
	vector < pair < int, int > > aToB;
	vector < pair < int, int > > bToA;

	input.open("TrainTimetable.in", ios_base::in);
	output.open("TrainTimetable.out", ios_base::out);

	input >> caseCount;
	for (i = 0; i < caseCount; i++)
	{
		//
		//  Initialize
		//
		memset(table, 0, sizeof (table));
		trainsAtA = 0;
		trainsAtB = 0;
		aToB.erase(aToB.begin(), aToB.end());
		bToA.erase(bToA.begin(), bToA.end());

		input >> turnaroundTime;
		input >> tripsA >> tripsB;

		for (k = 0; k < tripsA; k++)
		{
			input >> time;
			timePair.first  = (time[0] - '0') * 10;
			timePair.first += time[1] - '0';
			timePair.first *= 60;
			timePair.first += (time[3] - '0') * 10;
			timePair.first += time[4] - '0';

			input >> time;
			timePair.second  = (time[0] - '0') * 10;
			timePair.second += time[1] - '0';
			timePair.second *= 60;
			timePair.second += (time[3] - '0') * 10;
			timePair.second += time[4] - '0';
			timePair.second += turnaroundTime;
			table[0][timePair.second]++;

			aToB.push_back(timePair);
		}
		sort(aToB.begin(), aToB.end(), Sort);

		for (k = 0; k < tripsB; k++)
		{
			input >> time;
			timePair.first  = (time[0] - '0') * 10;
			timePair.first += time[1] - '0';
			timePair.first *= 60;
			timePair.first += (time[3] - '0') * 10;
			timePair.first += time[4] - '0';

			input >> time;
			timePair.second  = (time[0] - '0') * 10;
			timePair.second += time[1] - '0';
			timePair.second *= 60;
			timePair.second += (time[3] - '0') * 10;
			timePair.second += time[4] - '0';
			timePair.second += turnaroundTime;
			table[1][timePair.second]++;

			bToA.push_back(timePair);
		}
		sort(bToA.begin(), bToA.end(), Sort);

		trainsAtA       = 0;
		trainsAtB       = 0;
		trainsNeededAtA = 0;
		trainsNeededAtB = 0;
		for (t = 0; t < 1440; t++)
		{
			//
			//  Calculate available trains
			//
			trainsAtB += table[0][t];
			trainsAtA += table[1][t];

			for (k = 0; k < aToB.size(); k++)
			{
				if (aToB[k].first == t)
				{
					if (0 >= trainsAtA)
						trainsNeededAtA++;
					else
						trainsAtA--;
				}
			}

			for (k = 0; k < bToA.size(); k++)
			{
				if (bToA[k].first == t)
				{
					if (0 >= trainsAtB)
						trainsNeededAtB++;
					else
						trainsAtB--;
				}
			}
		}

		output << "Case #" << i + 1 << ": " << trainsNeededAtA << ' ' << trainsNeededAtB << endl;
	}

	input.close();
	output.close();

	return 0;
}

