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


bool Divides( int t, int n )
{
	if( ((n/t)*t) == n )
		return true;
	if( ((t/n)*n) == t )
		return true;

	return false;
}

int Solve()
{
	int N = read_int();
	int L = read_int();
	int H = read_int();

	vector<int>		notes;
	for( int r = 0; r < N; ++r )
	{
		notes.push_back( read_int() );
	}

	for( int t = L; t <= H; ++t )
	{
		bool failed = false;
		for( int n = 0; n < N; ++n )
		{
			if( !Divides(t, notes[n]) )
			{
				failed = true;
				break;
			}
		}

		if( !failed )
			return t;
	}

	return 0;
}

int main(int argc, char* argv[])
{
	//freopen( "test.txt", "r", stdin );
	freopen( "C:\\Users\\Paul\\Downloads\\C-small-attempt0.in", "r", stdin );
	freopen( "C:\\Users\\Paul\\Downloads\\C-small-attempt0.out", "w", stdout );

	int num_tests = read_int();

	for( int i = 0; i < num_tests; ++ i )
	{
		printf( "Case #%d: ", i+1 );
		int res = Solve();
		if( res )
			printf( "%d\n", res );
		else
			printf( "NO\n" );
	}

	return 0;
}

