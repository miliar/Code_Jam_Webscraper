#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

int N;

int T;
int NA;
int NB;
//-----------------------
std::vector<int> _DepaturesFromA;
std::vector<int> _DepaturesFromB;
std::vector<int> _ArrivalsToA;
std::vector<int> _ArrivalsToB;

//-----------------------
int NumTrainsA;
int NumTrainsB;
//-----------------------

void ReadData()
{
	_DepaturesFromA.clear();
	_DepaturesFromB.clear();
	_ArrivalsToA.clear();
	_ArrivalsToB.clear();

	scanf("%i%i%i", &T, &NA, &NB);

	for (int i = 0; i < NA; i++)
	{
		char depHH[3], depMM[3], arrHH[3], arrMM[3];
		scanf("%2s:%2s %2s:%2s", depHH, depMM, arrHH, arrMM);
		
		_DepaturesFromA.push_back(atoi(depHH) * 60 + atoi(depMM));
		_ArrivalsToB.push_back(atoi(arrHH) * 60 + atoi(arrMM));
	}

	for (int i = 0; i < NB; i++)
	{
		char depHH[3], depMM[3], arrHH[3], arrMM[3];
		scanf("%2s:%2s %2s:%2s", depHH, depMM, arrHH, arrMM);

		_DepaturesFromB.push_back(atoi(depHH) * 60 + atoi(depMM));
		_ArrivalsToA.push_back(atoi(arrHH) * 60 + atoi(arrMM));
	}
}

int CountTrains(std::vector<int>& depatures, std::vector<int>& arrivals)
{
	int count = 0;	

	int i = 0;
	int j = 0;

	int curTrains = 0;
	int curTime = 0;

	while (i < arrivals.size() && j < depatures.size())
	{
		if (arrivals[i] + T <= depatures[j])
		{
			curTrains++;
			i++;
		}
		else
		{
			if (curTrains == 0)
			{
				curTrains++;
				count++;
			}
			curTrains--;
			j++;
		}
	}

	while(j < depatures.size())
	{
		if (curTrains == 0)
		{
			curTrains++;
			count++;
		}
		curTrains--;
		j++;
	}

	return count;
}

void Work()
{
	std::sort(_DepaturesFromA.begin(), _DepaturesFromA.end());
	std::sort(_DepaturesFromB.begin(), _DepaturesFromB.end());
	std::sort(_ArrivalsToA.begin(), _ArrivalsToA.end());
	std::sort(_ArrivalsToB.begin(), _ArrivalsToB.end());

	NumTrainsA = CountTrains(_DepaturesFromA, _ArrivalsToA);
	NumTrainsB = CountTrains(_DepaturesFromB, _ArrivalsToB);
}

void WriteResult(int nTest)
{
	printf(
		"Case #%i: %i %i\n",
		nTest,
		NumTrainsA,
		NumTrainsB);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	scanf("%i", &N);

	for (int i = 0; i < N; i++)
	{
		ReadData();
		Work();
		WriteResult(i + 1);
	}

	return 0;
}
