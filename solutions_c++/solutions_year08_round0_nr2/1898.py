/*
 * 2008. Gooogle Code Jam.
 * Qualification Round
 *   B. Tran Timetable
 * Code by Kyoungmoon Sun
 */

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <map>

using namespace std;

int str2int( string str )
{
	stringstream stream( str );
	int result;
	stream >> result;
	return result;
}

struct TIME
{
	int hour;
	int min;

	TIME()
	{
	}

	TIME( string& time )
	{
		string hourStr;
		string minStr;

		hourStr += time[0];
		hourStr += time[1];

		minStr += time[3];
		minStr += time[4];

		hour = str2int( hourStr );
		min = str2int( minStr );
	}

	void addMinutes( int minutes )
	{
		min += minutes;
		hour += min / 60;
		min %= 60;
	}

};

bool operator <( const struct TIME& a, const struct TIME& b )
{
	return ( a.hour * 100 + a.min ) < ( b.hour * 100 + b.min );
}

bool operator <=( const struct TIME& a, const struct TIME& b )
{
	return ( a.hour * 100 + a.min ) <= ( b.hour * 100 + b.min );
}

class Train
{
private:
	struct TIME	departure;
	struct TIME	arrival;
	int direction;

public:
	Train( struct TIME departure, struct TIME arrival, int direction )
	{
		this->departure = departure;
		this->arrival = arrival;
		this->direction = direction;
	}

	struct TIME getDeparture()
	{
		return departure;
	}

	struct TIME getArrival()
	{
		return arrival;
	}

	int getDirection()
	{
		return direction;
	}

	bool operator < ( Train& a )
	{
		return departure < a.getDeparture();
	}
};

class Timetable
{
private:
	int turnaroundTime;
	int trainsA;
	int trainsB;
	list<Train>	schedule;

public:
	void setTurnaroundTime( int turnaroundTime )
	{
		this->turnaroundTime = turnaroundTime;
	}

	void addSchedule( Train train )
	{
		schedule.push_back( train );
	}

	int getTrainsA()
	{
		return trainsA;
	}

	int getTrainsB()
	{
		return trainsB;
	}

	void calc()
	{
		vector<TIME>	waitingTrainA;
		vector<TIME>	waitingTrainB;

		trainsA = 0;
		trainsB = 0;

		schedule.sort();

		while( schedule.size() )
		{
			if( schedule.front().getDirection() == 0 )
			{
				// A to B
				vector<TIME>::iterator itr;
				int flag = 0;

				for( itr = waitingTrainA.begin(); itr != waitingTrainA.end(); itr++ )
				{
					if( ( *itr ) <= schedule.front().getDeparture() )
					{
						waitingTrainA.erase( itr );
						flag = 1;
						break;
					}
				}
				if( flag == 0 )
					trainsA++;
				TIME time = schedule.front().getArrival();
				time.addMinutes( turnaroundTime );
				waitingTrainB.push_back( time );
			}
			else
			{
				// B to A
				vector<TIME>::iterator itr;
				int flag = 0;

				for( itr = waitingTrainB.begin(); itr != waitingTrainB.end(); itr++ )
				{
					if( ( *itr ) <= schedule.front().getDeparture() )
					{
						waitingTrainB.erase( itr );
						flag = 1;
						break;
					}
				}
				if( flag == 0 )
					trainsB++;
				TIME time = schedule.front().getArrival();
				time.addMinutes( turnaroundTime );
				waitingTrainA.push_back( time );
			}
			schedule.erase( schedule.begin() );
		}
	}
};

void process( char* filename )
{
	int caseCount;
	int turnaroundTime;
	int i, j;
	string str;
	Timetable table;

	ifstream inputfile( filename );

	if( !inputfile.is_open() )
	{
		cout << "Unable to open " << filename << endl;
		return;
	}

	inputfile >> caseCount;

	for( i = 0; i < caseCount; i++ )
	{
		int fromA;
		int fromB;
		string departure;
		string arrival;

		inputfile >> turnaroundTime;
		table.setTurnaroundTime( turnaroundTime );

		inputfile >> fromA;
		inputfile >> fromB;
		for( j = 0; j < fromA; j++ )
		{
			inputfile >> departure;
			inputfile >> arrival;

			table.addSchedule( Train( departure, arrival, 0 ) );
		}

		for( j = 0; j < fromB; j++ )
		{
			inputfile >> departure;
			inputfile >> arrival;

			table.addSchedule( Train( departure, arrival, 1 ) );
		}

		table.calc();
		cout << "Case #" << i + 1 << ": " << table.getTrainsA() << " " << table.getTrainsB() << endl;
	}

	inputfile.close();
}

int main( int argc, char* argv[] )
{
	if( argc != 2 )
	{
		cout << argv[0] << " [input file]" << endl;
		return 0;
	}

	process( argv[1] );

	return 0;
}
