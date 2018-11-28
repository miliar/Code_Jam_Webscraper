// Tongues.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <map>
#include <iostream>
#include <fstream>
#include <string>
#include <boost/foreach.hpp>

typedef std::pair<const char, char> pair_t;

using namespace std;

class Translator
{
public:
	Translator()
		: checkList("abcdefghijklmnopqrstuvwxyz")
	{}

	void learn(string input, string output)
	{
		int i = 0;
		BOOST_FOREACH( char ch, input )
		{
			if (mapping.find(ch) == mapping.end())
			{
				mapping[ch] = output[i];
				ch = output[i];	
				
				//int pos = checkList.find(output[i]);
				//if (pos != string::npos)
				//	checkList = checkList.substr(0, pos) + checkList.substr(pos + 1, checkList.size()-1);
			}
			++i;
		}

		//if (checkList.size() == 1)
		//	cout << "one char is missing" << endl;
	}

	string translate(string input)
	{
		string result;
		int i = 0;
		BOOST_FOREACH( char ch, input )
		{
			if (mapping.find(ch) != mapping.end())
			{
				result += mapping[ch];
			}
			else
				result += input[i];

			++i;
		}
		return result;
	}

	int size()
	{
		return mapping.size();
	}

private:
	map<char, char> mapping;
	string checkList;
};

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream inputFile;
	inputFile.open("input.txt");

	std::ifstream outputFile;
	outputFile.open("output.txt");

	std::string inputLine;
	std::getline(inputFile, inputLine);
	int numOfTestCase = atoi(inputLine.c_str());

	Translator translator;
	std::string outputLine;
	for(int i = 1; i <= numOfTestCase; ++i)
	{
		std::getline(inputFile, inputLine);
		std::getline(outputFile, outputLine);

		translator.learn(inputLine, outputLine);
	};
	inputFile.close();
	outputFile.close();

	cout << "learning done!" << endl;
	cout << "mapping size = " << translator.size() << endl << endl;

	inputFile.clear();
	inputFile.open("A-small-attempt2.in");

	std::getline(inputFile, inputLine); 
	numOfTestCase = atoi(inputLine.c_str());

	ofstream resultFile;
	resultFile.open("small_output.txt");
	for(int i = 1; i <= numOfTestCase; ++i)
	{
		std::getline(inputFile, inputLine);
		cout << "Case #" << i << ": " << translator.translate(inputLine) << endl;
		resultFile << "Case #" << i << ": " << translator.translate(inputLine) << endl;
	};
	resultFile.close();

	return 0;
}

