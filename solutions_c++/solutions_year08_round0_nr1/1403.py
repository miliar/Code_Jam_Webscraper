// SavingTheUniverse.cpp : Defines the entry point for the console application.
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

struct SearchEngine{
	char name[101];
	bool isExist;
	SearchEngine* nextEngine;
};

int readNextField(ifstream& input, char* field)
{
	if(input.eof())
		return 0;

	char temp;
	int index = 0;

	input.read(&temp, 1);
	while(!input.eof() && temp != '\n'){		
		field[index] = temp;
		index++;
		input.read(&temp, 1);
	}
	return index;
}

int skipNextField(ifstream& input)
{
	if(input.eof())
		return 0;

	char temp;
	int index = 0;

	input.read(&temp, 1);
	while(!input.eof() && temp != '\n'){		
		index++;
		input.read(&temp, 1);
	}
	return index;
}

int main()
{
	ifstream inputFile("A-large.in", ios::in);

	if(!inputFile)
	{
		cerr<<"File could not be opened"<<endl;
		exit(1);
	}

	//system("pause");
	//read number of cases
	int numberOfCase;
	inputFile>>numberOfCase;

	
	for(int i=1;i<=numberOfCase;i++)
	{
		//read number of search engines
		int numberOfSearchEng;
		inputFile>>numberOfSearchEng;
		SearchEngine* searchEngHead = NULL;

		//read the names of the search engines
		skipNextField(inputFile);
		int bytesread = 0;
		for(int j=0;j<numberOfSearchEng;j++)
		{
			SearchEngine* searchEng = new SearchEngine();
			bytesread = readNextField(inputFile, searchEng->name);
			searchEng->name[bytesread] = 0;
			searchEng->isExist = false;

			//sort the search engine in increasing order
			SearchEngine* temp = searchEngHead;
			SearchEngine* prev = NULL;
			if(temp != NULL)
			{
				while(strcmp(searchEng->name, temp->name) > 0)
				{
					prev = temp;
					if(temp->nextEngine != NULL)
						temp = temp->nextEngine;
					else
					{
						temp = NULL;
						break;
					}
				}
				if(prev == NULL)
				{
					searchEng->nextEngine = searchEngHead;
					searchEngHead = searchEng;
				}
				else
				{
					searchEng->nextEngine = temp;
					prev->nextEngine = searchEng;
				}
			}
			else
			{
				searchEng->nextEngine = NULL;
				searchEngHead = searchEng;				
			}
		}
		//system("pause");

		//read number of queries
		int numberOfQuery;
		inputFile>>numberOfQuery;
		//system("pause");

		skipNextField(inputFile);
		int numberOfSwitch = 0;
		int numberOfEngInQuery = 0;
		char query[101];
		SearchEngine* temp1 = NULL;
		//system("pause");
		for(int k=0;k<numberOfQuery;k++)
		{
			bytesread = readNextField(inputFile, query);
			query[bytesread] = 0;
			//system("pause");

			temp1 = searchEngHead;
			while(temp1!=NULL)
			{
				if(strcmp(query, temp1->name) == 0)
				{
					if(!temp1->isExist)
					{
						temp1->isExist = true;
						numberOfEngInQuery++;
					}
					break;
				}
				temp1 = temp1->nextEngine;
			}

			//need to switch
			if(numberOfEngInQuery >= numberOfSearchEng)
			{
				numberOfSwitch++;
				numberOfEngInQuery = 1;
				SearchEngine* temp2 = searchEngHead;
				while(temp2 != NULL)
				{
					if(temp2 != temp1)
						temp2->isExist = false;
					temp2 = temp2->nextEngine;
				}
			}
		}

		cout<<"Case #"<<i<<": "<<numberOfSwitch<<endl;
		SearchEngine* deleteTemp = searchEngHead;
		SearchEngine* deleteNext = NULL;
		while(deleteTemp!=NULL)
		{
			deleteNext = deleteTemp->nextEngine;
			delete deleteTemp;
			deleteTemp = deleteNext;
		}
		searchEngHead = NULL;
	}

	system("pause");
	return 0;
}
