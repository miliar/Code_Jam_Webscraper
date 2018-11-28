#include <iostream>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <set>
#include <string>

void process(const std::string& line, int nbUC)
{
	std::istringstream iss (line, std::istringstream::in);
	int min, max;
	iss >> min;
	iss >> max;

//	std::cout << min << " " << max << std::endl;

	int nbPairs = 0;

	int curNum = min;
	while (curNum <= max) 
	{
		std::stringstream ss;
		ss << curNum;
		std::string newNum = ss.str();
		int dup = -1;
		for (int i = 0; i < (newNum.length()-1); ++i)
		{	

			char c = newNum[0];
			newNum = newNum.substr(1);
			newNum += c;
			
			int num = atoi(newNum.c_str());
			if (num != dup && num > curNum && num <= max)
			{
				++nbPairs;
				dup = num;
//				std::cout << curNum << "," << num << std::endl;
			}
		}

		curNum++;
	}

	std::stringstream ss;
	ss << "Case #" << nbUC << ": ";
	ss << nbPairs;

	std::cout << ss.str() << std::endl;
}

int main(int argc, char **argv)
{
	std::ifstream in(argv[1], std::ifstream::in);

	std::string line;
	std::getline(in, line);

	int nbUC = atoi(line.c_str());
	int curUC = 1;

	while (curUC <= nbUC)
	{
		std::getline(in, line);
		process(line, curUC);
		curUC++;
	}

	return 0;
}
