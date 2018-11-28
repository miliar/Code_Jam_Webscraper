#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <limits>
#include <iterator>
#include <algorithm>

using namespace std;
struct journey
{
	unsigned int departure_time;
	unsigned int arrival_time;
	string departure_station;
	string arrival_station;
};

bool Sort(journey a, journey b)
{
	return a.departure_time < b.departure_time;
}

bool Merge(vector<journey>& Journeys)
{
	for(unsigned int i = 0; i < Journeys.size(); ++i)
	{
		for(unsigned int j = i + 1; j < Journeys.size(); ++j)
		{
			if(Journeys[i].arrival_station == Journeys[j].departure_station)
			{
				if(Journeys[i].arrival_time <= Journeys[j].departure_time)
				{
					Journeys[i].arrival_time = Journeys[j].arrival_time;
					Journeys[i].arrival_station = Journeys[j].arrival_station;
					Journeys.erase(Journeys.begin() + j);
					return true;
				}
			}
		}
	}
	return false;
}
int main()
{
	ifstream In("B-large.in");
	ofstream Out("B-large.out");
	unsigned int N = 0;
	In >> N;
	for(unsigned int i = 0; i < N; ++i)
	{
		unsigned int Turn_around = 0;
		In >> Turn_around;
		unsigned int NA = 0, NB = 0;
		In >> NA;
		In >> NB;
		vector<journey> Journeys;
		for(unsigned int j = 0; j < NA; ++j)
		{
			journey Journey;
			Journey.departure_station = "A";
			Journey.arrival_station = "B";
			unsigned int HH = 0, MM = 0;
			In >> HH;
			HH *= 60;
			In.ignore();
			In >> MM;

			Journey.departure_time = HH + MM;

			In >> HH;
			HH *= 60;
			In.ignore();
			In >> MM;

			Journey.arrival_time = HH + MM + Turn_around;
			Journeys.push_back(Journey);
		}
		for(unsigned int j = 0; j < NB; ++j)
		{
			journey Journey;
			Journey.departure_station = "B";
			Journey.arrival_station = "A";
			unsigned int HH = 0, MM = 0;
			In >> HH;
			HH *= 60;
			In.ignore();
			In >> MM;

			Journey.departure_time = HH + MM;

			In >> HH;
			HH *= 60;
			In.ignore();
			In >> MM;

			Journey.arrival_time = HH + MM + Turn_around;
			Journeys.push_back(Journey);
		}
		sort(Journeys.begin(), Journeys.end(), Sort);
		while(Merge(Journeys));
		int A_trains = 0, B_trains = 0;
		for(unsigned int j = 0; j < Journeys.size(); ++j)
		{
			if(Journeys[j].departure_station == "A")
			{
				++A_trains;
				continue;
			}
			++B_trains;
		}
		if(i != 0)
			Out << endl;
		Out << "Case #" << i + 1 << ": " << A_trains << ' ' << B_trains;
	}
	return 0;
}