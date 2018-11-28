/*
 * main.cpp - Gaurav Baruah
 * for Saving the universe
 * 
 * */

#include <iostream>

#include "FileReader.h"
#include "SavingTheUniverse.h"

#define PI (22.0/7.0)

using namespace gb_codejam;

int main(int argc, char** argv)
{
	if(argc < 2) {
		std::cout<<"Pass input file name as argument";
		return 0;
	}
	FileReader *fileReader = FileReader::getFileReader();
	fileReader->SetInputFile(argv[1]);

	int numTestCases = fileReader->GetInteger();
	//std::cout<<numTestCases;
	for(int i = 0; i< numTestCases; i++)
	{
		int numSearchEngines = fileReader->GetInteger();
		//std::cout<<numSearchEngines;
		std::vector< std::string > searchEngines;
		for(int x = 0; x < numSearchEngines; x++) 
		{
			std::string engine = fileReader->GetLine();
			searchEngines.push_back(engine);
		}
		SavingTheUniverse centralServer(searchEngines);
		
		int numQueries = fileReader->GetInteger();
		//std::cout<<numQueries;
		for(int q = 0; q < numQueries; q++) 
		{
			std::string query = fileReader->GetLine();
			centralServer.NewQuery(query);
		}
		
		std::cout<<"Case #"<<(i+1)<<": "<<centralServer.GetNumSwitches();
		std::cout<<"\n";
	}
	fileReader->releaseFileReader();
	return 0;	
}
