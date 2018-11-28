#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

struct Info {
	enum event_t { NA, NB };

	Info( int depart, int arrive, event_t ty):
	departure(depart), arrival(arrive), type(ty) {};

	Info( event_t ty): type(ty) {};

	int departure;
	int arrival;
	event_t type;
};

class Train {
public:
	enum status_t { at_a, at_b, moving_to_a, moving_to_b };
	
	Train(int ta, status_t st): turnaround(ta), status(st) {};
	
	void depart(Info &info) {
		if( status == status_t::at_a && info.type == Info::event_t::NA)
			status = status_t::moving_to_b;
		else if( status == status_t::at_b && info.type == Info::event_t::NB)
			status = status_t::moving_to_a;
		else
			return;
		arrival = info.arrival;
	}

	void tick( int time) {
		if( status == status_t::at_a || status == status_t::at_b )
			return;
		if( time == arrival + turnaround )
			status = (status == status_t::moving_to_a)?status_t::at_a:status_t::at_b;
	}

private:
	int arrival;
	int turnaround;
	status_t status;

	friend bool AtA(Train&);
	friend bool AtB(Train&);
};

bool AtA( Train& tn ) {
	if( tn.status == Train::status_t::at_a)
		return true;
	return false;
}

bool AtB( Train& tn ) {
	if( tn.status == Train::status_t::at_b)
		return true;
	return false;
}

bool Simulate(int& a_trains, int& b_trains, int turnaround_time, multimap<int, Info> &timetable);

int main() {

	/* Prepare the input file */
	ifstream infile("B-large.in");

	/* Prepare output file */
	ofstream outfile("output.txt");

	/* Read number of test cases */
	int num_of_cases;
	infile >> num_of_cases;

	for( int i = 0; i != num_of_cases; ++i) {

		/* Read turnaround time */
		int turnaround_time;
		infile >> turnaround_time;

		/* Arrange scheduler in to a multimap w/ 
		time being the key and event_t being the value */
		multimap<int, Info> timetable;

		/* Read in number of NA and NB */
		int NA, NB;
		infile >> NA;
		infile >> NB;

		for( int j = 0; j != NA; ++j ) 
		{
			Info detail(Info::event_t::NA);
			int hour, minute;
			
			/* The first time represents the leaving time */
			infile >> hour;
			infile.get(); // Skip over the : sign
			infile >> minute;
			detail.departure = hour*60 + minute;

			/* The second time represents the arrival time */
			infile >> hour;
			infile.get(); // Skip over the : sign
			infile >> minute;
			detail.arrival = hour*60 + minute;

			timetable.insert( make_pair( detail.departure, detail) );
		}

		for( int j = 0; j != NB; ++j ) 
		{
			Info detail(Info::event_t::NB);
			int hour, minute;
			
			/* The first time represents the leaving time */
			infile >> hour;
			infile.get(); // Skip over the : sign
			infile >> minute;
			detail.departure = hour*60 + minute;

			/* The second time represents the arrival time */
			infile >> hour;
			infile.get(); // Skip over the : sign
			infile >> minute;
			detail.arrival = hour*60 + minute;

			timetable.insert( make_pair( detail.departure, detail) );

		}

		/* Now for the main algorithm */
		/* Define the number of initial train at each station */
		int a_trains = 0, b_trains = 0;
		
		while( !Simulate(a_trains, b_trains, turnaround_time, timetable) );
		
		cout << "Case #" << i + 1 << ": " << a_trains << " " <<  b_trains << endl;
		outfile << "Case #" << i + 1 << ": " << a_trains << " " <<  b_trains << endl;
		
	}

	outfile.close();
	infile.close();
	system("pause");
	return 0;
}

bool Simulate(int& a_trains, int& b_trains, int turnaround_time, multimap<int, Info> &timetable) 
{
	/* Keep a list of train objects, with */
	vector<Train> train_list;
	/* number of trains specified in prev variables */
	for( int j = 0; j != a_trains; j++ )
		train_list.push_back( Train(turnaround_time, Train::status_t::at_a ) );
	for( int j = 0; j != b_trains; j++ )
		train_list.push_back( Train(turnaround_time, Train::status_t::at_b ) );

	for( int tick = 0; tick < 60*24; ++tick) 
	{
		/* First supply ticks to every trains */
		for( int j = 0; j != train_list.size(); ++j)
			train_list[j].tick(tick);

		/* Then search the timetable for possible events */
		pair< multimap<int,Info>::iterator, multimap<int,Info>::iterator> result 
			= timetable.equal_range(tick);
		
		while( result.first != result.second ) {

			Info& current_event = result.first->second;
			/* We will need to find a suitable train for the current task
			ie the train would have to be at that station! */
			
			if( current_event.type == Info::event_t::NA ) {
				vector<Train>::iterator avaliable_train
					= find_if( train_list.begin(), train_list.end(), AtA );
				if( avaliable_train == train_list.end() ) {
					++a_trains;
					return false;
				}
				else
					avaliable_train->depart(current_event);
			}
			else {
				vector<Train>::iterator avaliable_train
					= find_if( train_list.begin(), train_list.end(), AtB );
				if( avaliable_train == train_list.end() ) {
					++b_trains;
					return false;
				}
				else
					avaliable_train->depart(current_event);
			}
			++result.first;
		}
	}
	return true;
}