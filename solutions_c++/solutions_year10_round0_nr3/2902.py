#include <iostream>
#include <fstream>
#include <queue>
#include <string>
#include <assert.h>

using namespace std;

void ParseNumbers(vector<unsigned int> &numbers,const string &line)
{
	string::size_type pos=0,prev_pos=0;
	while((pos=line.find_first_of(' ',pos))!=string::npos)
	{
		unsigned int number=atoi(line.substr(prev_pos,pos-prev_pos).c_str());
		numbers.push_back(number);

		prev_pos=++pos;
	}

	numbers.push_back(atoi(line.substr(prev_pos,pos-prev_pos).c_str()));

}

unsigned long long int CalcRollerMoney(unsigned int runTimes,unsigned int pepoleContain,queue<unsigned int> groupQueue)
{
	unsigned long long int sumMoney=0;

	/*queue<unsigned int> gQueue=groupQueue;
	unsigned pepoleSum=0;
	while(!gQueue.empty())
	{
		pepoleSum+=gQueue.front();
		gQueue.pop();
	}*/
	for(unsigned int i=0;i<runTimes;i++)
	{
		unsigned int rollerContain=0;
		unsigned int visited=0;
		unsigned int singleSum=0;
		while(rollerContain<pepoleContain)
		{
			if(visited==groupQueue.size())
				break;
			unsigned int size=groupQueue.front();
			rollerContain+=size;
			//singleSum+=size;
			if(rollerContain>pepoleContain)
				break;
			sumMoney+=size;
			if(groupQueue.size()>1)
			{
			groupQueue.pop();
			groupQueue.push(size);
			visited++;
			}
			else
				break;
		}
		//assert(singleSum<=pepoleSum);

	}


	return sumMoney;

}





int main(int argc,char *argv[])
{
	string inputFile,outputFile;
	ifstream inStream;
	ofstream outStream;

	unsigned int testSize;

	
	if(argc<2)
	{
		cerr<<"Parameters are not enought!!! Format is : Roller input output"<<endl;
		exit(-1);
	}

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
		queue<unsigned int> groupQueue;
		unsigned int runTimes,pepoleContain,groupNum;
		vector<unsigned int> numbers_v;

		getline(inStream,dataLine,'\n');
		ParseNumbers(numbers_v,dataLine);
		
		assert(numbers_v.size()>=3);

		runTimes=numbers_v[0];
		pepoleContain=numbers_v[1];
		groupNum=numbers_v[2];

		numbers_v.clear();

		getline(inStream,dataLine,'\n');
		ParseNumbers(numbers_v,dataLine);
		for(int j=0;j<numbers_v.size();j++)
			groupQueue.push(numbers_v[j]);

		assert(groupQueue.size()==groupNum);

		unsigned long long int totalMoney=CalcRollerMoney(runTimes,pepoleContain,groupQueue);
		
		
		outStream<<"Case #"<<i+1<<": "<<totalMoney<<endl;


	}




	return 0;
}
