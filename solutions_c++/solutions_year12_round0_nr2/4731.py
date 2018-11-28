#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

void SpaceDelimiter(std::string _input, int _expectedCount, std::string _output[]);
void SpaceDelimiterInt(std::string _input, int _expectedCount, int _output[]);
int GetInt(std::string _string);
std::string GetString(int _int);
int CalculateCase(std::string _input, int _line);

int main (int argc, char* argv[])
{	
	std::ifstream inputFile;
	inputFile.open("input.in");

	if (!inputFile.is_open())
	{
		std::cout << "Cannot open input file!" << std::endl;
		return -1;
	}

	std::string currentLine;
	std::getline(inputFile, currentLine);

	// number of lines
	int numberOfLines = GetInt(currentLine);
	std::vector<int> output;

	for (int i = 0; i < numberOfLines; i++)
	{
		std::getline(inputFile, currentLine);
		
		output.push_back(CalculateCase(currentLine, i + 1));
	}	

	inputFile.close();

	std::ofstream outputFile;
	outputFile.open("output.out", std::ofstream::out);

	if (!outputFile.is_open())
	{
		std::cout << "Fail to open output file!" << std::endl;
		return -2;
	}

	for (int i = 0; i < numberOfLines; i++)
	{
		std::cout << "Case #" << (i+1) <<
					": " << output[i] << std::endl;
		outputFile << "Case #" << (i+1) <<
					": " << output[i] << std::endl;
	}

	outputFile.close();

	return 0;
}

void SpaceDelimiter(std::string _input, int _expectedCount, std::string _output[])
{
	int startIndex = 0;
	int substrLength = 0;

	for (int i = 0; i < _expectedCount; i++)
	{
		substrLength = _input.find_first_of(' ');

		if (substrLength == -1)
		{
			std::cout << "Expected " << _expectedCount << ", only obtained " << i << "!" << std::endl;
			return;
		}

		std::string substr = _input.substr(startIndex, substrLength - startIndex);
		_output[i] = substr;

		startIndex += substrLength + 1;
	}
}

void SpaceDelimiterInt(std::string _input, int _expectedCount, int _output[])
{
	int startIndex = 0;
	int endIndex = 0;

	for (int i = 0; i < _expectedCount; i++)
	{
		endIndex = _input.find_first_of(' ', startIndex);

		if (endIndex == -1)
		{
			if (startIndex >= (signed int)_input.length())
			{
				std::cout << "Expected " << _expectedCount << ", only obtained " << i << "!" << std::endl;
				return;
			}
			else
			{
				endIndex = _input.length();
			}
		}

		std::string substr = _input.substr(startIndex, endIndex - startIndex);
		_output[i] = GetInt(substr);

		startIndex = endIndex + 1;
	}
}

int GetInt(std::string _string)
{
	int finalOutput = 0;
	std::stringstream sstream(_string);
	sstream >> finalOutput;
	return finalOutput;
}

std::string GetString(int _int)
{
	std::stringstream sstream;
	sstream << _int;
	return sstream.str();
}

int CalculateCase(std::string _input, int _line)
{
	int output = 0;
	int spaceIndex = _input.find_first_of(' ');
	std::string totalGooglersSubStr = _input.substr(0, spaceIndex);
	int totalGooglers = GetInt(totalGooglersSubStr);

	int totalData = totalGooglers + 3;

	int* individualDatas = new int[totalData];

	SpaceDelimiterInt(_input, totalData, individualDatas);
	
	if (totalGooglers != individualDatas[0])
	{
		std::cout << "Error parsing input data for line " << _line << std::endl;
		delete[] individualDatas;
		return -1;
	}

	int totalSurprising = individualDatas[1];
	int bestResultOf = individualDatas[2];

	for (int g = 0; g < totalGooglers; g++)
	{
		int thisGooglerScore = individualDatas[3 + g];
		int average = thisGooglerScore / 3;

		if (average >= bestResultOf)
			output++;
		else if (average + 1 >= bestResultOf && ((average * 2 + (average + 1) == thisGooglerScore)
											|| (average + (average + 1) * 2 == thisGooglerScore)))
			output++;
		else if (totalSurprising > 0)
		{
			if (thisGooglerScore % 3 == 0)
			{
				if (average + 1 >= bestResultOf && thisGooglerScore > 0)
				{
					totalSurprising--;
					output++;
				}
			}
			else if (thisGooglerScore % 3 == 1)
			{
				if (average + 1 >= bestResultOf && thisGooglerScore > 0)
				{
					totalSurprising--;
					output++;
				}
			}
			else if (thisGooglerScore % 3 == 2)
			{
				if (average + 2 >= bestResultOf && thisGooglerScore > 0)
				{
					totalSurprising--;
					output++;
				}
			}
		}
	}

	delete[] individualDatas;

	return output;
}