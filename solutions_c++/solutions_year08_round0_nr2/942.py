#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <algorithm>

using namespace std;

struct Trip
{
	int start;
	int end;
	char from;

	Trip &operator=( Trip &tr)
	{
		this->start = tr.start;
		this->end = tr.end;
		this->from = tr.from;
		return *this;
	};
};

bool stoi( string &str, int &n )
{
	int res = 0;
	for( int i = 0; i != str.length(); i++ )
	{
		if ( str[i] - '0' > 9 || str[i] - '0' < 0 )
			return false;
		res = res * 10 + str[i] - '0';
	}
	n = res;
	return true;
}

bool stot( string &str, int &time)
{
	int res1 = 0;
	int res2 = 0;
	for( int i = 0; i != 2 ; i++ )
	{
		if ( str[i] - '0' > 9 || str[i] - '0' < 0 )
			return false;
		res1 = res1 * 10 + str[i] - '0';
	}
	res1 = res1 * 60;
	for( int i = 3; i != 5; i++ )
	{
		if ( str[i] - '0' > 9 || str[i] - '0' < 0 )
			return false;
		res2 = res2 * 10 + str[i] - '0';
	}
	time = res1 + res2;
	return true;
}

bool compare( Trip tr1, Trip tr2 )
{
	return tr1.start < tr2.start;
}

vector<Trip>::iterator find( vector<Trip> &vec_trip, int start )
{
	
	for( vector<Trip>::iterator it = vec_trip.begin(); it != vec_trip.end(); it++ )
	{
		if ( it->start >= start )
			return it;
	}
	return vec_trip.end();
}

int find_start( vector<Trip> &trip_a, vector<Trip> &trip_b )
{
	if ( trip_a[0].start < trip_b[0].start )
		return 1;
	else 
		return 0;
}

bool delete_trip( vector<Trip> &trip_a, vector<Trip> &trip_b, int tr_time )
{
	Trip tr = trip_a[0];
	int start = tr.start;
	vector<Trip>::iterator it;;
	while( true )
	{
		if ( trip_a.empty() )
			return true;
		it = find( trip_a, start );
		if ( it == trip_a.end() )
			return true;
		tr = *it;
		trip_a.erase( it );

		start = tr.end + tr_time;
			
		if ( trip_b.empty() )
			return true;
		it = find( trip_b, start );
		if ( it == trip_b.end() )
			return true;
		tr = *it;
		trip_b.erase( it );
		
		start = tr.end + tr_time;
	}
}

bool find_train( vector<int> &trains, int start )
{
	if ( trains.empty() )
		return false;
	if( trains[0] <= start )
	{
		trains.erase( trains.begin() );
		return true;
	}
	return false;
}

bool insert_train( vector<int> &trains, int start )
{
	if ( trains.empty() )
	{
		trains.push_back( start );
		return true;
	}
	for( vector<int>::iterator it = trains.begin(); it != trains.end(); it++ )
	{
		if ( *it > start )
		{
			trains.insert( it, start );
			return true;
		}
	}
	trains.push_back( start );
	return true;
}

