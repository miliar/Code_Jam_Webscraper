#include <algorithm>
#include <iostream>
#include <vector>

#define VECTOR vector<pair<int, EventType>>
#define VECTOR_PAIR pair<int, EventType>

using namespace std;

enum EventType
{
	A_Arrival,
	B_Arrival,
	A_Departure,
	B_Departure,
};

bool comp(VECTOR_PAIR elem1, VECTOR_PAIR elem2)
{
	return elem1.first == elem2.first ? elem1.second < elem2.second : elem1.first < elem2.first;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testNum;
	cin >> testNum;

	for (int testId = 0; testId < testNum; testId++)
	{
		int t, na, nb;
		cin >> t >> na >> nb;

		VECTOR events;
		events.reserve((na + nb) * 2);

		for (int i = 0; i < na; i++)
		{
			int hours, minutes;

			scanf("%d:%d", &hours, &minutes);
			events.push_back(VECTOR_PAIR(hours * 60 + minutes, A_Departure));

			scanf("%d:%d", &hours, &minutes);
			events.push_back(VECTOR_PAIR(hours * 60 + minutes + t, B_Arrival));
		}

		for (int i = 0; i < nb; i++)
		{
			int hours, minutes;
			
			scanf("%d:%d", &hours, &minutes);
			events.push_back(VECTOR_PAIR(hours * 60 + minutes, B_Departure));

			scanf("%d:%d", &hours, &minutes);
			events.push_back(VECTOR_PAIR(hours * 60 + minutes + t, A_Arrival));
		}

		sort(events.begin(), events.end(), comp);

		int initTrainA = 0, initTrainB = 0, curTrainA = 0, curTrainB = 0;

		for (VECTOR::const_iterator i = events.begin(); i != events.end(); i++)
		{
			switch (i->second)
			{
			case A_Departure:
				// Поезд отходит от станции А
				if (curTrainA < 1)
				{
					initTrainA++;
				}
				else
				{
					curTrainA--;
				}

				break;

			case A_Arrival:
				// Поезд прибыл на станцию А и прошло t минут
				curTrainA++;
				break;

			case B_Departure:
				// Поезд отходит от станции B
				if (curTrainB < 1)
				{
					initTrainB++;
				}
				else
				{
					curTrainB--;
				}

				break;

			case B_Arrival:
				// Поезд прибыл на станцию B и прошло t минут
				curTrainB++;
				break;
			}
		}

		cout << "Case #" << testId + 1 << ": " << initTrainA << ' ' << initTrainB << endl;
	}

	return 0;
}