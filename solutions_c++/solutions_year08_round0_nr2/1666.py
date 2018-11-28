#include <fstream>
//#include <iostream>
//#include <string>
#include <vector>
#include <algorithm>
//#include <map>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

struct Time
{
	int hours, minutes;
	
	Time() { }
	Time(int h, int m) : hours(h), minutes(m) { }

	int rawMinutes()
	{
		return minutes + 60 * hours;
	}

	void read()
	{
		fin >> hours;
		fin.ignore();
		fin >> minutes;
	}
};

enum Direction
{
	AtoB,
	BtoA
};

struct Trip
{
	Time start, end;
	Direction dir;
	bool mark;

	Trip() { mark = false; }
	Trip(const Time& s, const Time& e): start(s), end(e) { }

	friend bool operator<(Trip a, Trip b)
	{
		return (a.start.rawMinutes() < b.start.rawMinutes());
	}

	int rawLength()
	{
		return end.rawMinutes() - start.rawMinutes();
	}

	void read()
	{
		start.read();
		end.read();
	}
};

////////////////////////////////////
vector<Trip> trips;
int T;
////////////////////////////////////

void markTrainRoute(int it)
{
	trips[it].mark = true;
	//vector<Trip>::const_iterator it2;
	for (int it2=it+1; it2 < trips.size(); it2++)
	{
		if ((!trips[it2].mark) && (trips[it2].dir != trips[it].dir) && (trips[it2].start.rawMinutes() >= (trips[it].end.rawMinutes() + T)))
		{
			markTrainRoute(it2);
			return;
		}
	}
	return;
}

int main()
{
	int N;
	fin >> N;

	for (int n=1; n <= N; n++)
	{
		
		fin >> T;

		int NA, NB;
		fin >> NA >> NB;

		trips.clear();
		for (int i=0; i<NA; i++)
		{
			Trip t;
			t.read();
			t.dir = AtoB;
			trips.push_back(t);
		}
		for (int i=0; i<NB; i++)
		{
			Trip t;
			t.read();
			t.dir = BtoA;
			trips.push_back(t);
		}

		sort(trips.begin(), trips.end());

		int nATrains = 0, nBTrains = 0;
		//vector<Trip>::const_iterator it;
		for (int it = 0; it < trips.size(); it++)
		{
			if (!trips[it].mark)	//if no train has taken this trip yet
			{
				if (trips[it].dir == AtoB)
				{
					nATrains++;
				}
				else
				{
					nBTrains++;
				}
				markTrainRoute(it);
			}
		}

		fout << "Case #" << n << ": " << nATrains << " " << nBTrains << endl;
	}

	return 0;
}