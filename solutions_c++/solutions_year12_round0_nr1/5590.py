#include <iostream>
#include <fstream>
#include <map>
#include <string>

int main(int argc, const char* argv[])
{
	std::ifstream file(argv[1]);
	std::ofstream output("output.txt");
	char testcaseT[100];
	char currLine[100];

	std::string result = "";

	
	file.getline(currLine, 100);
	int testcases = std::atoi(currLine);
	

	for(int i = 0; i < testcases; ++i)
	{
		file.getline(currLine, 100);
		std::string resultLine = "";
		std ::cout << currLine << std::endl;
		for(int j = 0; j < std::strlen(currLine); ++j)
		{
			switch(currLine[j])
			{
			case 'a':
				resultLine += 'y';
				break;

			case 'b':
				resultLine += 'h';
				break;
			case 'c':
				resultLine += 'e';
				break;
			case 'd':
				resultLine += 's';
				break;

			case 'e':
				resultLine += 'o';
				break;
			case 'f':
				resultLine += 'c';
				break;

			case 'g':
				resultLine += 'v';
				break;
			case 'h':
				resultLine += 'x';
				break;

			case 'i':
				resultLine += 'd';
				break;
			case 'j':
				resultLine += 'u';
				break;

			case 'k':
				resultLine += 'i';
				break;
			case 'l':
				resultLine += 'g';
				break;

			case 'm':
				resultLine += 'l';
				break;
			case 'n':
				resultLine += 'b';
				break;

			case 'o':
				resultLine += 'k';
				break;
			case 'p':
				resultLine += 'r';
				break;

			case 'q':
				resultLine += 'z';
				break;
			case 'r':
				resultLine += 't';
				break;

			case 's':
				resultLine += 'n';
				break;
			case 't':
				resultLine += 'w';
				break;

			case 'u':
				resultLine += 'j';
				break;
			case 'v':
				resultLine += 'p';
				break;

			case 'w':
				resultLine += 'f';
				break;
			case 'x':
				resultLine +='m';
				break;

			case 'y':
				resultLine += 'a';
				break;
			case 'z':
				resultLine += 'q';
				break;
			case ' ':
				resultLine += ' ';
				break;
			case '\n': resultLine += '\n';
				break;
			default:

				break;
			}
		}

		output << "Case #" << i+1 << ": " << resultLine << std::endl;
		std::cout << "Case #" << (i+1) << ": " << resultLine << std::endl;
	}
	file.close();
	output.close();
	std::cin.get();
}