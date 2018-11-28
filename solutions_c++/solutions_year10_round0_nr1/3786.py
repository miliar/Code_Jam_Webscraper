#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
	int numCases=0,i=0;
	long onPos;
	unsigned long int numSnaps;
	ifstream infile("c:/myfile.txt");
	ofstream  outfile("c:/resfilesnap.txt",ios_base::out);
	cout<<"Reading from file"<<endl;
	infile>>numCases;
	int mod=0,numBits=0;
	int onFlag =1;
	for(i=0;i<numCases;i++)
	{
		numBits=0;
		numSnaps =0;
		onFlag =1;
		onPos =0;
		infile>>numBits>>numSnaps;
		cout<<"Case # "<<i+1<<endl;//<<" Numbits "<<numBits<<"\tNumSnaps "<<numSnaps<<endl;
		if(numBits > 1)
		{
		onPos = (long)pow(2.0,numBits);
		//cout<<onPos<<"power"<<endl;
		numSnaps = numSnaps-onPos+1;
		//cout<<"Num Bits "<<numBits<<"\tNum Snaps "<<numSnaps<<endl;
		if(numSnaps < 0)
		{
			onFlag=1;
		}
		else if(numSnaps == 0)
		{
			onFlag =0;
		}
		else
		{
		mod=numSnaps%onPos;
		//cout<<"Modulus is "<<mod<<endl;
		onFlag=mod;
		}
		}
		else if(numSnaps == 0)
		{
			onFlag =1;
		}
		else
		{
			onPos = numSnaps %2;
			if(onPos == 1)
			{
				onFlag = 0;
			}
		}
		
	
		
		if(onFlag == 0 )
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
