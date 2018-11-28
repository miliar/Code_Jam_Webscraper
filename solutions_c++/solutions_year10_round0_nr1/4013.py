// 2010_Q1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>


using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	fstream input("c:\\1\\1.input.log", ios::in),
		output("c:\\1\\1.output.log", ios::out);

	unsigned int cases = 0;
	input >> cases;

	for( unsigned int i = 1; i <= cases; ++ i ) {
		unsigned int N = 0, K = 0;
		input >> N >> K;

		unsigned int mark = (1 << N) - 1;

		if ( ( K & mark ) == mark )
			output << "Case #" << i << ": ON\n";
		else
			output << "Case #" << i << ": OFF\n";
	}

	output.close();
	input.close();

	return 0;
}

