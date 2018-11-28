#include <fstream>
#include <math.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

std::ifstream in( "B-small.in" );
std::ofstream out( "B-small.out" );

struct time
{
	int first;
	int last;
	bool is_a;
	bool is_normal;
	time(){}
};

bool less( time & a, time & b )
{
	if( a.first == b.first )
	{
		return (a.last < b.last );
	}
	else return ( a.first < b.first );
}

bool check( std::vector<time> & arr )
{
	for( int i = 0; i != arr.size(); ++i )
		if( arr[i].is_normal ) return true;

	return false;
}

int main( void )
{
	int n = 0;
	in >> n;

	for(int i = 0; i != n; ++i)
	{
		int stop_time = 0;
		in >> stop_time;

		int way_a = 0, way_b = 0;
		in >> way_a >> way_b;
		
		std::vector<time> time_table(way_a+way_b);
		std::string temp;
		std::string temp2;
		std::getline( in, temp, '\n' );
		for( int j = 0; j != way_a; ++j )
		{
			std::getline( in, temp, '\n' );
			temp2 = temp.substr( 0, 2 );
			time_table[j].first = atoi( temp2.c_str() )*60;
			temp2 = temp.substr( 3, 2 );
			time_table[j].first += atoi( temp2.c_str() );
			temp2 = temp.substr( 6, 2 );
			time_table[j].last = atoi( temp2.c_str() )*60;
			temp2 = temp.substr( 9, 2 );
			time_table[j].last += atoi( temp2.c_str() );
			time_table[j].is_a = true;
			time_table[j].is_normal = true;
		}
		for( int j = 0; j != way_b; ++j )
		{
			std::getline( in, temp, '\n' );
			temp2 = temp.substr( 0, 2 );
			time_table[way_a+j].first = atoi( temp2.c_str() )*60;
			temp2 = temp.substr( 3, 2 );
			time_table[way_a+j].first += atoi( temp2.c_str() );
			temp2 = temp.substr( 6, 2 );
			time_table[way_a+j].last = atoi( temp2.c_str() )*60;
			temp2 = temp.substr( 9, 2 );
			time_table[way_a+j].last += atoi( temp2.c_str() );
			time_table[way_a+j].is_a = false;
			time_table[way_a+j].is_normal = true;
		}
		std::sort( time_table.begin(), time_table.end(), less );

		int count_a = 0, count_b = 0;

		while( check( time_table ) )
		{
			if( time_table[0].is_normal )
			{
				time_table.push_back( time() );
				time_table.back().is_normal = false;
				time_table.back().is_a = !time_table[0].is_a;
				if( time_table[0].is_a )count_a++;
				else count_b++;
				time_table.back().first = time_table[0].last + stop_time;
				time_table.erase( time_table.begin() );

			}
			else
			{
				int j = 1;
				while( (time_table.size() > j ) && ( time_table[0].is_a != time_table[j].is_a || !time_table[j].is_normal ) )
					j++;
				if( j < time_table.size() )
				{
					time_table.push_back( time() );
					time_table.back().is_normal = false;
					time_table.back().is_a = !time_table[0].is_a;
					time_table.back().first = time_table[j].last + stop_time;
					time_table.erase( time_table.begin()+j );
					time_table.erase( time_table.begin() );
				}
				else
					time_table.erase( time_table.begin() );

				
			}
			std::sort( time_table.begin(), time_table.end(), less );
		}

		out << "Case #" << i+1 << ": " << count_a << " " << count_b << "\n";

	}

	return 0;
}