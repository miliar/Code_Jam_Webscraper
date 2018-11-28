#include <iostream>
#include <fstream>
#include <string>
#define INPUT_STRING "welcome to code jam"

using namespace std;

int numTimesPresent(string searchSet, string searchString)
{
	if (searchSet.length() < searchString.length())
		return 0;
	if (searchString.length() == 0)
		return 1;
	int timesPresent = 0;
	//This limits us slightly; if we're searching for "w", we don't need to search all the way to the end, only up to 12ish chars from the end.
	for (int i = 0; i <= searchSet.length() - searchString.length(); i++)
	{
		if (searchSet[i] == searchString[0])
		{
			string newSubstr = searchSet.substr(i);
			string newSearch = searchString.substr(1);
			timesPresent += numTimesPresent(searchSet.substr(i), searchString.substr(1));
		}
	}
	return timesPresent;
}

string trimString(string inputString, string validValues)
{
	string trimmedString;
	for (int i = 0; i < inputString.length(); i++)
	{
		if (validValues.find(inputString[i]) != string::npos)
			trimmedString += inputString[i];
	}
	return trimmedString;
}

int main (int argc, char * const argv[]) {
	while(1)
	{
		char filename[100];
		cout << "Enter filename or q to quit: ";
		cin >> filename;
		if (strcmp(filename, "q") == 0)
			return 0;
		ifstream input (filename);
		if (!input.is_open())
		{
			cout << "Unable to open file\n";
			continue;
		}
		
		int numCases;
		input >> numCases;
		//finish off the newline.
		input.get();
		for (int i = 0; i < numCases; i++)
		{
			string currLine;
			getline(input, currLine);
			string trimmedString = trimString(currLine, INPUT_STRING);
			printf("Case #%d: %04d\n", i+1, numTimesPresent(trimmedString, INPUT_STRING)%10000);
		}
	}
    return 0;
}
