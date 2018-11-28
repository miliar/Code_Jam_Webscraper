#include <iostream>

using namespace std;

struct times
{
	int d;
	int a;
};

int main()
{
	int numCases;

	cin >> numCases;

	for(int caseNumber = 1; caseNumber <= numCases; caseNumber++)
	{
		int turnaround, NA, NB;
		times A[100], B[100];
		char c;
		int ATrains = 0, BTrains = 0;

		cin >> turnaround >> NA >> NB;

		for(int i = 0, d1, d2, a1, a2; i < NA; i++)
		{
			cin >> d1 >> c >> d2 >> a1 >> c >> a2;
			A[i].d = 100 * d1 + d2;
			A[i].a = 100 * a1 + a2;
		}

		for(int i = 0, d1, d2, a1, a2; i < NB; i++)
		{
			cin >> d1 >> c >> d2 >> a1 >> c >> a2;
			B[i].d = 100 * d1 + d2;
			B[i].a = 100 * a1 + a2;
		}

		while( (NA > 0) && (NB > 0) )
		{
			bool currentIsA = true;

			int current = 0;
			times currentTime = A[0];
			times* currentArray;
			times* oppositeArray;
			int* currentArrayLength;
			int* oppositeArrayLength;

			for(int i = 1; i < NA; i++)
				if(A[i].d < currentTime.d)
				{
					currentTime = A[i];
					current = i;
				}

			for(int i = 0; i < NB; i++)
				if(B[i].d < currentTime.d)
				{
					currentTime = B[i];
					current = i;
					currentIsA = false;
				}

			if(currentIsA)
			{
				A[current] = A[NA - 1];
				NA--;
				ATrains++;
			}
			else
			{
				B[current] = B[NB - 1];
				NB--;
				BTrains++;
			}

			do
			{
				if(currentIsA)
				{
					currentArray = A;
					currentArrayLength = &NA;
					oppositeArray = B;
					oppositeArrayLength = &NB;
				}
				else
				{
					currentArray = B;
					currentArrayLength = &NB;
					oppositeArray = A;
					oppositeArrayLength = &NA;
				}

				int min = oppositeArray[0].d - currentTime.a - turnaround;
				int minLoc = 0;

				for(int i = 0; i < *oppositeArrayLength; i++)
				{
					int t = oppositeArray[i].d - currentTime.a - turnaround;

					if(t >= 0)
						if( (min < 0) || (t < min) )
						{
							min = t;
							minLoc = i;
						}
				}

				if(min >= 0)
				{
					currentTime = oppositeArray[minLoc];
					oppositeArray[minLoc] = oppositeArray[(*oppositeArrayLength) - 1];
					(*oppositeArrayLength)--;
					currentIsA = !currentIsA;
				}
				else
					break;
			} while((*currentArrayLength) > 0);
		}

		ATrains += NA;
		BTrains += NB;

		cout << "Case #" << caseNumber << ": " << ATrains << ' ' << BTrains << '\n';
	}

	return(0);
}
