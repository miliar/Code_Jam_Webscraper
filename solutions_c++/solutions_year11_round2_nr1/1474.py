#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string>
#include <vector>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <map>

using std::cin;
using std::cout;
using std::string;
using std::vector;

typedef std::pair<int,int>	pi;

typedef unsigned __int64 u64;

int read_int() { int r; cin >> r; return r; }
string read_str() { string s; cin >> s; return s; }

double CalcWinPercent( int * matrix, int num_teams, int team_idx )
{
	int num_won = 0;
	int num_lost = 0;
	for( int x = 0; x < num_teams; ++x )
	{
		int r = matrix[team_idx*num_teams + x ];
		if( r < 0 )
			num_lost++;
		else if( r > 0 )
			num_won++;
	}
	return (double)num_won / (double)(num_won + num_lost);
}

double CalcOppWinPercent( int * matrix, int num_teams, int team_idx )
{
	double sum = 0.0;
	int opponents = 0;

	for( int t = 0; t < num_teams; ++t )
	{
		// Only include for teams that we played
		if( matrix[team_idx*num_teams + t] == 0 )
			continue;

		int num_won = 0;
		int num_lost = 0;
		for( int x = 0; x < num_teams; ++x )
		{
			// Ignore results against ourself
			if( x == team_idx )
				continue;

			int r = matrix[t*num_teams + x ];
			if( r < 0 )
				num_lost++;
			else if( r > 0 )
				num_won++;
		}

		sum += (double)num_won / (double)(num_won + num_lost);
		opponents ++;
	}

	return sum / (double)opponents;
}


double CalcOppOppWinPercent( int * matrix, double * owp_all, int num_teams, int team_idx )
{
	double sum = 0.0;
	int opponents = 0;

	for( int t = 0; t < num_teams; ++t )
	{
		// Only include for teams that we played
		if( matrix[team_idx*num_teams + t] == 0 )
			continue;

		sum += owp_all[t];
		opponents ++;
	}

	return sum / (double)opponents;
}


vector<double> Solve()
{
	int num_teams = read_int();

	int *	matrix = new int[ num_teams * num_teams ];

	for( int i = 0; i < num_teams; ++i )
	{
		string r = read_str();

		for( int x = 0; x < num_teams; ++x )
		{
			char result = r[x];
			int result_int = 0;
			if( result == '0' )
				result_int = -1;
			else if( result == '1' )
				result_int = +1;
			matrix[ i*num_teams + x ] = result_int;
		}
	}

	double * owp_all = new double[ num_teams ];
	for( int i = 0; i < num_teams; ++i )
	{
		owp_all[i] = CalcOppWinPercent( matrix, num_teams, i );
	}

	vector<double> result;
	result.resize(num_teams);

	for( int i = 0; i < num_teams; ++i )
	{
		double wp = CalcWinPercent( matrix, num_teams, i );
		double owp = owp_all[i];
		double oowp = CalcOppOppWinPercent( matrix, owp_all, num_teams, i );

		//int num_won = 0;
		//int num_lost = 0;
		//for( int x = 0; x < num_teams; ++x )
		//{
		//	int r = matrix[i *num_teams + x ];
		//	if( r < 0 )
		//		num_lost++;
		//	else if( r > 0 )
		//		num_won++;
		//	printf( "%s ", r < 0 ? "lose" : r > 0 ? "win " : "    ");
		//}

		double rpi = (0.25*wp) + (0.5*owp) + (0.25*oowp);


		//printf( "w:%d, l:%d, wp:%f, owp:%f, oowp:%f, rpi:%f\n",
		//	num_won, num_lost, wp, owp, oowp, rpi );

		result[i] = rpi;
	}

	delete [] owp_all;
	delete [] matrix;
	return result;
}

int main(int argc, char* argv[])
{
	//freopen( "test.txt", "r", stdin );
	freopen( "C:\\Users\\Paul\\Downloads\\A-large.in", "r", stdin );
	//freopen( "C:\\Users\\Paul\\Downloads\\A-large.out", "w", stdout );

	int num_tests = read_int();

	for( int i = 0; i < num_tests; ++ i )
	{
		vector<double> res = Solve();
		printf( "Case #%d:\n", i+1 );

		for( size_t r = 0; r < res.size(); ++r )
		printf( "%.15f\n", res[r] );
	}

	return 0;
}

