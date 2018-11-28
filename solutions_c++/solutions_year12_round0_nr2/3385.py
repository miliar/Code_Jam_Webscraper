#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

int main(int argc, char** argv)
{
	std::string line;
	std::ifstream inputFile ("B-small-attempt0.in");
	std::ofstream outputFile ("output.txt");
	int no_of_cases = 0;
	int no_of_googlers = 0;
	int no_of_surprises = 0;
	int exp_score = 0;
	int total_score = 0;
	int without_surprise = 0;
	int with_surprise = 0;
	std::string temp_string = "";
	int judges_score[3];
	int some_temp = 0;
	if (inputFile.is_open())
	{
		// this line gives us the number of test cases
		getline (inputFile,line);
		no_of_cases = atoi(line.c_str());

		for (int counter = 1; counter <= no_of_cases; counter++)
		{
			// read line by line
			getline (inputFile,line);
			std::istringstream iss(line);
			
			// get number of googlers
			iss >> temp_string;
			no_of_googlers = atoi(temp_string.c_str());
			
			// get number of surprises
			iss >> temp_string;
			no_of_surprises = atoi(temp_string.c_str());

			// get expected score
			iss >> temp_string;
			exp_score = atoi(temp_string.c_str());
			
			without_surprise = 0;
			with_surprise = 0;
			// loop to get the various scores and store it in array
			for (int i = 0; i < no_of_googlers; i++)
			{
				iss >> temp_string;
				// read total score
				total_score = atoi(temp_string.c_str());
				
				// get set of judges score. 
				judges_score[0] = total_score / 3;
				judges_score[1] = (total_score - judges_score[0]) / 2;
				judges_score[2] = total_score - judges_score[0] - judges_score[1];

				// sort the judges score
				for (int k = 0;k<3;k++)
				{
					for (int l = k+1; l<3;l++)
					{
						if (judges_score [k] > judges_score [l])
						{
							some_temp = judges_score [k];
							judges_score [k] = judges_score [l];
							judges_score [l] = some_temp;
						}
					}
				}

				if (judges_score [2] >= exp_score)
					without_surprise ++;
				else if (judges_score [2] == (exp_score-1) && (total_score - judges_score [2] > 0) && (judges_score[1] == judges_score[2]))
					with_surprise ++;

			}
			if (with_surprise > no_of_surprises)
				with_surprise = no_of_surprises;
			outputFile <<"Case #"<<counter<<": "<<(without_surprise + with_surprise)<<std::endl;
		}
		inputFile.close();
		outputFile.close();
	}
	else 
		std::cout << "Unable to open file"; 
	return 0;
}