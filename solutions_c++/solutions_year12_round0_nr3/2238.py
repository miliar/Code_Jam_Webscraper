#include <windows.h>
#include <shellapi.h>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <math.h>
#include <set>

int makeRecycled( long x, int l )
{
    int L = getLength10(x);
    int D = (long)pow(10.0, l);
    int M = (long)pow(10.0, L - l);
    return (long)(x / D) + (x % D) * M;
}


void solveC( )
{
	std::ifstream in;
	in.open( "C.in" );

	std::fstream out;
	out.open( "C.out", std::ios_base::out );

	int numCases = 0;
	in >> numCases;

	for( int caseIndex = 0; caseIndex < numCases; ++caseIndex )
	{
		long A = 0;
		in >> A;

		long B = 0;
		in >> B;

		std::set< std::pair< long, long > > pairs;

		for( long x = A; x <= B; ++x )
		{
			int L = getLength10(x);
			for( int l = 1; l < L; ++l )
			{
				int xr = makeRecycled(x, l);
				if( x < xr && xr >= A && xr <= B )
				{
					pairs.insert(std::make_pair(x, xr));
				}
			}
		}

		int R = pairs.size( );

		std::cout << "Case #" << caseIndex + 1 << ": Done" << std::endl;

		out << "Case #" << caseIndex + 1 << ": ";
		out << R;
		out << "\n";
		//out.flush( );
	}
}


int WINAPI WinMain( HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow )
{
	solveC( );
	return 0;
}