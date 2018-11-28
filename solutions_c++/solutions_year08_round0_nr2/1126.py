/*
 * main.cpp - Gaurav Baruah
 * for the always turn left problem
 * 
 * */

#include <iostream>

#include "DataConverter.h"
#include "FileReader.h"
#include "Station.h"

using namespace gb_codejam;

int getIntegerFromFile(FileReader *fileReader)
{
	std::string strTime = fileReader->GetWord();
	//std::cout<<strTime<<" ";
	//int ind = strTime.find(':'); // this is 2 always, using directly
	strTime.erase((strTime.begin() += 2));
	//std::cout<<strTime<<" ";
	return DataConverter::getInteger(strTime);
}

int main(int argc, char** argv)
{
	if(argc < 2) {
		std::cout<<"Pass input file name as argument";
		return 0;
	}
	FileReader *fileReader = FileReader::getFileReader();
	fileReader->SetInputFile(argv[1]);

	int numTestCases = fileReader->GetInteger();
	//std::cout<<"numTestCases = "<<numTestCases<<std::endl;
	for(int i = 0; i< numTestCases; i++)
	{
		int turnTime =  fileReader->GetInteger();
		int numATrips = fileReader->GetInteger();
		int numBTrips = fileReader->GetInteger();
		//std::cout<<turnTime<<numATrips<<numBTrips<<std::endl;
		Station A(turnTime);
		Station B(turnTime);
		for(int a = 0; a < numATrips; a++)
		{
			A.AddDeparture(getIntegerFromFile(fileReader));
			
			B.AddArrival(getIntegerFromFile(fileReader));
			//std::cout<<std::endl;
		}
		for(int b = 0; b < numBTrips; b++)
		{
			B.AddDeparture(getIntegerFromFile(fileReader));
			A.AddArrival(getIntegerFromFile(fileReader));
			//std::cout<<std::endl;
		}
		/*std::cout<<"Station A\n";
		A.GetNumTrainsRequired();
		std::cout<<"Station B\n";
		B.GetNumTrainsRequired();
		std::cout<<"reached here 3";
		getchar();*/
		std::cout<<"Case #"<<i+1<<": "<<A.GetNumTrainsRequired()<<" "<<B.GetNumTrainsRequired()<<std::endl;
	}
	fileReader->releaseFileReader();
	return 0;	
}
