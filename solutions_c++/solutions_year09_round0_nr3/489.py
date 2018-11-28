#include <iostream>
#include <iomanip>
#include <fstream>

#define NB_CHAR_PATTERN 19
//#define NB_CHAR_PATTERN 4

int main(int argc, char *argv[])
{
	std::ifstream inputFile(argv[1]);

	int numberCases = 0;
	inputFile >> numberCases;


	char pattern[] = "welcome to code jam";
	char buffer[512];
	inputFile.getline(buffer, 512);

	int dynamicArray[NB_CHAR_PATTERN][512];
	for (int indexCase = 1; indexCase <= numberCases; indexCase++)
	{
		inputFile.getline(buffer, 512);
		for (int i = 0; i < NB_CHAR_PATTERN; i++)
			for (int j = 0; j < 512; j++)
			dynamicArray[i][j] = 0;

		int nbCharStr = strlen(buffer);

		for (int iterPattern = NB_CHAR_PATTERN - 1; iterPattern >= 0; iterPattern--)
		{
			for (int iterString = nbCharStr - 1; iterString >= 0; iterString--)
			{
				if (iterPattern == NB_CHAR_PATTERN - 1)
				{
					dynamicArray[iterPattern][iterString] = dynamicArray[iterPattern][iterString + 1];
					if (pattern[iterPattern] == buffer[iterString])
						dynamicArray[iterPattern][iterString]++;
				}
				else
				{
					dynamicArray[iterPattern][iterString] = dynamicArray[iterPattern][iterString + 1];
					if (pattern[iterPattern] == buffer[iterString]) 
						dynamicArray[iterPattern][iterString] += dynamicArray[iterPattern + 1][iterString + 1]; 
				}
				dynamicArray[iterPattern][iterString] = dynamicArray[iterPattern][iterString] % 10000;
			}
		}

		int res = dynamicArray[0][0] % 10000;
		std::cout << "Case #" << indexCase << ": " << std::setfill('0') << std::setw(4) << res << std::endl;
	}
}