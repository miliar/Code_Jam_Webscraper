

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

enum Station { StationA, StationB };

/*Station other( Station st )
{
	if( st == StationA ) return StationB;
	else return StationA;
}*/

class Hora
{
public:
	int hour;
	int minute;
	
	int total_minutes() const { return hour * 60 + minute; };
	bool operator<( const Hora &t ) const  { return total_minutes() < t.total_minutes(); }
	bool operator<=( const Hora &t ) const { return total_minutes() <= t.total_minutes(); }
	bool operator>( const Hora &t ) const  { return total_minutes() > t.total_minutes(); }
	bool operator>=( const Hora &t ) const { return total_minutes() >= t.total_minutes(); }
	bool operator==( const Hora &t ) const { return total_minutes() == t.total_minutes(); }

	void set_minutes( int mins ) {
		hour = mins / 60;
		minute = mins % 60; }
	
	void operator+=( const int mins ){
		set_minutes( total_minutes() + mins );}
	void operator+=( const Hora hr ){
		set_minutes( total_minutes() + hr.total_minutes() );}
};

istream& operator>>(istream& is, Hora& h) 
{
	char c;
	is >> h.hour >> c >> h.minute;
	return is;
}

ostream& operator<<(ostream& os, Hora& h) 
{
	os << h.hour << ":" << h.minute;
	return os;
}

class Trip
{
public:
	Hora start;
	Hora finish;
	Station destination;
	Station origin;
	
	bool operator<( const Trip &t ) const  { return start < t.start; }
	bool operator<=( const Trip &t ) const { return start <= t.start; }
	bool operator>( const Trip &t ) const  { return start > t.start; }
	bool operator>=( const Trip &t ) const { return start >= t.start; }
	bool operator==( const Trip &t ) const { return start == t.start; }
};

istream& operator>>(istream& is, Trip& t) 
{
	is >> t.start;
	is >> t.finish;
	return is;
}

ostream& operator<<(ostream& os, Trip& t) 
{
	if( t.destination == StationA )
	{
		os << "B to A: " << t.start << "-" << t.finish;
	}
	else
	{
		os << "A to B: " << t.start << "-" << t.finish;
	}

	return os;
}

class Train
{
	friend ostream& operator<<(ostream& os, Train& tr);
	
public:
	Train(){};
	Train(Station br, Station st, Hora hr)
	: birth(br), whereAt(st), time(hr){};

	Station birth;
	Station whereAt;
	Hora time;
};

ostream& operator<<(ostream& os, Train& train)
{
	os << train.birth;
	return os;
}


int main()
{
	ifstream inf( "B-large.in", ifstream::in );
	ofstream ouf( "B-large.out", ofstream::out );
	
	float ncases;
	inf >> ncases;
	
	for( int n = 0; n < ncases; n++ )
	{
		vector<Trip> trips;
		vector<Train> trains;
		int turnaround, NA, NB;
		
		inf >> turnaround >> NA >> NB; 
		
		for( int i = 0; i < NA; i++ )
		{
			Trip trip;
			trip.origin = StationA;
			trip.destination = StationB;
			inf >> trip;
			trips.push_back(trip);
		}
		for( int i = 0; i < NB; i++ )
		{
			Trip trip;
			trip.origin = StationB;
			trip.destination = StationA;
			inf >> trip;
			trips.push_back(trip);
		}
		
		for( unsigned int i = 0; i < trips.size(); i++ )
		{
			//std::cout << trips[i] << std::endl;
		}
		//std::cout << std::endl;
		
		
		std::sort( trips.begin(), trips.end() );
		
		for( unsigned int i = 0; i < trips.size(); i++ )
		{
			//std::cout << trips[i] << std::endl;
		}
		//std::cout << std::endl;
		
		bool found_train;
		
		vector<Trip>::iterator trip = trips.begin(), end_trip = trips.end();
		for( ; trip != end_trip; ++trip ) //for each trip
		{
			found_train = false;
			for( unsigned int i = 0; i < trains.size(); i++ )
			{
				if( trains[i].whereAt == trip->origin &&
					 trip->start >= trains[i].time )
				{
					trains[i].whereAt = trip->destination;
					trains[i].time = trip->finish;
					trains[i].time += turnaround;
					found_train = true;
					break;
				}
			}
			if( !found_train )
			{
				Hora time = trip->finish;
				time += turnaround;
				trains.push_back( Train( trip->origin, trip->destination, time) );
			}
		}
		
		int stA=0, stB=0;
		//cout << "TRAINS:" << endl;
		vector<Train>::iterator train = trains.begin(), end_train = trains.end();
		for( ; train != end_train; ++train )
		{
			//cout << *train << endl;
			if( train->birth == StationA ) stA++;
			else stB++;
		}
		
		
		cout << "Case #" << n+1 << ": " << stA << " " << stB << endl;
		ouf << "Case #" << n+1 << ": " << stA << " " << stB << endl;
	}
	
	inf.close();
	ouf.close();
	
	return 0;
}

