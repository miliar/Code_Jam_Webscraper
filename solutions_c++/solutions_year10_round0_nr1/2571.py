// snapper.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
using namespace std;

const char* inputFileName = "A-large.in";
const char* outputFileName = "A-large.out";

//const char* inputFileName = "A-large-practice.in";
//const char* outputFileName = "A-large-practice.out";

int main(int argc, char* argv[])
{
	ifstream inFile;
	ofstream outFile;

	inFile.open (inputFileName, ifstream::in);
	outFile.open (outputFileName, ofstream::out);

	if(!inFile.is_open() || !outFile.is_open())
	{
		cout << "Can't open file!"<<endl;
		return 0;
	}

	int indexT = 0;
	int T = 0;
	if(inFile.good())
	{
		inFile>>T;
		if(T > 0)
		{
			indexT = 1;
			while(indexT <= T)
			{
				int N = 0;
				int K = 0;
				int value = 0;

				inFile>>N;
				inFile>>K;
				
				value = 1 << N;
				
				if(value == ((K % value) + 1))
				{
					outFile<<"Case #"<<indexT<<": "<<"ON"<<endl;
				}
				else
				{
					outFile<<"Case #"<<indexT<<": "<<"OFF"<<endl;
				}
				indexT++;
			}
		}
	}
	else
	{
		//do nothing;
	}

	inFile.close();
	outFile.close();
	return 0;

}