#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	fstream inp,outp;
	inp.open("input.txt");
	outp.open("output.txt");
	int numTest,numDev,numSnap;
	inp>>numTest;
	for(int i=0; i<numTest; i++)
	{
		inp>>numDev>>numSnap;
		//this is binary counting, silly
		int mask=((1<<numDev)-1);
		if((numSnap&mask)==mask)
		{
			outp<<"Case #"<<i+1<<": ON"<<endl; 
		}
		else
		{
			outp<<"Case #"<<i+1<<": OFF"<<endl;
		}
	}
	return 0;
}
