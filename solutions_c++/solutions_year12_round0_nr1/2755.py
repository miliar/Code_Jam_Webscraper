//============================================================================
// Name        : Google-code-jam-qualification-round.cpp
// Author      : Kashif Munir
// Problem     : Problem A. Speaking in Tongues, Qualification round 2012
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
	char mapping[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

	char buffer_string[110];

	ifstream infile("input.txt");
	ofstream outfile("output.txt");

	int number_of_strings = 0;
	infile >> number_of_strings;
	infile.getline(buffer_string,110,'\n');

	int case_num = 0;
	while (number_of_strings > 0)
	{
		outfile << "Case #" << ++case_num << ": ";
		infile.getline(buffer_string,110,'\n');
		int i = 0;
		while ( (buffer_string[i] >= 65 && buffer_string[i] <= 90) || (buffer_string[i] >= 97 && buffer_string[i] <= 122) || (buffer_string[i] == ' ') )
		{
			if (buffer_string[i] >= 65 && buffer_string[i] <= 90)
				outfile << mapping[ buffer_string[i]-65 ];
			else if  (buffer_string[i] >= 97 && buffer_string[i] <= 122)
				outfile << mapping[ buffer_string[i]-97 ];
			else
				outfile << buffer_string[i];
			i++;
		}
		outfile << endl;

		number_of_strings--;
	}

	outfile.close();

	return 0;
}
