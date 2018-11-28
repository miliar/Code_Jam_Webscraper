// GCQ.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int main(int argc, char* argv[])
{
	freopen( "input.txt", "rt", stdin );
	freopen( "output.txt", "wt", stdout );

	int T = 0;
	cin >> T;

	for( int ct = 0; ct < T; ++ct )
	{
		vector< char > vSequence;
		vector< int > vBlue;
		vector< int > vOrange;
		int N = 0;
		cin >> N;

		for( int i = 0; i < N; ++i )
		{
			char r;
			int b;
			cin >> r >> b;
		
			vSequence.push_back( r );

			if( 'O' == r )
			{
				vOrange.push_back( b );
			}
			else
			{
				vBlue.push_back( b );
			}
		}

		reverse( vOrange.begin( ), vOrange.end( ) );
		reverse( vBlue.begin( ), vBlue.end( ) );

		int curPosOrange = 1;
		int curPosBlue = 1;
		int timeOrange = 0;
		int timeBlue = 0;
		int time = 0;

		for( int i = 0; i < N; ++i )
		{
			if( 0 < vOrange.size( )  )
			{
				timeOrange += abs( curPosOrange - vOrange.back( ) );
				curPosOrange = vOrange.back( );
			}
			if ( 0 < vBlue.size( ) )
			{
				timeBlue += abs( curPosBlue - vBlue.back( ) );
				curPosBlue = vBlue.back( );
			}

			if( vSequence[ i ] == 'O' )
			{
				++timeOrange;
				time = timeOrange;
				timeBlue = max( time, timeBlue );
				vOrange.pop_back( );
			}
			else
			{
				++timeBlue;
				time = timeBlue;
				timeOrange = max( time, timeOrange );
				vBlue.pop_back( );
			}
		}

		cout << "Case #" << ct + 1 << ": " << time << endl;
	}

	return 0;
}

