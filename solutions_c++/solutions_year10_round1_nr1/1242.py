
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

using namespace std;

int test_round( ifstream& ifs, int case_no )
{
	int n, k;
	int i, j, j2;
	char * table;
	char buf[51];
	char rmatch[51];
	char bmatch[51];
	bool rwin = false;
	bool bwin = false;

	ifs >> n;
	ifs >> k;

	table = (char *) malloc( n * n * sizeof(char) );
	if ( table == 0 )
	{
		cout << "there is no memory space" << endl;
		return( false );
	}

	// Rotate Read
	for ( i = 0; i < n; i++ )
	{
		string buf;
		ifs >> buf;

		for ( j = 0; j < n; j++ )
			table[(n-1-j)*n+(n-1-i)] = buf[j];
	}

	// Gravity
	for ( j = 0; j < n; j++ )
	{
		int bottom = 0;
		for ( i = 0; i < n; i++ )
		{
			if ( table[i*n+j] == '.' )
				continue;
			table[bottom*n+j] = table[i*n+j];
			bottom++;
		}
		for ( i = bottom; i < n; i++ )
			table[i*n+j] = '.';
	}
		
	// Create Match
	memset( rmatch, 'R', k );
	rmatch[k] = '\0';
	memset( bmatch, 'B', k );
	bmatch[k] = '\0';

#if 0
	for ( i = n-1; i >= 0; i-- )
	{
		for ( j = 0; j < n; j++ )
		{
			cout << table[i*n+j];
		}
		cout << endl;
	}
#endif

	// Check Horizontal
	for ( i = 0; i < n; i++ )
	{
		memset( buf, 0, sizeof(buf) );
		for ( j = 0; j < n; j++ )
			buf[j] = table[i*n+j];
		if ( strstr( buf, rmatch ) != 0 )
			rwin = true;
		if ( strstr( buf, bmatch ) != 0 )
			bwin = true;
	}

	// Check Vertical
	for ( j = 0; j < n; j++ )
	{
		memset( buf, 0, sizeof(buf) );
		for ( i = 0; i < n; i++ )
			buf[i] = table[i*n+j];
		if ( strstr( buf, rmatch ) != 0 )
			rwin = true;
		if ( strstr( buf, bmatch ) != 0 )
			bwin = true;
	}

	// Check Diagonal
	for ( i = 0; i < n; i++ )
	{
		memset( buf, 0, sizeof(buf) );
		for ( j = 0; j < n; j++ )
		{
			if ( i - j < 0 )
				break;
			buf[j] = table[(i-j)*n+j];
		}
		if ( strstr( buf, rmatch ) != 0 )
			rwin = true;
		if ( strstr( buf, bmatch ) != 0 )
			bwin = true;

		memset( buf, 0, sizeof(buf) );
		for ( j = n-1; j >= 0; j-- )
		{
			if ( i - (n-1-j) < 0 )
				break;
			buf[j] = table[(i-(n-1-j))*n+j];
		}
		if ( strstr( buf, rmatch ) != 0 )
			rwin = true;
		if ( strstr( buf, bmatch ) != 0 )
			bwin = true;
	}
	for ( i = 0; i < n; i++ )
	{
		memset( buf, 0, sizeof(buf) );
		for ( j = 0; j < n; j++ )
		{
			if ( i + j >= n )
				break;
			buf[j] = table[(i+j)*n+j];
		}
		if ( strstr( buf, rmatch ) != 0 )
			rwin = true;
		if ( strstr( buf, bmatch ) != 0 )
			bwin = true;

		memset( buf, 0, sizeof(buf) );
		for ( j = n-1; j >= 0; j-- )
		{
			if ( i + (n-1-j) >= n )
				break;
			buf[j] = table[(i+(n-1-j))*n+j];
		}
		if ( strstr( buf, rmatch ) != 0 )
			rwin = true;
		if ( strstr( buf, bmatch ) != 0 )
			bwin = true;
	}

	if ( rwin && bwin )
		cout << "Case #" << case_no << ": " << "Both" << endl;
	else if ( rwin )
		cout << "Case #" << case_no << ": " << "Red" << endl;
	else if ( bwin )
		cout << "Case #" << case_no << ": " << "Blue" << endl;
	else
		cout << "Case #" << case_no << ": " << "Neither" << endl;

	free( table );
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
