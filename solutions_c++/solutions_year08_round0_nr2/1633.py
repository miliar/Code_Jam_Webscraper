#include <boost/foreach.hpp>
#include <boost/lexical_cast.hpp>
#include <cstdlib>
#include <exception>
#include <iomanip>
#include <iostream>
#include <new>
#include <set>
#include <sstream>
#include <string>

using namespace std;
using namespace boost;

#define FOR BOOST_FOREACH

string read_line()
{
    string Line;
    getline(cin, Line);
    return Line;
}

string format_time(int Time)
{
    stringstream stream;
    stream << setw(2) << setfill('0') << (Time / 60);
    stream << ':';
    stream << setw(2) << setfill('0') << (Time % 60);
    return stream.str();
}

string format_station(int Station)
{
    const char StationNames[2] = {'A', 'B'};
    stringstream stream;
    stream << '[' << StationNames[Station] << ']';
    return stream.str();
}

struct trip
{
    int Station;
    int Departs;
    int Arrives;

    trip(int Station, int Departs, int Arrives): Station(Station), Departs(Departs), Arrives(Arrives) {}
    bool operator <(trip Trip) const {return Departs < Trip.Departs;}
};

struct train
{
    int Train;
    int Ready;

    train(int Train, int Ready): Train(Train), Ready(Ready) {}
    bool operator <(train Train) const {return Ready < Train.Ready;}
};

int main()
{
    try
    {
	int N = lexical_cast< int >(read_line());
#ifndef NDEBUG
	cerr << string(80, '-') << endl;
#endif
	for(int n = 0; n < N; ++n)
	{
	    int T = lexical_cast< int >(read_line());
	    int NA, NB;
	    {
		stringstream stream(read_line());
		stream >> NA >> NB;
	    }
	    multiset< trip > Trips;
	    for(int na = 0; na < NA; ++na)
	    {
		stringstream stream(read_line());
		int DepartHour, DepartMinute, ArriveHour, ArriveMinute;
		char Colon;
		stream >> DepartHour >> Colon >> DepartMinute >> ArriveHour >> Colon >> ArriveMinute;
		Trips.insert(trip(0, DepartHour * 60 + DepartMinute, ArriveHour * 60 + ArriveMinute));
	    }
	    for(int nb = 0; nb < NB; ++nb)
	    {
		stringstream stream(read_line());
		int DepartHour, DepartMinute, ArriveHour, ArriveMinute;
		char Colon;
		stream >> DepartHour >> Colon >> DepartMinute >> ArriveHour >> Colon >> ArriveMinute;
		Trips.insert(trip(1, DepartHour * 60 + DepartMinute, ArriveHour * 60 + ArriveMinute));
	    }
	    multiset< train > Pool[2];
	    int Trains[2] = {0, 0};
	    FOR(trip Trip, Trips)
	    {
#ifndef NDEBUG
		cerr << format_time(Trip.Departs) << ' ' << format_station(Trip.Station) << " -> " << format_station(Trip.Station ^ 1) << ' ' << format_time(Trip.Arrives) << ' ';
#endif
		multiset< train >::iterator Train = Pool[Trip.Station].begin();
		if(Train == Pool[Trip.Station].end() || Trip.Departs < Train->Ready)
		{
#ifndef NDEBUG
		    cerr << "(train " << (Trains[0] + Trains[1] + 1) << ")";
#endif
		    Pool[Trip.Station ^ 1].insert(train(Trains[0] + Trains[1], Trip.Arrives + T));
		    ++Trains[Trip.Station];
		}
		else
		{
#ifndef NDEBUG
		    cerr << "(train " << (Train->Train + 1) << ")";
#endif
		    Pool[Trip.Station ^ 1].insert(train(Train->Train, Trip.Arrives + T));
		    Pool[Trip.Station].erase(Train);
		}
#ifndef NDEBUG
		cerr << endl;
#endif
	    }
	    cout << "Case #" << (n + 1) << ": " << Trains[0] << ' ' << Trains[1] << endl;
#ifndef NDEBUG
	cerr << string(80, '-') << endl;
#endif
	}
	return EXIT_SUCCESS;
    }
    catch(const exception& Exception)
    {
	cerr << "STL exception: " << Exception.what() << endl;
	return EXIT_FAILURE;
    }
}
