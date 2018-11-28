// DancingWithGooglers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <assert.h>

using namespace std;

vector<int> total_points;

void next_num ( const char*& buf )
{
	while (*buf && *buf != ' ')
		buf++;
	buf++;
}

int process_points ( const vector<int>& total_points, const int S, const int p )
{
	const int good_thrld = __max(3*p-2,0); // can be not surprising
	const int tentative_thrld = __max(3*p-4,0); // all surprising

	int n_good = 0;
	int n_tentative = 0;
	for ( size_t i = 0; i < total_points.size(); i++ )
	{
		const int val = total_points [i];
		if ( val == 0 && p != 0)
			continue;
		else if ( val >= good_thrld )
			n_good++;
		else if ( val >= tentative_thrld )
			n_tentative++;
	}

	n_tentative = __min(n_tentative,S);
	return n_good + n_tentative;
}

int get_result ( const char* const line )
{
	const char* buf = line;
	
	const int N = atoi (buf);
	next_num (buf);
	total_points.resize (N);

	const int S = atoi (buf);
	next_num (buf);

	const int p = atoi (buf);
	next_num (buf);

	for ( int i = 0; i < N; i++ )
	{
		total_points [i] = atoi (buf);
		next_num (buf);
	}
	buf = 0;

	return process_points ( total_points, S, p );
}

int _tmain(int argc, _TCHAR* argv[])
{
	string line;
	ifstream myfile ("c:\\temp\\g\\QR\\B-large.in");

	if (myfile.is_open())
	{
		if ( !myfile.good() )
			throw "Invalid input format";

		int N = 0; // the number of cases
		getline (myfile,line);
		N = atoi ( line.data() );
		for ( int n_case = 0; n_case < N; n_case++ )
		{
			getline (myfile,line);
			cout << "Case #" << n_case+1 << ": ";
			cout << get_result ( (char*)line.data() ) << endl;
		}
	}

	getchar();
	return 0;
}

