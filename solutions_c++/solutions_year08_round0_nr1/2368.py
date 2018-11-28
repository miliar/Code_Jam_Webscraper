#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int bestResult;
int positionSolved;

int outputCase(char* file, int counter)
{
	ofstream fout;
	fout.open(file, ios::app);
	fout << "Case #" << counter << ": " << bestResult << endl;
	fout << flush;
	fout.close();
	return 0;
}

int giveIndex(char *palabra, char **eChar, int number)
{
	for(int i=0; i < number; i++)
	{
		if(strcmp(eChar[i], palabra) == 0)
			return i;
	}
	return -1;
}

bool foundInUsed(int *engines, int numberEngines, int search, int *used, int *numberUsed)
{
	cout << "used: ";
	for(int i = 0; i < numberEngines; i++)
		cout << used[i] << ", " ;
	cout << endl;	
	for(int i = 0; i < numberEngines ; i++)
	{
		if(used[i] == search)
		{
		    cout << "used found: " << used[i] << endl;
			return true;
		}
	}
	(*numberUsed)++;
	for(int i = 0; i < numberEngines ; i++)
	{
		if(used[i] == -1)
		{
			used[i] = search;
			break;
		}
	}
	return false;
}



int main()
{
	char inputFile[256], outputFile[256];
	int counter, numberRecords;
	char **enginesChar, **searchesChar;
	int numberEngines, numberSearches, numberUsed;
	int *engines, *searches, *used;
	string line = "";
	counter = 0;
	
	cout << "Starting program" << endl;
	
	strcpy(inputFile, "A-small.in");
	strcpy(outputFile, "A-small.out");
	remove(outputFile);
	
	//Load the input file:
	ifstream fileReader;
	fileReader.open(inputFile);
	if(!fileReader.is_open())
	{
		cout << "Input file not found! Exiting..." << endl;
		return -1;
	}
	cout << "Intput file opened..." << endl;
		
	fileReader.seekg(0);		//Pointer to the start of the file
	//Read the first line counter
	getline(fileReader, line);
	stringstream(line) >> numberRecords;
	cout << "Number of records: " << numberRecords << endl;

	//Loop to read the file
	while(!fileReader.eof() && counter < numberRecords)
	{
		//Read case
		line = "";
		counter++;
		getline(fileReader, line);
		stringstream(line) >> numberEngines;
		enginesChar = new char*[numberEngines];	
		engines     = new int[numberEngines];	
		used        = new int[numberEngines];
		numberUsed = 0;
		for(int i = 0; i < numberEngines; i++)
		{
			getline(fileReader, line);
			enginesChar[i] = new char[line.size()+1];
			strcpy (enginesChar[i], line.c_str());	
			engines[i] = i;
			used[i] = -1;
		}
		getline(fileReader, line);
		stringstream(line) >> numberSearches;

		searchesChar = new char*[numberSearches];
		searches     = new int[numberSearches];
		for(int i = 0; i < numberSearches; i++)
		{
			getline(fileReader, line);
			searchesChar[i] = new char[line.size()+1];
			strcpy (searchesChar[i], line.c_str());		
			searches[i] = giveIndex(searchesChar[i], enginesChar, numberEngines);
		}
		cout << "Number of engines: " << numberEngines << endl;
		for(int i = 0; i < numberEngines; i++)
			cout << engines[i] << ", " ;
		cout << endl << "Number of searches: " << numberSearches << endl;
		for(int i = 0; i < numberSearches; i++)
			cout << searches[i] << ", " ;
		cout << endl;
		
		//CalculateStep (This is the real algorithm)
		bestResult = 0;
		for(int i = 0; i < numberSearches; i++)
		{
			cout << "----------------Testing: " << searches[i] << endl;
			bool failed = foundInUsed(engines, numberEngines, searches[i], used, &numberUsed);
			if(numberUsed == numberEngines)
			{	
				//Switch!!
				cout << "switchhhhhhhhhhhhhhhhhhh" << endl;
				bestResult++;
				for(int j = 0; j < numberEngines; j++)
				{
					used[j] = -1;
				}
				numberUsed = 0;
				failed = foundInUsed(engines, numberEngines, searches[i], used, &numberUsed);
			}
			
		}
		
		//Print output
		cout << "Result: " << bestResult << endl;
		outputCase(outputFile, counter);
		
		//Delete arrays
		delete [] engines;
		delete [] searches;
		for(int i=0; i < numberEngines; i++)
			delete [] enginesChar[i];
		for(int i=0; i < numberSearches; i++)
			delete [] searchesChar[i];
		cout << "------------------------------------------" << endl;
	}
	
	//End of the program
	fileReader.close();
	cout << endl << endl << "Finished file with " << counter << " lines" << endl;
	cout << "Ending program" << endl;
	return 0;
}
