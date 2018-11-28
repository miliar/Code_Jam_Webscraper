
#include <iostream>
#include <fstream>
#include <queue>

using namespace std;


int test_round( ifstream& ifs, int round_num )
{
	int snapper_num, action_num, limit;
	bool on = false;

	ifs >> snapper_num >> action_num;

	limit = 1 << snapper_num;

	if ( (action_num+1) % limit == 0 )
		cout << "Case #" << round_num << ": ON" << endl;
	else
		cout << "Case #" << round_num << ": OFF" << endl;
	return 0;
}

int main ( int argc, char * argv[] )
{
	int round_num;
	int i;

	if ( argc != 2 )
	{
		cout << "Usage: gtest <filename>" << endl;
		return -1;
	}

	ifstream ifs( argv[1] );
	if (!ifs )
	{
		cout << "File does not exist" << endl;
		return( -1 );
	}

	ifs >> round_num;

	for ( i = 0; i < round_num; i++ )
	{
		if ( test_round( ifs, i+1 ) != 0 )
			return -1;
	}

	return( 0 );
}
