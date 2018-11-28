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
typedef __int64 s64;

u64 read_u64() { u64 r; cin >> r; return r; }
int read_int() { int r; cin >> r; return r; }
string read_str() { string s; cin >> s; return s; }

void PlaceDrive( vector<int> & pos, vector<bool> & has_drive, u64 t )
{
	vector<u64>		time_to_reach;
	time_to_reach.resize( pos.size() );

	u64 cur_time = 0;
	for( size_t i = 0; i < pos.size(); ++i )
	{
		time_to_reach[i] = cur_time;

		u64 time_to_cross = 2*pos[i];
		u64 slow_end_time = cur_time + time_to_cross;

		if( t < slow_end_time && has_drive[i] )
		{
			if( t <= cur_time )
			{
				// drive is active the whole time
				time_to_cross = pos[i];
			}
			else
			{
				// drive is active part of the time
				u64 time = t-cur_time;
				time_to_cross = time + (( time_to_cross - time ) / 2);	// Cover second leg twice as fast
			}
		}


		cur_time += time_to_cross;
	}

	u64 best_saving = 0;
	int best_idx = 0;
	for( int i = has_drive.size()-1; i >= 0; --i )
	{
		if( has_drive[i] )
			continue;

		u64 time_to_cross = 2*pos[i];
		if( t < time_to_reach[i]+time_to_cross )
		{
			if( t <= time_to_reach[i] )
			{
				// drive is active the whole time
				time_to_cross = pos[i];
			}
			else
			{
				// drive is active part of the time
				u64 time = t-time_to_reach[i];
				time_to_cross = time + (( time_to_cross - time ) / 2);	// Cover second leg twice as fast
			}
		}

		u64 saving = (2*pos[i]) - time_to_cross;
		if( saving > best_saving )
		{
			best_saving = saving;
			best_idx = i;
		}
	}

	has_drive[best_idx] = true;
}

u64 Solve()
{
	int L = read_int();
	u64 t = read_u64();
	int N = read_int();
	int C = read_int();

	vector<int> A;
	A.resize(C);
	for( int r = 0; r < C; ++r )
	{
		A[r] = read_int();
	}

	vector<int>		pos;
	pos.resize(N);
	vector<bool>	has_drive;
	has_drive.resize(N);
	for( int r = 0; r < N; ++r )
	{
		pos[r] = A[r%C];
		has_drive[r] = false;
	}

	for( int l = 0; l < L; ++l )
	{
		PlaceDrive( pos, has_drive, t );
	}

	//for( size_t n = 0; n < has_drive.size(); ++n )
	//{
	//	if( has_drive[n] )
	//		printf( "Drive at %d\n", n );
	//}

	u64 cur_time = 0;
	for( size_t i = 0; i < pos.size(); ++i )
	{
		u64 time_to_cross = 2*pos[i];
		u64 slow_end_time = cur_time + time_to_cross;

		if( t < slow_end_time && has_drive[i] )
		{
			if( t <= cur_time )
			{
				// drive is active the whole time
				time_to_cross = pos[i];
			}
			else
			{
				// drive is active part of the time
				u64 time = t-cur_time;
				time_to_cross = time + (( time_to_cross - time ) / 2);	// Cover second leg twice as fast
			}
		}

		cur_time += time_to_cross;
	}

	return cur_time;
}

int main(int argc, char* argv[])
{
	//freopen( "test.txt", "r", stdin );
	freopen( "C:\\Users\\Paul\\Downloads\\B-small-attempt3.in", "r", stdin );
	freopen( "C:\\Users\\Paul\\Downloads\\B-small-attempt3.out", "w", stdout );

	int num_tests = read_int();

	for( int i = 0; i < num_tests; ++ i )
	{
		printf( "Case #%d: ", i+1 );
		u64 res = Solve();
		printf( "%d\n", res );
	}

	return 0;
}

