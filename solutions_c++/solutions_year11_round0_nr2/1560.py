
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream inFile;
ofstream outFile;

char combines[26][26];
int opposes[26][26];


int
main()
{
	inFile.open("input.txt");
	outFile.open("output.txt");

	int num_cases;
	inFile >> num_cases;
	
	int tmp_num;
	string tmp_str;
	for (int curr_case = 0 ; curr_case < num_cases ; curr_case++)
	{
		memset(combines, 0, sizeof(combines));
		memset(opposes, 0, sizeof(opposes));

		inFile >> tmp_num;
		for (int i = 0 ; i < tmp_num ; i++)
		{
			inFile >> tmp_str;
			combines[tmp_str.at(0) - 'A'][tmp_str.at(1) - 'A'] = tmp_str.at(2);
			combines[tmp_str.at(1) - 'A'][tmp_str.at(0) - 'A'] = tmp_str.at(2);
		}
		inFile >> tmp_num;
		for (int i = 0 ; i < tmp_num ; i++)
		{
			inFile >> tmp_str;
			opposes[tmp_str.at(0) - 'A'][tmp_str.at(1) - 'A'] = 1;
			opposes[tmp_str.at(1) - 'A'][tmp_str.at(0) - 'A'] = 1;
		}
		inFile >> tmp_num;
		inFile >> tmp_str;
		
		string result = "";
		for (int i = 0 ; i < tmp_num ; i++)
		{
			if (result.length() == 0)
				result += tmp_str[i];
			else {
				if (combines[result[result.length() - 1] - 'A'][tmp_str[i] - 'A'] > 0)
				{
					char ac = combines[result[result.length() - 1] - 'A'][tmp_str[i] - 'A'];
					result.erase(result.end() - 1);
					result += ac;
				} else {
					result += tmp_str[i];
					for (int j = 0 ; j < result.length() ; j++)
					{
						if (opposes[result[j] - 'A'][tmp_str[i] - 'A'] > 0)
						{
							result.clear();
							break;
						}
					}
				}
			}
		}
		outFile << "Case #" << curr_case + 1 << ": [";
		if (result.length() > 0)
			outFile << result[0];
		for (int i = 1 ; i < result.length() ; i++)
		{
			outFile << ", " << result[i];
		}
		outFile << "]" << endl;
	}

	return 0;
}
