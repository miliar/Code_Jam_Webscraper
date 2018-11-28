
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

using namespace std;

struct group_t
{
	int size;
	int next;
	int total;
};

struct euro_t
{
	long billion;
	long euro;
};

ostream& operator << ( ostream& os, struct euro_t euro )
{
	if ( euro.billion == 0 )
		os << euro.euro;
	else
	{
		os << euro.billion;
		os << setfill('0') << setw(9) << euro.euro;
	}
	return os;
}

int test_round( ifstream& ifs, int case_no )
{
	int round, capacity, group_num;
	vector<group_t> groups;
	struct group_t g0;
	int i, j, cur;
	struct euro_t euro;
	long billion = 1000000000L;

	ifs >> round >> capacity >> group_num;
	for ( i = 0; i < group_num; i++ )
	{
		ifs >> g0.size;
		g0.next = (i+1) % group_num;
		g0.total = g0.size;
		groups.push_back( g0 );
	}
	for ( i = 0; i < group_num; i++ )
	{
		j = (i+1) % group_num;
		while ( j != i )
		{
			if ( groups[i].total + groups[j].size > capacity )
				break;
			groups[i].total += groups[j].size;
			groups[i].next = (j+1) % group_num;
			j = (j+1) % group_num;
		}
	}

	cur = 0;
	euro.billion = 0;
	euro.euro = 0;
	for ( i = 0; i < round; i++ )
	{
		euro.euro += groups[cur].total;
		if ( euro.euro >= billion )
		{
			euro.billion += euro.euro / billion;
			euro.euro = euro.euro % billion;
		}

		cur = groups[cur].next;
	}

	cout << "Case #" << case_no << ": " << euro << endl;
	return( 0 );
}

int main ( int argc, char * argv[] )
{
	int case_num;
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

	ifs >> case_num;

	for ( i = 0; i < case_num; i++ )
	{
		if ( test_round( ifs, i+1 ) != 0 )
			return -1;
	}

	return( 0 );
}
