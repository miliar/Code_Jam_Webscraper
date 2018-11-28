
#include <iostream>
#include <fstream>
#include <list>

using namespace std;

typedef struct _Time {
	int hr;
	int mins;

	_Time():hr(0),mins(0) {}
	_Time(int h, int m):hr(h),mins(m) {}

	_Time operator+( int minutes ) { 
		_Time temp;
		temp.hr = hr;
		temp.mins = mins + minutes;
		while( temp.mins > 59 )
		{
			++temp.hr;
			temp.mins -= 60;
		}
		return temp;
	}

	bool operator<( _Time second) {
		if( hr < second.hr )
			return true;
		else if( hr == second.hr && mins < second.mins )
			return true;
		return false;
	}

	bool operator<=( _Time second) {
		if( hr < second.hr )
			return true;
		else if( hr == second.hr && mins <= second.mins )
			return true;
		return false;
	}

} Time;

typedef struct _Train {
	Time dep, arr;
	char stn;
	_Train():dep(),arr() {}
	_Train( char* hhmm, char s ) {			// HH:MM HH:MM
		hhmm[2] = NULL;
		hhmm[5] = NULL;
		hhmm[8] = NULL;
		dep.hr = atoi(hhmm);
		dep.mins = atoi(hhmm+3);
		arr.hr = atoi(hhmm+6);
		arr.mins = atoi(hhmm+9);
		stn = s;
	}
} Train;

bool compare_train( Train first, Train second ) 
{
	if( first.dep < second.dep )
		return true;
	return false;
}

// Returns true if a train is ready at a station
// Train is scheduled and no more available
bool sendFreeTrain( list<Time>& freeTrains, Time& dep )
{
	list<Time>::iterator it = freeTrains.begin();
	for( ; it != freeTrains.end() ; ++it ) {
		if( *it <= dep ) {
			freeTrains.erase(it);
			return true;
		}
	}
	return false;
}

int main()
{
	ifstream in;
	ofstream out;
	in.open("inTS.txt",ios::in);
	out.open("outTS.txt",ios::out);
	int iterations = 0;
	list<Train> schedule;
	list<Time> freeTrainsA, freeTrainsB;
	int nTrainsA = 0, nTrainsB = 0;
	int turnAround;
	char buffer[100];
	Train train;
	in >> iterations >> ws;
	for( int ite = 1; ite <= iterations ; ++ite ) {
		schedule.clear();
		freeTrainsA.clear();
		freeTrainsB.clear();
		in >> turnAround >> ws;
		in >> nTrainsA >> nTrainsB >> ws;
		for( int i=1 ; i <= nTrainsA ; ++i ) {
			in.getline(buffer,100);
			schedule.push_back(Train(buffer,'A'));
		}
		for( int i=1 ; i <= nTrainsB ; ++i ) {
			in.getline(buffer,100);
			schedule.push_back(Train(buffer,'B'));
		}
		nTrainsA = nTrainsB = 0;
		schedule.sort(compare_train);	// Start from earliest train
		for(;;) {
			if( !schedule.empty() ) {
				train = schedule.front();
				schedule.pop_front();
			}
			else
				break;
			if( !sendFreeTrain( train.stn=='A' ? freeTrainsA : freeTrainsB, train.dep ) ) {
				train.stn=='A' ? ++nTrainsA : ++nTrainsB;	// No trains ready, send new train
			}
			// Add the train to list of trains available at opposite station
			train.stn=='A' ? freeTrainsB.push_back(train.arr+turnAround) : freeTrainsA.push_back(train.arr+turnAround);
		}
		out << "Case #" << ite << ": " << nTrainsA << " " << nTrainsB << endl; 
	}
	in.close();
	out.close();
	return 0;
}