#include <iostream>
#include <list>
#include <string>
#include <sstream>
#include <fstream>
#include <algorithm>

using namespace std;

void getInput(ifstream& source, int& n)
{
	string inp;
	getline(source, inp);
	istringstream ist(inp);
	ist >> n;
}

void getInput(ifstream& source, int& a, int& b)
{
	string inp;
	getline(source, inp);
	istringstream ist(inp);
	ist >> a >> b;
}

void getTime(ifstream& source, int& de, int& ar)
{
	int a, b, c, d;
	char c1, c2;
	
	string inp;
	getline(source, inp);
	istringstream ist(inp);
	ist >> a >> c1 >> b >> c >> c2 >> d;
	
	de = a * 60 + b;
	ar = c * 60 + d;
}

struct Trip
{
	int departure;
	int arrive;
};

bool RemoveFirst(list<Trip>& lt, int& after, const int turnaround);

int main(int argc, char* argv[])
{
	if( argc != 2 ) return -1;

	std::ifstream source(argv[1]);

	if( !source ) return -1;

	int number;
	getInput(source, number);

	for(int cases = 0; cases < number; cases++)
	{
		int turnaround;
		getInput(source, turnaround);
		
		int na, nb;
		getInput(source, na, nb);
		
		list<Trip> a_trips;
		for(int i = 0; i < na; i++)
		{
			struct Trip t;
			
			getTime(source, t.departure, t.arrive);
			
			list<Trip>::iterator it;
			for(it = a_trips.begin(); it != a_trips.end(); it++)
			{
				if( it->departure > t.departure ||
					it->departure == t.departure && it->arrive >= t.arrive)
				{
					break;
				}
			}
			a_trips.insert(it, t);
		}
		
		list<Trip> b_trips;
		for(int i = 0; i < nb; i++)
		{
			Trip t;
			
			getTime(source, t.departure, t.arrive);
			
			list<Trip>::iterator it;
			for(it = b_trips.begin(); it != b_trips.end(); it++)
			{
				if( it->departure > t.departure ||
					it->departure == t.departure && it->arrive >= t.arrive)
				{
					break;
				}
			}
			b_trips.insert(it, t);			
		}
		
		int a_train = 0, b_train = 0;
		int nexttime;
		while ( !a_trips.empty() && !b_trips.empty() )
		{
			Trip af = a_trips.front();
			Trip bf = b_trips.front();

			if( af.departure <= bf.departure )
			{
				a_train++;
				
				nexttime = a_trips.front().arrive + turnaround;
				a_trips.pop_front();
				
				while(1)
				{
					if( !RemoveFirst(b_trips, nexttime, turnaround) ) break;
					if( !RemoveFirst(a_trips, nexttime, turnaround) ) break;
				}
			}
			else
			{
				b_train++;
				
				nexttime = b_trips.front().arrive + turnaround;
				b_trips.pop_front();
				
				while(1)
				{
					if( !RemoveFirst(a_trips, nexttime, turnaround) ) break;
					if( !RemoveFirst(b_trips, nexttime, turnaround) ) break;
				}				
			} 
	    }
	    
	    if( !a_trips.empty() ) a_train += a_trips.size();
	    if( !b_trips.empty() ) b_train += b_trips.size();
		
		cout << "Case #" << cases + 1 << ": " << a_train << " " << b_train << endl;
	}
	
	return 0;
}

bool RemoveFirst(list<Trip>& lt, int& after, const int turnaround)
{
	for(list<Trip>::iterator i = lt.begin(); i != lt.end(); i++)
	{
		if( i->departure >= after )
		{
			after = i->arrive + turnaround;
			lt.erase(i);
			return 1;
		}
	}
	return 0;
}
