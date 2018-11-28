
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>

using namespace std;

const int MAX_TIME = (24*60)*2;

int readyAtTimeA[MAX_TIME];
int needAtTimeA[MAX_TIME];

int readyAtTimeB[MAX_TIME];
int needAtTimeB[MAX_TIME];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int caseCount;
	cin >> caseCount;
	for (int caseNum=1; caseNum<=caseCount; caseNum++)
	{
		int turnTime, fromACount, fromBCount;
		cin >> turnTime >> fromACount >> fromBCount;

		memset(readyAtTimeA, 0, sizeof readyAtTimeA);
		memset(readyAtTimeB, 0, sizeof readyAtTimeB);
		memset(needAtTimeA, 0, sizeof needAtTimeA);
		memset(needAtTimeB, 0, sizeof needAtTimeB);

		char ch;
		int hSrc, mSrc, hDest, mDest;

		for (int a=0; a<fromACount; a++)
		{
			cin >> hSrc >> ch >> mSrc >> hDest >> ch >> mDest;
			const int timeSrc = hSrc*60 + mSrc;
			const int timeDest = hDest*60 + mDest + turnTime;

			needAtTimeA[timeSrc]++;
			readyAtTimeB[timeDest]++;
		}

		for (int b=0; b<fromBCount; b++)
		{
			cin >> hSrc >> ch >> mSrc >> hDest >> ch >> mDest;
			const int timeSrc = hSrc*60 + mSrc;
			const int timeDest = hDest*60 + mDest + turnTime;

			needAtTimeB[timeSrc]++;
			readyAtTimeA[timeDest]++;
		}

		int trainsA = 0;
		int trainsB = 0;
		int readyA = 0;
		int readyB = 0;

		for (int t=0; t<MAX_TIME; t++)
		{
			readyA += readyAtTimeA[t];
			readyB += readyAtTimeB[t];

			while (needAtTimeA[t] > 0)
			{
				if (readyA == 0)
				{
					trainsA++;
					readyA++;
				}

				readyA--;
				readyAtTimeA[t]--;
				needAtTimeA[t]--;
			}

			while (needAtTimeB[t] > 0)
			{
				if (readyB == 0)
				{
					trainsB++;
					readyB++;
				}

				readyB--;
				readyAtTimeB[t]--;
				needAtTimeB[t]--;
			}
		}

		cout << "Case #" << caseNum << ": " << trainsA << " " << trainsB << endl;
	}

	return 0;
}


