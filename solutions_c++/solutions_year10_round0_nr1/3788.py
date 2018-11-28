#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
	int tCases=0,i=0;
	long numJumps;
	unsigned long int nSnaps;
	ifstream infile("c:/gjam/input.txt");
	ofstream  outfile("c:/gjam/output.txt",ios_base::out);
	infile>>tCases;
	int mod=0,nPlugs=0;
	int switchFlag =1;
	for(i=0;i<tCases;i++)
	{
		nPlugs=0;
		nSnaps =0;
		switchFlag =1;
		numJumps =0;
		infile>>nPlugs>>nSnaps;
		if(nPlugs > 1)
		{
		numJumps = (long)pow(2.0,nPlugs);
		nSnaps = nSnaps-numJumps+1;
		if(nSnaps < 0)
		{
			switchFlag=1;
		}
		else if(nSnaps == 0)
		{
			switchFlag =0;
		}
		else
		{
		mod=nSnaps%numJumps;
		switchFlag=mod;
		}
		}
		else if(nSnaps == 0)
		{
			switchFlag =1;
		}
		else
		{
			numJumps = nSnaps %2;
			if(numJumps == 1)
			{
				switchFlag = 0;
			}
		}
		
	
		
		if(switchFlag == 0 )
		{
			outfile<<"Case #"<<i+1<<": ON"<<endl;
		}
		else
		{
			outfile<<"Case #"<<i+1<<": OFF"<<endl;
		}
	
	}
	outfile.close();
	infile.close();
}
