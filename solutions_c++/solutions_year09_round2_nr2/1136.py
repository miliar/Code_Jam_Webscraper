/* ****************************************
	b.cpp - Greg Tourville - September 12th - Google Code Jam - Problem B
*/


#include <iostream>
#include <fstream>
#include <assert.h>

void Swap(char* n, int x, int y)
{
	char tmp = n[x];
	n[x] = n[y];
	n[y] = tmp;
}

void Insert(char* n, char value, int s, int e)
{
	for (int i = e; i > s; i--)
		n[i] = n[i-1];
	n[s] = value;
}

void Sort(char* n, int s, int e)
{
	char values[24];
	int size = 0;
	for (int i = s; i <= e; i++)
	{
		for (int j = 0; j <= size; j++)
			if (j == size || n[i] < values[j])
			{
				Insert(values, n[i], j, size);
				break;
			}
		size++;
	}


	for (int i = s; i <= e; i++)
		n[i] = values[i-s];
}


void FindNextLargest(char* num, int digits)	// num = "0XXX", digits = 3
{
	char largest = 0;
	for (int i = digits; i >= 0; i--)
	{
		if (num[i] < largest)
			for (int j = digits; j > i; j--)
			{
				if (num[i] < num[j])
				{
				Swap(num, i, j);
				Sort(num, i+1, digits);
				return;
				}
			}
		else
			largest = num[i];
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
		
	char nummmm[24];

	// Process all cases
	int cases;
	input >> cases;
	input.getline(&nummmm[1], 22, '\n');

	for (int k = 1; k <= cases; k++)
	{	
		char num[24];

		int digits;

		num[0] = '0';

		int i = 1;


		input.getline(&num[1], 22, '\n');
		/*while (num[i-1] != '\n')
		{
			input >> num[i];
			i++;
		}*/

		digits = strlen(num)-1;

		FindNextLargest(num, digits);

		if (num[0] == '0')
			output << "Case #" << k << ": " << &num[1] <<std::endl;
		else
			output << "Case #" << k << ": " << num <<std::endl;

	}

	// Clean up
	input.close();
	output.close();

	return 0;
}
