// TrainTimeTable.cpp : Defines the entry point for the console application.
//

#include <cstdio>
#include <iostream>
#include <vector>
#include <fstream>
#include <cassert>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;



template<typename T>
T ReadValueAndSkipNext(istream & in)
{
	T t;
	in >> t;
	in.ignore();  //ignore next character
	return t;
}

template<typename T>
T ReadValue(istream & in)
{
	T t;
	in >> t;
	return t;
}

class Trip
{
public:
	enum TripState { Init, Running, Finished };
	Trip(bool dir):dir(dir)
	{
		state = Init;
		start_hour = start_min = end_hour = end_min = 0;
	}
public:
	int start_hour;
	int start_min;
	int end_hour;
	int end_min;
	TripState state;
	bool dir;
};

istream & operator >>(istream & in, Trip & trip)
{
	trip.start_hour = ReadValueAndSkipNext<int>(in);
	trip.start_min = ReadValueAndSkipNext<int>(in);
	trip.end_hour = ReadValueAndSkipNext<int>(in);
	trip.end_min = ReadValueAndSkipNext<int>(in);;
	return in;
}

ostream & operator << (ostream & out, const Trip & trip)
{
	if( trip.dir )
		out << "A-B: " ;
	else
		out << "B-A: ";
	out << setw(2) << setfill('0') << trip.start_hour << ":" << setw(2) << setfill('0') << trip.start_min << " " 
		<< setw(2) << setfill('0') << trip.end_hour << ":" << setw(2) << setfill('0') << trip.end_min;
	return out;
}


template<typename T>
struct PrintStreamable
{
public:
	PrintStreamable(char delimiter = '\0'):delim(delimiter){}
	void operator()( const T & t )
	{
		cout << t ;
		if( delim )
			cout << delim;
	}
private:
	char delim;
};

struct TripCompare
{	
	bool operator()(const Trip & lhs, const Trip & rhs) const
	{
		if( lhs.start_hour < rhs.start_hour )
			return true;
		else if( lhs.start_hour == rhs.start_hour )
		{
			return lhs.start_min < rhs.start_min;
		}
		return false;
	}
};

typedef std::vector<Trip> TripSet;



void ReadTrip( istream & in, int trips1, int trips2, TripSet & tripSet)
{
	tripSet.reserve( trips1+ trips2 );
	for( int i = 0; i < trips1; ++i )
	{
		Trip t( true) ;
		in >> t;
		tripSet.push_back( t );
	}

	for( int i = 0; i < trips2; ++i )
	{
		Trip t(false);
		in >> t;
		tripSet.push_back( t );
	}

	std::sort( tripSet.begin(), tripSet.end(), TripCompare() );
	std::for_each( tripSet.begin(),tripSet.end(), PrintStreamable<Trip>('\n') );
}


class Train
{
public:
	Train(bool dir, int hour, int minute) : dir(dir),hour(hour),minute(minute){}
public:
	bool dir;
	int hour;
	int minute;
};


pair<int,int> Simulation(int turnRoundMinute,TripSet & trips )
{
	int trainAllocatedA = 0;
	int trainAllocatedB = 0;

	vector<Train> trainsAvail;

	for( int hour = 0; hour < 24; ++hour )
	{
		for( int minute = 0; minute < 60; ++minute )
		{
			for( size_t i = 0; i < trips.size(); ++i )
			{
				Trip & trip = trips[i];
				if( trip.start_hour == hour && trip.start_min == minute  && trip.state == Trip::Init )
				{
				
					bool avail = false;
					for( vector<Train>::iterator  k = trainsAvail.begin(); k != trainsAvail.end(); ++k )
					{
						const Train & train = *k;
						if( train.hour < hour || ( train.hour == hour && train.minute <= minute) )
						{
							if( train.dir == trip.dir )
							{
								// OK, available
								trainsAvail.erase(k);
								avail = true;
								break;
							}
						}
					}

					if( !avail)
					{
						if( trip.dir )
							trainAllocatedA++;
						else
							trainAllocatedB++;
					}
					trip.state = Trip::Running;
				}
				else if( trip.end_hour == hour && trip.end_min == minute && trip.state == Trip::Running )
				{
					trip.state = Trip::Finished;
					int train_h = hour + (minute + turnRoundMinute) / 60;
					int train_m = (minute + turnRoundMinute) %60;
					// add a new train at finished time + turn_round_time
					trainsAvail.push_back( Train( !trip.dir, train_h, train_m) );
				}
			}
		

		}
	}
	return pair<int,int>(trainAllocatedA,trainAllocatedB);
}


int main(int argc, char * argv[])
{
	if ( argc < 3 )
	{
		cout << "TrainTimeTable inputfile outputfile" << endl;
		return 1;
	}

	ifstream in(argv[1],ios::in);
	ofstream out(argv[2]);
	if( !in )
	{
		cout << "can't open input file" << endl;
		return 1;
	}

	if( !out )
	{
		cout << "can't open output file" << endl;
		return 1;
	}
	

	int totalCase = 0;
	in>> totalCase;
	cout << totalCase << endl;
	assert( totalCase > 0 );

	for( int i = 1; i <= totalCase; ++i )
	{
		TripSet trips;
		int turnRoundMinute = ReadValueAndSkipNext<int>(in);
		int numAtoB = ReadValue<int>(in);
		int numBtoA = ReadValueAndSkipNext<int>(in);

		cout << "------------------------------------" << endl;
		cout << "Total trips: " << numAtoB+numBtoA << ". Turnround time: " << turnRoundMinute << " minutes."  << endl;

		ReadTrip(in,numAtoB,numBtoA,trips);


		pair<int,int> ret = Simulation(turnRoundMinute,trips);
		cout << "Case #" << i <<": " << ret.first << " " << ret.second << endl;
		out << "Case #" << i <<": " <<  ret.first << " " << ret.second << endl;
	}
	return 0;
}



