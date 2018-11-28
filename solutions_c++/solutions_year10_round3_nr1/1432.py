#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;


#define Point pair<int,int>

Point windowsPlaces[1000];



int CalcIntersections(Point wPlace1,Point wPlace2)
{
	//float slop1=abs(wPlace1.first-wPlace1.second);
	//float slop2=abs(wPlace2.first-wPlace2.second);
	//if(slop1==slop2)
	//	return 0;
	//else 
	{
		float dis1=wPlace1.first-wPlace2.first;
		float dis2=wPlace1.second-wPlace2.second;
		if((dis1>0&&dis2<0)||(dis1<0&&dis2>0))
			return 1;
		else
			return 0;
	}
}


int CalcMulIntersections(Point wPlaces[],int lineNumbers)
{
	
	if(lineNumbers==1)
		return 0;
	int intersections=0;
	for(int i=0;i<lineNumbers;i++)
		for(int j=0;j<lineNumbers;j++)
		{
			if(i!=j)
			{
				intersections+=CalcIntersections(wPlaces[i],wPlaces[j]);
			}

		}


		return intersections/2;
}




int main(int argc,char *argv[])
{

	
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


		getline(inStream,dataLine,'\n');
		int lineNumbers=atoi(dataLine.c_str());

		for(int j=0;j<lineNumbers;j++)
		{
			Point windowsplace;
			
			getline(inStream,dataLine,'\n');
			unsigned int pos=dataLine.find_first_of(' ');
			windowsplace.first=atoi(dataLine.substr(0,pos).c_str());
		    windowsplace.second=atoi(dataLine.substr(pos,dataLine.size()-pos).c_str());
			windowsPlaces[j]=windowsplace;
		}
		
		//CalcIntersections(windowsPlaces,lineNumbers)
		int intersections=CalcMulIntersections(windowsPlaces,lineNumbers);

		outStream<<"Case #"<<i+1<<": "<<intersections<<endl;

	}


	return 0;
}