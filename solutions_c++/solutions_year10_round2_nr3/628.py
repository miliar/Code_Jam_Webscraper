
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

#include "longint.h"

using namespace std;

#define MAX_N 25

long_integer Comp[MAX_N+1][MAX_N+1];
std::vector<long_integer> Pool;

long_integer choose( int n, int c )
{
	long_integer res;
	long_integer x;

	if ( c == 0 )
	{
		res.clear();
		res._digit[MAX_DIGIT-1] = 1;
		return res;
	}

	res = Pool[n];
	x = Pool[c];
	res = res / x;

	x = Pool[n-c];
	res = res / x;

	return res;
}

long_integer pure ( int last, int size )
{
	int i;
	long_integer res;

	if ( size == 1 )
	{
		return Comp[1][1];
	}

	for ( i = 1; i <= size-1; i++ )
	{
		if ( size + (size-i) > last )
			continue;
		long_integer s = pure( size, i );
		long_integer t = Comp[last-size-1][size-i-1];
		long_integer w = s * t;
		res = res + w;
	}

	return res;
}

int test_round( ifstream& ifs, int case_no )
{
	int i, N;
	long_integer Num;
	long_integer mod;
	long_integer res;
	
	ifs >> N;

	mod.setint( 100003 );

	for ( i = 1; i <= N-1; i++ )
		Num = Num + pure( N, i );

	res = Num % mod;
	cout << "Case #" << case_no << ": " << res << endl;

	return( 0 );
}

int main ( int argc, char * argv[] )
{
	int case_num;
	int i, j;
	long_integer li;

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

	for ( i = 0; i < MAX_N+1; i++ )
		for ( j = 0; j < MAX_N+1; j++ )
			Comp[i][j].clear();

	for ( i = 0; i < MAX_N+1; i++ )
		Comp[i][0].setint(1);
	for ( i = 0; i < MAX_N+1; i++ )
		Comp[0][i].setint(1);
	for ( i = 0; i < MAX_N+1; i++ )
		Comp[i][i].setint(1);

	for ( i = 1; i < MAX_N+1; i++ )
		for ( j = 1; j < i; j++ )
			Comp[i][j] = Comp[i-1][j] + Comp[i-1][j-1];
		
	for ( i = 0; i < case_num; i++ )
	{
		if ( test_round( ifs, i+1 ) != 0 )
			return -1;
	}

	return( 0 );
}
