// test_A.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <iostream>
#include <fstream>


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in;
	in.open( "A-large.in" );

	std::fstream out;
	out.open( "A-large.out", std::ios_base::out );

	int N = 0;
	in >> N;

	for( int caseIndex = 0; caseIndex < N; ++caseIndex )
	{
		unsigned int S = 0;
		in >> S;

		unsigned int K = 0;
		in >> K;

		unsigned int clicks = (1 << S);
		unsigned int cc = K % clicks;
		
		out << "Case #" << caseIndex + 1 << ": ";
		if( cc + 1 == clicks )
			out << "ON";
		else
			out << "OFF";
		out << "\n";
		out.flush( );
	}

	out.flush( );
	out.close( );

	return 0;
}