int main(int argc, char* argv[])
{
	//define file stream
	ofstream outfile;
	ifstream infile;	

	//the file name;
	string filename;

	if ( argc == 2 )
		filename = argv[1];
	else 
	{
		if ( argc == 1 )
			cout<<"please enter the name of the input data file:";
		else
			cout<<"the arguments number is wrong, please enter the name of input data file:";
		cin>>filename;
	}
	
	//open output file and input file
	outfile.open("output");
	infile.open(filename.c_str());
	
	if ( !infile )
	{
		cout<<"error, the input data file is invalid"<<endl;
		exit(0);
	}
	//the string that is used to read each line of input data file
	string line;
	//case num
	int case_num;
	
	case_num = 0;
	
	getline(infile, line);
	if( !stoi( line, case_num ) )
	{
		cout<<"error, the case num is invalid"<<endl;
		exit(0);
	}

	//turnround time
	int tr_time;

	Trip trip;
	
	int trip_a_num;
	int trip_b_num;

	int train_a_num;
	int train_b_num;

	vector<Trip> trip_a;
	vector<Trip> trip_b;
	
	vector<int> trains_a;
	vector<int> trains_b;

	stringstream sline;
	string fir_str, sec_str;
	int start, end;

	

	for( int xnum = 0; xnum != case_num; xnum++ )
	{
		trip_a.clear();
		trip_b.clear();
		trains_a.clear();
		trains_b.clear();
		tr_time = 0;
		trip_a_num = 0;
		trip_b_num = 0;
		train_a_num = 0;
		train_b_num = 0;

		getline(infile, line);
		if ( !stoi(line, tr_time) )
		{
			cout<<"error, the turnround time is invalid"<<endl;
			exit(0);
		}
		
		getline(infile, line);
		sline.clear();
		sline.str(line);
		sline>>fir_str>>sec_str;
		if( !stoi(fir_str, trip_a_num) || !stoi(sec_str, trip_b_num) )
		{
			cout<<"error, the trip num is invalid"<<endl;
			exit(0);
		}
		
		for( int i = 0; i != trip_a_num; i++ )
		{
			getline(infile, line);
			sline.clear();
			sline.str(line);
			sline>>fir_str>>sec_str;
			
			if ( !stot( fir_str, start ) || !stot( sec_str, end ) || start >= end )
			{
				cout<<"error, the time of A of "<<line<<" is invalid"<<endl;
				exit(0);
			}
			
			trip.start = start;
			trip.end = end;
			trip.from = 'A';
			
			trip_a.push_back(trip);
			
		}
		
		for( int i = 0; i != trip_b_num; i++ )
		{
			getline(infile, line);
			sline.clear();
			sline.str(line);
			sline>>fir_str>>sec_str;
			
			if ( !stot( fir_str, start ) || !stot( sec_str, end ) || start >= end )
			{
				cout<<"error, the time of B of "<<line<<" is invalid"<<endl;
				exit(0);
			}
			
			trip.start = start;
			trip.end = end;
			trip.from = 'b';
			
			trip_b.push_back(trip);
			
		}
	
		sort( trip_a.begin(), trip_a.end(), compare );
		sort( trip_b.begin(), trip_b.end(), compare );
		
//		for( vector<Trip>::iterator it = trip_a.begin(); it != trip_a.end(); it++ )
//			cout<<it->start<<" "<<it->end<<endl;		
//		for( vector<Trip>::iterator it = trip_b.begin(); it != trip_b.end(); it++ )
//			cout<<it->start<<" "<<it->end<<endl;
		
		while( !trip_a.empty() && !trip_b.empty() )
		{
			if ( find_start( trip_a, trip_b ) )
			{
				if ( !find_train( trains_a, trip_a[0].start ) )
					train_a_num++;
				insert_train( trains_b, trip_a[0].end + tr_time );
				trip_a.erase( trip_a.begin() );
			}
			else
			{
				if ( !find_train( trains_b, trip_b[0].start ) )
					train_b_num++;
				insert_train( trains_a, trip_b[0].end + tr_time );
				trip_b.erase( trip_b.begin() );
			}
		}
		if ( trip_a.empty() )
		{
			while( !trains_b.empty() && !trip_b.empty() )
			{
				if ( !find_train( trains_b, trip_b[0].start ) )
					train_b_num++;
				trip_b.erase( trip_b.begin() );
			}
			train_b_num += trip_b.size();
		}
		else
		{
			while( !trains_a.empty() && !trip_a.empty() )
			{
				if ( !find_train( trains_a, trip_a[0].start ) )
					train_a_num++;
				trip_a.erase( trip_a.begin() );
			}
			train_a_num += trip_a.size();
		}

		outfile<<"Case #"<<xnum+1<<": "<<train_a_num<<" "<<train_b_num<<endl;
		
		
	}	


}

