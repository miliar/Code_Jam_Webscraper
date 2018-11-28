//============================================================================
// Name        : Google-code-jam-qualification-round.cpp
// Author      : Kashif Munir
// Problem     : Problem B. Problem B. Dancing With the Googlers, Qualification round 2012
// Description : C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main()
{
	char buffer_string[10];

	ifstream infile("input.txt");
	ofstream outfile("output.txt");

	int number_of_lines = 0;
	infile >> number_of_lines;
	infile.getline(buffer_string,10,'\n');

	int case_num = 0;
	int Number_of_Googlers_N = 0;
	int Number_Surprising_triplets_S = 0;
	int best_result_of_at_least_p = 0;

	int googler_score = 0;
	int count = 0;

	while (number_of_lines > 0)
	{
		outfile << "Case #" << ++case_num << ": ";

		infile >> Number_of_Googlers_N;
		infile >> Number_Surprising_triplets_S;
		infile >> best_result_of_at_least_p;

		count = 0;
		for (int i=0; i < Number_of_Googlers_N ; i++)
		{
			infile >> googler_score;

			if (  (best_result_of_at_least_p * 3) <= (googler_score+2) )
				count++;
			else if ( (best_result_of_at_least_p * 3 <= googler_score+4 ) && (Number_Surprising_triplets_S > 0) )
			{
				if ( !(best_result_of_at_least_p == 1 && googler_score == 0) )
				{
					count++;
					Number_Surprising_triplets_S--;
				}
			}

		}

		outfile << count << endl;
		infile.getline(buffer_string,10,'\n');

		number_of_lines--;
	}

	outfile.close();

	return 0;
}
