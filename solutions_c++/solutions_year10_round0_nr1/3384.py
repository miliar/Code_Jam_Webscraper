// Snapper Chain.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream input_file("1.txt");
	std::ofstream output_file("out.txt");

	size_t count_tests = 0;
	input_file >> count_tests;

	size_t N = 0, K = 0;
	size_t result = 0;
	for (size_t i = 0; i < count_tests; ++i)
	{
		input_file >> N >> K;
		
		size_t X = 0;
		for (size_t j = 0; j < N; ++j)
			X = 2*X + 1;

		result = (K+1) % (X+1);

		output_file << "Case #" << i+1 << ": ";
	
		(result == 0) ? output_file << "ON\n" : output_file << "OFF\n";
	}

	input_file.close();
	output_file.close();

	return 0;
}
