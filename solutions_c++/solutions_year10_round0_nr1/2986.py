#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;


unsigned int OnLightCal(unsigned int snappers)
{
	if(snappers<=0)
	{
		cerr<<"Error!!!"<<endl;
		exit(-1);
	}
	if(snappers==1)
		return 1;
	else
		return (2*OnLightCal(snappers-1)+1);

}





int main(int argc,char *argv[])
{
	typedef pair<unsigned int,unsigned int> snapPair;

	vector<snapPair> snapPair_v;


	string inputFile,outputFile;
	ifstream inStream;
	ofstream outStream;

	unsigned int testSize;

	

	inputFile=string(argv[1]);
	outputFile=string(argv[2]);

	inStream.open(inputFile.c_str());
	outStream.open(outputFile.c_str());

	if(!inStream.is_open()||!outStream.is_open())
	{

		cerr<<"Stream Error!!!"<<endl;
	}


	string dataLine;

	getline(inStream,dataLine,'\n');
	testSize=atoi(dataLine.c_str());

	cerr<<"Test size is "<<testSize<<endl;


	for(int i=0;i<testSize;i++)
	{
		unsigned int snappers,snapTimes;

		getline(inStream,dataLine,'\n');

		unsigned int pos=dataLine.find_first_of(' ');
		snappers=atoi(dataLine.substr(0,pos).c_str());
		snapTimes=atoi(dataLine.substr(pos,dataLine.size()-pos).c_str());
		//snapPair_v.push_back(snapPair(snappers,snapTimes));
		unsigned int lightOnNeeds=OnLightCal(snappers);
		string status;
		if(snapTimes%(lightOnNeeds+1)==lightOnNeeds)
			status="ON";
		else
			status="OFF";
		outStream<<"Case #"<<i+1<<": "<<status<<endl;
	}



	

	

	//cerr<<"Size of int "<<sizeof(unsigned int)<<endl;

	return 0;
}
