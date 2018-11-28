#include <iostream>
#include <queue>
#include <string>

using namespace std;

struct trip_time
{
	int start;	//minutes;
	int end;	//minutes;
};

struct station
{
	int trip_num;
	int train_num;
	vector<trip_time> trips;
	vector<trip_time> arriving;
};

void computeTrainNums( int turnaround, struct station *A, struct station *B )
{
	int cur_time = 0;

	while( A->trip_num || B-> trip_num )
	{
		if( A->trip_num )
		{
			while( !A->trips.empty() && cur_time == A->trips.front().start )
			{
				if( A->arriving.empty() )
				{
					int i;
					for( i = 0; i < B->arriving.size(); i++)
					{
						if( A->trips.front().end < B->arriving[i].end )
							break;
					}
					B->arriving.insert( B->arriving.begin()+i, A->trips.front() );
					A->trips.erase( A->trips.begin() );
					A->trip_num--;
					A->train_num++;
				}
				else if( A->arriving.front().end + turnaround <= A->trips.front().start )
				{
					A->arriving.erase( A->arriving.begin() );
					int i;
					for( i = 0; i < B->arriving.size(); i++)
					{
						if( A->trips.front().end < B->arriving[i].end )
							break;
					}
					B->arriving.insert( B->arriving.begin()+i, A->trips.front() );
					A->trips.erase( A->trips.begin() );
					A->trip_num--;
				}
				else
				{
					int i;
					for( i = 0; i < B->arriving.size(); i++)
					{
						if( A->trips.front().end < B->arriving[i].end )
							break;
					}
					B->arriving.insert( B->arriving.begin()+i, A->trips.front() );
					A->trips.erase( A->trips.begin() );
					A->trip_num--;
					A->train_num++;
				}
			}
		}

		if( B->trip_num )
		{
			while( !B->trips.empty() && cur_time == B->trips.front().start )
			{
				if( B->arriving.empty() )
				{
					int i;
					for( i = 0; i < A->arriving.size(); i++)
					{
						if( B->trips.front().end < A->arriving[i].end )
							break;
					}
					A->arriving.insert( A->arriving.begin()+i, B->trips.front() );
					B->trips.erase( B->trips.begin() );
					B->trip_num--;
					B->train_num++;
				}
				else if( B->arriving.front().end + turnaround <= B->trips.front().start )
				{
					B->arriving.erase( B->arriving.begin() );
					int i;
					for( i = 0; i < A->arriving.size(); i++)
					{
						if( B->trips.front().end < A->arriving[i].end )
							break;
					}
					A->arriving.insert( A->arriving.begin()+i, B->trips.front() );
					B->trips.erase( B->trips.begin() );
					B->trip_num--;
				}
				else
				{
					int i;
					for( i = 0; i < A->arriving.size(); i++)
					{
						if( B->trips.front().end < A->arriving[i].end )
							break;
					}
					A->arriving.insert( A->arriving.begin()+i, B->trips.front() );
					B->trips.erase( B->trips.begin() );
					B->trip_num--;
					B->train_num++;
				}
			}
		}
	
		cur_time++;
	}
}


void handleCase( int *A_num, int *B_num )
{
	struct station A, B;
	int turnaround;
	string start, end;
	cin >> turnaround;

	cin>> A.trip_num >> B.trip_num;
	A.train_num = 0;
	B.train_num = 0;

	for( int i = 0; i < A.trip_num; i++ )
	{
		int hour, minute;
		trip_time time;

		cin>>start;
		hour = atoi( start.substr(0,2).c_str() );
		minute = atoi( start.substr(3,2).c_str() );
		time.start = 60*hour + minute;

		cin>>end;
		hour = atoi( end.substr(0,2).c_str() );
		minute = atoi( end.substr(3,2).c_str() );
		time.end = 60*hour + minute;

		int j = 0;
		for( j = 0; j < A.trips.size(); j ++ )
		{
			if( time.start < A.trips[j].start )
				break;
			else if( time.start == A.trips[j].start && time.end < A.trips[j].end )
				break;
			
		}
		A.trips.insert(A.trips.begin()+j, time);
	}

	for( int i = 0; i < B.trip_num; i++ )
	{
		int hour, minute;
		trip_time time;

		cin>>start;
		hour = atoi( start.substr(0,2).c_str() );
		minute = atoi( start.substr(3,2).c_str() );
		time.start = 60*hour + minute;

		cin>>end;
		hour = atoi( end.substr(0,2).c_str() );
		minute = atoi( end.substr(3,2).c_str() );
		time.end = 60*hour + minute;

		int j = 0;
		for( j = 0; j < B.trips.size(); j ++ )
		{
			if( time.start < B.trips[j].start )
				break;
			else if( time.start == B.trips[j].start && time.end < B.trips[j].end )
				break;
		}
		B.trips.insert(B.trips.begin()+j, time);
	}
	
	computeTrainNums( turnaround, &A, &B );
	*A_num = A.train_num;
	*B_num = B.train_num;
}

int main()
{
	int case_nums;
	cin >> case_nums;

	for( int i = 0; i < case_nums; i++ )
	{
		int A_trains, B_trains;
		handleCase(&A_trains, &B_trains);
		cout << "Case #" << i+1 << ": " << A_trains << " " << B_trains << endl;
	}
}
