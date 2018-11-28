/* ****************************************
	b.cpp - Greg Tourville - September 2nd - Google Code Jam - Problem B
*/


#include <iostream>
#include <fstream>
#include <assert.h>

const int NUM_DIRECTIONS = 4;
const int X_DIRECTIONS[NUM_DIRECTIONS]	=	{ 0, -1, 1,  0};
const int Y_DIRECTIONS[NUM_DIRECTIONS]	=	{-1,  0, 0,  1};

bool InRange(int x, int y, int width, int height)
{
	return (x >= 0 && y >= 0 && x < width && y < height);
}

bool IsSink(int** in, int x, int y, int width, int height)
{
	for (int k = 0; k < NUM_DIRECTIONS; k++)
	{
		int i = x + X_DIRECTIONS[k];
		int j = y + Y_DIRECTIONS[k];
		if (InRange(i, j, width, height))
		{
			if (in[j][i] < in[y][x])
			{
				return false;
			}
		}
	}
	return true;
}


char FindSink(int** in, char** result, int x, int y, int width, int height, char label)
{
	int lowest = -1;
	int idx = -1;

	for (int k = 0; k < NUM_DIRECTIONS; k++)
	{
		int i = x + X_DIRECTIONS[k];
		int j = y + Y_DIRECTIONS[k];
		if (InRange(i, j, width, height))
		{
			if (in[j][i] < lowest || lowest == -1)
			{
				lowest = in[j][i];
				idx = k;
			}
		}
	}

	if (lowest < in[y][x] && lowest != -1)
	{
		int i = x + X_DIRECTIONS[idx];
		int j = y + Y_DIRECTIONS[idx];

		if (!result[j][i])
			label = FindSink(in, result, i, j, width, height, label);
		result[y][x] = result[j][i];
		return label;
	} else {
		// sink
		result[y][x] = label;
		return label + 1;
	}
}

void LabelBasins(int** in, char** result, int width, int height)
{
	char label = 'a';

	// find sinks
	for (int y = 0; y < height; y++)
		for (int x = 0; x < width; x++)
		{
			result[y][x] = 0;
		}

	// find basins
	for (int y = 0; y < height; y++)
		for (int x = 0; x < width; x++)
		{
			if (!result[y][x])
				label = FindSink(in, result, x, y, width, height, label);
		}
}


// ****************************************************************************

int main(int argc, const char* argv[])	// Arguments to executed program should be 1) input file and 2) output file
{
	assert(argc == 3);

	std::ofstream output(argv[2]);
	std::ifstream input(argv[1], std::ifstream::in);

	assert(output.good());
	assert(input.good());
		

	// Process all cases
	int cases;
	input >> cases;

	for (int i = 1; i <= cases; i++)
	{	
		int width;
		int height;
		input >> height;
		input >> width;

		int** values = new int*[height];
		char** result = new char*[height];
		for (int y = 0; y < height; y++)
		{
			values[y] = new int[width];
			result[y] = new char[width];
			for (int x = 0; x < width; x++)
				input >> values[y][x];
		}

		
		// compute and output
		LabelBasins(values, result, width, height);
		
		output << "Case #" << i << ":" << std::endl;
		for (int y = 0; y < height; y++)
		{	
			for (int x = 0; x < width; x++)
			{
				output << result[y][x];
				if (x < width - 1)
					output << ' ';
				else
					output << std::endl;
			}

			delete[] result[y];
			delete[] values[y];
		}
		delete[] result;
		delete[] values;
	}

	// Clean up
	input.close();
	output.close();

	return 0;
}
