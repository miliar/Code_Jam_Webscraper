#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

char ConvertToEnglish(char _input);
int GetInt(std::string _string);

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
	std::vector<std::string*> output;

	for (int i = 0; i < numberOfLines; i++)
	{
		std::getline(inputFile, currentLine);
		
		std::string* inEnglish = new std::string();

		for (int c = 0; c < (signed int)currentLine.length(); c++)
		{
			*inEnglish += ConvertToEnglish(currentLine[c]);
		}

		output.push_back(inEnglish);
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
					": " << *output[i] << std::endl;
		outputFile << "Case #" << (i+1) <<
					": " << *output[i] << std::endl;
	}

	outputFile.close();

	while (!output.empty())
	{
		delete output[output.size() - 1];
		output.pop_back();
	}

	return 0;
}

char ConvertToEnglish(char _input)
{
	switch (_input)
	{
	case 'a': return 'y'; break;
	case 'b': return 'h'; break;
	case 'c': return 'e'; break;
	case 'd': return 's'; break;
	case 'e': return 'o'; break;
	case 'f': return 'c'; break;
	case 'g': return 'v'; break;
	case 'h': return 'x'; break;
	case 'i': return 'd'; break;
	case 'j': return 'u'; break;
	case 'k': return 'i'; break;
	case 'l': return 'g'; break;
	case 'm': return 'l'; break;
	case 'n': return 'b'; break;
	case 'o': return 'k'; break;
	case 'p': return 'r'; break;
	case 'q': return 'z'; break;
	case 'r': return 't'; break;
	case 's': return 'n'; break;
	case 't': return 'w'; break;
	case 'u': return 'j'; break;
	case 'v': return 'p'; break;
	case 'w': return 'f'; break;
	case 'x': return 'm'; break;
	case 'y': return 'a'; break;
	case 'z': return 'q'; break;
	default: return _input; break;
	}
}

int GetInt(std::string _string)
{
	int finalOutput = 0;
	std::stringstream sstream(_string);
	sstream >> finalOutput;
	return finalOutput;
}