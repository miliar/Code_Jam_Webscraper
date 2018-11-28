#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
using namespace std;

#ifndef ONLINE_JUDGE
#include<fstream>
  ifstream in("b.in");
  ofstream out("b.out");
#define cin in
#define cout out
#endif


struct Time
{
	int hour;
	int minute;

	bool operator<(const Time & b) const 
	{
		return hour < b.hour || hour == b.hour && minute < b.minute;
	}

	bool operator==(const Time& b) const 
	{
		return hour == b.hour && minute == b.minute;
	}

	bool operator<=(const Time & b) const 
	{
		return *this < b || *this == b;
	}

	void normalize()
	{
		if(minute >= 60)
		{
			hour += minute / 60;
			minute = minute % 60;
		}
	}

	void addMinute(int n)
	{
		minute += n;
		normalize();
	}
};

istream& operator>>(istream&is, Time& time) 
{
	char ch;
	is >> time.hour >> ch >> time.minute;
	return is;
}

struct Trip
{
	Time departure;
	Time arrival;
	int direction;

	bool operator < (const Trip& b) const 
	{
		return departure < b.departure || departure == b.departure && arrival < b.arrival;
	}
};

struct Train
{
	Time available;
	int direction;
};

int main()
{
	int cs;
	cin >> cs;



	for(int z = 1; z <=cs; z ++) 
	{
		cout << "Case #"<< z <<": ";

		int a = 0, b = 0;
		int t, na, nb;
		vector<Trip> trips;
		vector<Train> trains;
		
		cin >> t;

		cin >> na >> nb;
		for(int i = 0; i < na; i ++)
		{
			Time time;
			Trip trip;

			cin >> time;
			trip.departure = time;
			cin >> time;
			trip.arrival = time;
			trip.direction = 0;
			trips.push_back(trip);
		}

		for(int i = 0; i < nb; i ++)
		{
			Time time;
			Trip trip;

			cin >> time;
			trip.departure = time;
			cin >> time;
			trip.arrival = time;
			trip.direction = 1;
			trips.push_back(trip);
		}


		sort(trips.begin(), trips.end());

		Time current;
		current.hour = 0;
		current.minute = 0;

		int index = 0;

		for(int i = 0; i < 24 * 60; i ++)
		{
			if(index >= trips.size())
				break;

			while(index < trips.size() && trips[index].departure == current )
			{
				bool found = false;
				for(int j = 0; j < trains.size(); j ++)
				{
					if(trains[j].available <= trips[index].departure && trains[j].direction == trips[index].direction)
					{
						trains.erase(trains.begin() + j);
						found = true;
						break;
					}
				}

				if(!found)
				{
					if(trips[index].direction == 0)
						a ++;
					else b ++;
						
				}

				Train train;
				train.available = trips[index].arrival;
				train.available.addMinute(t);
				train.direction = 1 - trips[index].direction;
				trains.push_back(train);

				index ++;
			}
			
			
			current.addMinute(1);
		}


		cout << a <<' '<< b << endl;
	}

	return 0;
}
