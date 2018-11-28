
#include <fstream>
#include <string>
#include <cstring>
using namespace std;

#define FILENAME_IN "B-small-attempt0.in"
#define FILENAME_OUT "B-small-attempt0.out"

int* used_nums = new int[10];
int* current_nums = new int[10];

void Calculate( int number, int* array )
{
	while ( number )
	{
		++array[ number % 10 ];
		number = number / 10;
	}

	array[0] = 0;
}

bool Compare()
{
	// TODO: May be use memcmp
	for( int i = 0; i < 10; ++i )
	{
		if ( used_nums[i] != current_nums[i] )
		{
			return false;
		}
	}

	return true;
}

int main()
{
	ifstream fin( FILENAME_IN );
	if ( !fin )
	{
		return 1;
	}

	ofstream fout( FILENAME_OUT );
	if ( !fout )
	{
		return 1;
	}


	int T = 0;
	fin >> T;
	fin.ignore();

	for ( int i = 0; i < T; ++i )
	{
		int number = 0;

		fin >> number;
		fin.ignore();

		memset( used_nums, 0, sizeof(int) * 10 );

		Calculate( number, used_nums );

		do
		{
			memset( current_nums, 0, sizeof(int) * 10 );
			++number;
			//std::cout << number << std::endl;
			Calculate( number, current_nums );
		} while( !Compare() );

		fout << "Case #" << (i+1) << ": " << number << std::endl;
	}


	fout.close();
	fin.close();

	delete [] current_nums;
	delete [] used_nums;

	return 0;
}

