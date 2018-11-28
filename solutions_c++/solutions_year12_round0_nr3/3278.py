#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <math.h>
using namespace std;


int numberofTestCases;

struct TestCase
{
	int minNumber;
	int maxNumber;
};

void readFromFile(ifstream &inp,TestCase** testCases)
{
	inp>>numberofTestCases;
	*testCases=new TestCase[numberofTestCases];
	for(int i=0;i<numberofTestCases;i++)
	{
		inp>>(*testCases)[i].minNumber;
		inp>>(*testCases)[i].maxNumber;
	}

}

void main()
{	
	ifstream inp("C-small-attempt0.in");
	ofstream outp("output.txt");
	TestCase* testCases=new TestCase;
	readFromFile(inp,&testCases);
	int neededCount=0;
	bool* matched;
	for(int i=0;i<numberofTestCases;i++)
	{
		int temp1,temp2;
		neededCount=0;
		matched=new bool[testCases[i].maxNumber+1];
		for(int c=0;c<testCases[i].maxNumber+1;c++)
			matched[c]=false;
		int numberOfDigits=0;
		int tempx=testCases[i].minNumber;
		while(tempx!=0)
		{
			tempx/=10;
			numberOfDigits++;
		}
		for(int i1=testCases[i].minNumber;i1<=testCases[i].maxNumber-1;i1++)
		{
			//if(matched[i1])
				//continue;
			for(int i2=i1+1;i2<=testCases[i].maxNumber;i2++)
			{
				//if(matched[i2])
					//continue;
				int n=1;
				int m;
				int initialTemp1=i1;int initialTemp2=i2;
				temp1=i1;temp2=i2;
				while(temp1!=temp2 )
				{
					int part1=temp2/10;
					int part2=(temp2%10)*pow((double)10,numberOfDigits-1);
					temp2=part1+part2;
					if(temp2==initialTemp2)
						break;
				}
				/*if(temp2!=initialTemp2)
				{
					temp2=floor(initialTemp2/(pow((double)10,m)))*pow((double)10,m-1);
					temp2+=initialTemp2%(int)(pow((double)10,m-1));
					initialTemp2=temp2;
				}
				else 
					break;*/
				if(temp1==temp2)
				{
					//if(!matched[i1])
						neededCount++;
					matched[i1]=true;
					matched[i2]=true;
					i1;
					i2;
				}
			}
		}
			outp<<"Case #"<<i+1<<": "<<neededCount<<endl;
	}
}