

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <map>
#include <vector>


int find( std::vector< std::string >& vec, std::string str )
{

	for( int i = 0; i < (int) vec.size(); i++ )
	{
		if( vec[i] == str ) return i;
	}
	return 0;
}

void resetarray( int arr[], int num_indices )
{
	for( int i = 0; i < num_indices; i++ )
	{
		arr[i] = 0;
	}
}

bool lastitem( int arr[], int num_indices, int index, int ignore_index = -1 )
{
	bool last = (arr[index]>0?false:true);
	for( int i = 0; i < num_indices; i++ )
	{
		if( (ignore_index == -1 || i != ignore_index ) && i != index && arr[i] == 0 )
		{
			if( last ) return false;
		}
	}
	return last;
}

void printarray( int arr[], int num_indices )
{
	for( int i = 0; i < num_indices; i++ )
	{
		std::cout << arr[i] << " ";
	}
	std::cout << std::endl;
}

int main( int argc, char* argv[] )
{
	std::string filename;
	if( argc == 0 ) return 1;
	std::ifstream file( argv[1] );
	if( !file.is_open() ) return 1;
	
	int num = 0;
	std::string str;
	std::istringstream iss;

	std::getline( file, str );
	iss.str( str );

	iss >> num;

	int n  = num;
	for( int n = 0; n < num; n++ )
	{
		int switches = 0;

		int ns = 0;
		std::getline( file, str );
		iss.str( str );
		iss.clear();
		iss >> ns;

		std::vector< std::string > engines;
		int * queries = new int[ ns ];

		for( int s = 0; s < ns; s++ )
		{
			std::getline( file, str );
			engines.push_back( str );
		}

		int nq = 0;
		std::getline( file, str );
		iss.str( str );
		iss.clear();
		iss >> nq;

		resetarray( queries, ns );
		int lastswitch = -1;
		for( int q = 0; q < nq; q++ )
		{
			std::getline( file, str );
			int qy = find( engines, str );
//			printarray( queries, ns );
			if( lastitem( queries, ns, qy, lastswitch ) )
			{
				lastswitch = qy;
				resetarray( queries, ns );
				switches++;
			}
			else queries[qy]++;
		}

		delete[] queries;
		std::cout << "Case #" << (n+1) << ": " << switches << std::endl;
	}
	
	return 0;
}