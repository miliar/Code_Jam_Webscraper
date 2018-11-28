#include <stdio.h>
#include <string.h>
#include <string>
#include <map>

using namespace std;

int main(void)
{
	int N;
	int T, NA, NB;
	int timeA[100], timeB[100];
	multimap<int, int> tableA, tableB;
	multimap<int, int>::iterator miA, miB;
	int hour, minute, a, b;
	int lastArrival;
	char departure[8], arrival[8];
	int i, j;
	bool fromA;

	scanf("%d", &N);
	for (i = 0; i < N; i++)
	{
		tableA.clear();
		tableB.clear();
		scanf("%d", &T);
		scanf("%d %d", &NA, &NB);
		for (j = 0; j < NA; j++)
		{
			scanf("%s %s", departure, arrival);
			minute = atoi(departure + 3);
			departure[2] = 0;
			hour = atoi(departure);
			a = hour * 60 + minute;
			minute = atoi(arrival + 3);
			arrival[2] = 0;
			hour = atoi(arrival);
			b = hour * 60 + minute;
			tableA.insert(make_pair<int, int>(b, a));
		}
		for (j = 0; j < NB; j++)
		{
			scanf("%s %s", departure, arrival);
			minute = atoi(departure + 3);
			departure[2] = 0;
			hour = atoi(departure);
			a = hour * 60 + minute;
			minute = atoi(arrival + 3);
			arrival[2] = 0;
			hour = atoi(arrival);
			b = hour * 60 + minute;
			tableB.insert(make_pair<int, int>(b, a));
		}

		timeA[i] = 0;
		timeB[i] = 0;
		lastArrival = -1;
		while (tableA.size() > 0 || tableB.size() > 0)
		{
			if (lastArrival < 0)
			{
				miA = tableA.begin();
				miB = tableB.begin();
				if (miA != tableA.end() && (miB == tableB.end() || miA->second <= miB->second))
				{
					fromA = true;
					timeA[i]++;
					lastArrival = miA->first;
					tableA.erase(miA);
				}
				else
				{
					fromA = false;
					timeB[i]++;
					lastArrival = miB->first;
					tableB.erase(miB);
				}
			}
			else
			{
				if (!fromA)
				{
					for (miA = tableA.begin(); miA != tableA.end(); miA++)
					{
						if (miA->second >= lastArrival + T)
						{
							break;
						}
					}
					if (miA == tableA.end())
					{
						lastArrival = -1;
					}
					else
					{
						lastArrival = miA->first;
						tableA.erase(miA);
						fromA = true;
					}
				}
				else
				{
					for (miB = tableB.begin(); miB != tableB.end(); miB++)
					{
						if (miB->second >= lastArrival + T)
						{
							break;
						}
					}
					if (miB == tableB.end())
					{
						lastArrival = -1;
					}
					else
					{
						lastArrival = miB->first;
						tableB.erase(miB);
						fromA = false;
					}
				}
			}
		}
	}

	for (i = 0; i < N; i++)
	{
		printf("Case #%d: %d %d\n", i + 1, timeA[i], timeB[i]);
	}

	return 0;
}
