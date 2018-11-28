#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>

using namespace std;

char translatetable[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(int argc,char * argv[])
{
	int totalnumber;
	ifstream infile("A-small-attempt1.in");
	ofstream outfile("result.out");
	string readresult;
	infile>>totalnumber;
	getline(infile,readresult);
	for(int i=0;i<totalnumber;i++)
	{
		getline(infile,readresult);
		for(unsigned int k=0;k<readresult.length();k++)
		{
			if(readresult[k]>0x60&&readresult[k]<0x7B)
			{
				readresult[k]=translatetable[readresult[k]-0x61];
			}
			else if(readresult[k]>0x40&&readresult[k]<0x5B)
			{
				readresult[k]=translatetable[readresult[k]-0x41]-32;
			}
		}
		outfile<<"Case #"<<i+1<<": "<<readresult<<endl;
	}
	infile.close();
	outfile.close();
	return 0;
}
