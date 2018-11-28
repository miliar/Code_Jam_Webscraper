#include <iostream>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <map>
#include <string>

static std::map<char, char> map;

void process(const std::string& line, int nbUC)
{
	std::istringstream iss (line, std::istringstream::in);
	int num, nbSurprising, minGrade;
	iss >> num;
	iss >> nbSurprising;
	iss >> minGrade;
	
	int sub = (minGrade == 0 ? 0 : (minGrade - 1));
	int minNormal = minGrade + sub + sub;
	
	sub = (sub == 0 ? 0 : (sub - 1));
	int minSurprising = minGrade + sub + sub;

	int curNbElem = 1;
	int val = 0;
	int numNormal = 0;
	int numSurprising = 0;
	while (curNbElem <= num) 
	{
		iss >> val;
		if (val >= minNormal)
			numNormal++;
		else if (val >= minSurprising)
			numSurprising++;

		++curNbElem;
	}

	if (numSurprising > nbSurprising)
		numNormal += nbSurprising;
	else
		numNormal += numSurprising;

	std::stringstream ss;
	ss << "Case #" << nbUC << ": ";
	ss << numNormal;

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
