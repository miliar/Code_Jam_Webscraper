#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

int main (int argc, char * const argv[]) {
    long t,k;
	int n,x=0;
	int output=0;
	int value=0;
	int case_Num=0;
	char *state;
	ifstream infile;
	ofstream outputFile;
	outputFile.open("largeOutput.txt");
	infile.open("/Users/Ish/Downloads/A-large.in");		//should include your location of the file
	if (!infile) {
		cerr << "Unable to open file A-small.in";
		exit(1);   // call system to stop
	}

	infile >> t;
	for(int i=1;i<=t;i++)
	{
		infile >> n;
		infile >> k;
		output = pow(2,n)-1;
		value = output;
		case_Num++;
		while(value < k)
		{
			value += pow(2,n);
			if(k == output|| k == value)
			{	
				state = "ON";
				outputFile << "Case #"<<case_Num<<": "<< state<<endl;
				
			}
			
		}
		if(k != output && k != value)
		{
			state="OFF";
			outputFile << "Case #"<<case_Num<<": "<< state<<endl;
		}
		if(k == output && k == value)
		{
			state = "ON";
			outputFile << "Case #"<<case_Num<<": "<< state<<endl;
		}
		
		x=0;
		value=0;
	}	
    return 0;
}
