/* ****************************************
	universe.cpp - Greg Tourville - July 17th - Google Code Jam - Problem B
*/


#include <iostream>
#include <fstream>
#include <string>
#include <assert.h>

using namespace std;


int* v1;
int* v2;
int nDimensions;
int minScalarProduct;
int scalarProduct;


void permute(int *v, const int start, const int n)
{  
  if (start == n-1) {
			scalarProduct = 0;
			for (int j = 0; j < nDimensions; j++)
				scalarProduct += v[j] * v2[j];
			if (scalarProduct < minScalarProduct)
				minScalarProduct = scalarProduct;
  }
  else {
    for (int i = start; i < n; i++) {
      int tmp = v[i];
      
      v[i] = v[start];
      v[start] = tmp;
      permute(v, start+1, n);
      v[start] = v[i];
      v[i] = tmp;
    }
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
	for (int c = 1; c <= cases; c++)
	{
		minScalarProduct = 0;

		input >> nDimensions;

		v1 = new int[nDimensions];
		v2 = new int[nDimensions];

		for (int i = 0; i < nDimensions; i++)
			input >> v1[i];

		for (int i = 0; i < nDimensions; i++)
			input >> v2[i];


		for (int j = 0; j < nDimensions; j++)
			minScalarProduct += v1[j] * v2[j];


		/*
		for (int offs = 1; offs < nDimensions; offs++)
		{
			scalarProduct = 0;
			for (int j = 0; j < nDimensions; j++)
				scalarProduct += v1[(j+offs)%nDimensions] * v2[j];
			if (scalarProduct < minScalarProduct)
				minScalarProduct = scalarProduct;
		}*/

		permute(v1, 0, nDimensions);

		output << "Case #" << c << ": " << minScalarProduct << std::endl;

		// clean up
		delete[] v1;
		delete[] v2;
	}

	// Clean up
	input.close();
	output.close();

	return 0;
}


