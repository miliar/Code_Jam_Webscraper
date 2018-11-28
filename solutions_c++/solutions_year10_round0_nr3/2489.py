// ThemePark.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

const char* inputFileName = "C-small-attempt1.in";
const char* outputFileName = "C-small-attempt1.out";

//const char* inputFileName = "C-large.in";
//const char* outputFileName = "C-large.out";

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

	unsigned int indexT = 0;
	unsigned int T = 0;
	if(inFile.good())
	{
		inFile>>T;
		if(T > 0)
		{
			indexT = 1;
			while(indexT <= T)
			{
				unsigned int R = 0;
				unsigned int K = 0;
				unsigned int N = 0;
				unsigned int indexN = 0;
				unsigned int indexR = 0;
				unsigned int Euros = 0;
				queue<unsigned int> group;
				

				inFile>>R;
				inFile>>K;
				inFile>>N;
				
				indexN = 0;
				while(indexN < N)
				{
					unsigned int g = 0;
					inFile>>g;
					group.push(g);
					indexN ++;
				}
				
				indexR = 0;
				Euros = 0;
				while(indexR < R)
				{
					unsigned int value = 0;
					indexN = 0;
					while(((value + group.front()) <= K) && indexN < N)
					{
						int frontV = group.front();
						value += frontV;
						group.pop();
						group.push(frontV);
						indexN ++;
					}
					Euros += value;
					indexR++;
				}

				outFile<<"Case #"<<indexT<<": "<<Euros<<endl;

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