// B.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

typedef unsigned long long ull;

struct Trip 
{
	unsigned int startTime, endTime;
	bool served;

	Trip(): served(false) {}
	Trip(unsigned int s, unsigned int e, unsigned int se): startTime(s), endTime(e), served(se) {}
};

bool operator < (Trip const &l, Trip const &r)
{
	return l.startTime < r.startTime;
}

std::ifstream in("B.in");
std::ofstream out("B.out");

std::vector< Trip > stations[2];
unsigned int N, NA, NB, T;

Trip stringToTrip(char *str)
{
	return Trip(((str[0] - '0')*10 + str[1] - '0')*60 + ((str[3] - '0')*10 + str[4] - '0'),
			    ((str[6] - '0')*10 + str[7] - '0')*60 + ((str[9] - '0')*10 + str[10] - '0'),
				false);
}

bool firstTrainFromA()
{
	unsigned int a = 0;
	unsigned int b = 0;

	for (; a < stations[0].size(); ++a)
		if (!stations[0][a].served)
			break;

	for (; b < stations[1].size(); ++b)
		if (!stations[1][b].served)
			break;

	if (stations[0].size() == a)
		return false;

	if (stations[1].size() == b)
		return true;

	if (stations[0][a].startTime < stations[1][b].startTime)
		return true;

	return false;
}

unsigned int trip(unsigned int station)
{
	unsigned int currTrip = 0;
	unsigned int lastA = 0, lastB = 0;
	unsigned int result = 0;

	for (; currTrip < stations[station].size(); ++currTrip)
		if (!stations[station][currTrip].served)
			break;

	unsigned int time = stations[station][currTrip].startTime;

	while (true)
	{
		++result;
		time = stations[station][currTrip].endTime + T;
		stations[station][currTrip].served = true;
		
		if (0 == station)
		{
			lastA = currTrip;
			currTrip = lastB;
		}
		else
		{
			lastB = currTrip;
			currTrip = lastA;
		}

		station = (station + 1) % 2;



		for (; currTrip < stations[station].size(); ++currTrip)
		{
			if (!stations[station][currTrip].served && time <= stations[station][currTrip].startTime)
				break;
		}
        
        if (currTrip == stations[station].size())
			break;
	}

	return result;
}

void solve(unsigned int caseNumber)
{
	unsigned int currentServed = 0;
	unsigned int currStation;
	unsigned int trainsA = 0, trainsB = 0;

	while (currentServed != (NA + NB))
	{
		if (firstTrainFromA())
		{
			currStation = 0;
			unsigned int r = trip(currStation);

			++trainsA;
			currentServed += r;
		}
		else
		{
			currStation = 1;
			unsigned int r = trip(currStation);

			++trainsB;
			currentServed += r;

		}
	}

	out << "Case #" << (caseNumber) << ": " << trainsA << " " << trainsB << "\n";
}

int main()
{
	in >> N;

	for (unsigned int i = 0; i < N; ++i)
	{
		in >> T;
		in.get();

		in >> NA;
		in.get();
		stations[0].clear();
		stations[0].reserve(NA);

		in >> NB;
		in.get();
		stations[1].clear();
		stations[1].reserve(NB);

		for (unsigned int k = 0; k < NA; ++k)
		{
			char buf[1000];
			in.getline(buf, 1000, '\n');

			stations[0].push_back(stringToTrip(buf));
		}

		std::sort(stations[0].begin(), stations[0].end());

		for (unsigned int k = 0; k < NB; ++k)
		{
			char buf[1000];
			in.getline(buf, 1000, '\n');

			stations[1].push_back(stringToTrip(buf));
		}

		std::sort(stations[1].begin(), stations[1].end());

		//out << "Case #" << (i + 1) << ": " << NA << " " << NB << "\n";
		solve(i + 1);
	}

	return 0;
}

