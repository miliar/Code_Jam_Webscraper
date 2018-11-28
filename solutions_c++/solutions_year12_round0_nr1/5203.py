
#include <string>
#include <fstream>
#include <iostream>

std::string translate(std::string G)
{
	char cur = ' ';
	char tCur = ' ';
	std::string tG;

	for (int i = 0; i != G.size(); ++i)
	{
		cur = G.at(i);
		switch (cur)
		{
			case 'a':
				tCur = 'y';
				break;
			case 'b':
				tCur = 'h';
				break;
			case 'c':
				tCur = 'e';
				break;
			case 'd':
				tCur = 's';
				break;
			case 'e':
				tCur = 'o';
				break;
			case 'f':
				tCur = 'c';
				break;
			case 'g':
				tCur = 'v';
				break;
			case 'h':
				tCur = 'x';
				break;
			case 'i':
				tCur = 'd';
				break;
			case 'j':
				tCur = 'u';
				break;
			case 'k':
				tCur = 'i';
				break;
			case 'l':
				tCur = 'g';
				break;
			case 'm':
				tCur = 'l';
				break;
			case 'n':
				tCur = 'b';
				break;
			case 'o':
				tCur = 'k';
				break;
			case 'p':
				tCur = 'r';
				break;
			case 'q':
				tCur = 'z';
				break;
			case 'r':
				tCur = 't';
				break;
			case 's':
				tCur = 'n';
				break;
			case 't':
				tCur = 'w';
				break;
			case 'u':
				tCur = 'j';
				break;
			case 'v':
				tCur = 'p';
				break;
			case 'w':
				tCur = 'f';
				break;
			case 'x':
				tCur = 'm';
				break;
			case 'y':
				tCur = 'a';
				break;
			case 'z':
				tCur = 'q';
				break;
			default:
				tCur = ' ';
				break;
		}

		tG.push_back(tCur);
	}

	return tG;
}



int main ()
{
	std::string filename;
	std::string gIn;
	std::string trans;
	
	char cIn = 'x';

	int t, caseNum, gCount;

	std::ofstream outFile ("output.txt", std::ios::out);
	
	std::cout << "Input filename:  ";

	std::cin >> filename;

	std::ifstream inputFile (filename, std::ios::in);

	if (!inputFile)
	{
		std::cout << "Bad filename";
	}
	
	inputFile >> t;

	if ((t > 30) || (t < 1))
	{
		outFile << "BAD T, try again";
		std::cout << "BAD T, try again";
		return 1;
	}

	inputFile.get(cIn);
	inputFile.get(cIn);

	for (int i = 1; i <= t; ++i)
	{
		caseNum = i;
		gCount = 1;
		outFile << "\nCase #" << caseNum << ": ";
		
		while ((cIn != '\n') && !inputFile.eof())
		{
			gIn.push_back(cIn);
			inputFile.get(cIn);
			++gCount;
			if (gCount > 101)
			{
				cIn = '\n';
			}
		}

		trans = translate(gIn);
		outFile << trans;
		outFile << " ";		
		
		gIn.clear();
		if (!inputFile.eof())
		{
			inputFile.get(cIn);
		}
	}

	return 0;
}