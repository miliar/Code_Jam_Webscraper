//============================================================================
// Name        : Google-code-jam-qualification-round.cpp
// Author      : Kashif Munir
// Problem     : Problem C. Recycled Numbers, Qualification round 2012
// Description : C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
	char buffer_string[10];

	ifstream infile("input.txt");
	ofstream outfile("output.txt");

	int number_of_lines = 0;
	infile >> number_of_lines;
	infile.getline(buffer_string,110,'\n');

	int case_num = 0;
	int A = 0;
	int B = 0;

	int temp = 0;

	while (number_of_lines > 0)
	{
		outfile << "Case #" << ++case_num << ": ";

		int number_of_pairs = 0;

		infile >> A;
		infile >> B;
		infile.getline(buffer_string,10,'\n');

		int digits = 1;
		for (int i = A; i < B; i++)
		{
			// count digits of i
			int copy_i = i;
			digits = 1;
			while (copy_i / 10 != 0)
			{
				digits++;
				copy_i = copy_i / 10;
			}

			if (digits == 2)
			{
				temp = ((i % 10) * 10) + (i / 10);

				if ( (temp > i+1) && (temp <= B) )
					number_of_pairs++;
			}

			if (digits == 3)
			{
				temp = ((i % 10) * 100) + (i / 10);
				if ( (temp > i+1) && (temp <= B) )
					number_of_pairs++;

				temp = ((i % 100) * 10) + (i / 100);
				if ( (temp > i+1) && (temp <= B) )
					number_of_pairs++;
			}

		}

		outfile << number_of_pairs << endl;

		number_of_lines--;
	}

	outfile.close();

	return 0;
}
