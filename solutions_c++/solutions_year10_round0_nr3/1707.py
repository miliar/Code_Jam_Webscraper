// ThemePark.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

//const char* inputFileName = "C-small-attempt0.in";
//const char* outputFileName = "C-small-attempt0.out";

const char* inputFileName = "C-large.in";
const char* outputFileName = "C-large.out";

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
				long long Euros = 0;
				unsigned int current = 0;
				vector<unsigned int> group;
				vector<unsigned int> groupE;
				vector<unsigned int> groupIndex;

				inFile>>R;
				inFile>>K;
				inFile>>N;
				
				indexN = 0;
				while(indexN < N)
				{
					unsigned int g = 0;
					inFile>>g;
					group.push_back(g);
					indexN ++;
				}
				indexN = 0;
				while(indexN < N)
				{
					unsigned int ge = 0;
					unsigned int g = indexN;
					unsigned int iN = 0;
					while(ge + group[g] <= K && iN < N)
					{
						ge += group[g];
						g++;
						if(g == N)
						{
							g = 0;
						}
						iN++;
					}
					groupE.push_back(ge);
					groupIndex.push_back(g);
					indexN ++;
				}

				vector<unsigned int> forLoop(N, 0);
				unsigned int loopStart = 1;
				unsigned int loop = 0;
				long long valueBeforeLoop = 0;
				long long valueForLoop = 0;
				unsigned int looppoint = 0;
				current = 0;
				forLoop[current] = 1;
				valueBeforeLoop += groupE[current];
				indexN = 0;
				while(indexN < N)
				{
					if(forLoop[groupIndex[current]] == 1)
					{
						looppoint = groupIndex[current];
						forLoop[groupIndex[current]] = 2;
						valueForLoop += groupE[groupIndex[current]];
						current = groupIndex[current];
						loop = 1;
						while(forLoop[groupIndex[current]] != 2)
						{
							valueForLoop += groupE[groupIndex[current]];
							current = groupIndex[current];
							loop ++;
						}
						break;
					}
					forLoop[groupIndex[current]] = 1;
					valueBeforeLoop += groupE[groupIndex[current]];
					current = groupIndex[current];
					loopStart ++;
				}

				indexR = 0;
				Euros = 0;
				current = 0;
				if(R < loopStart)
				{
					indexR = 0;
					while(indexR < R)
					{
						Euros += groupE[current];
						current = groupIndex[current];
						indexR++;
					}
				}
				else
				{
					R -= loopStart;
					Euros += valueBeforeLoop;
					Euros += (R / loop) * valueForLoop;
					R %= loop;
					current = looppoint;
					indexR = 0;
					while(indexR < R)
					{
						Euros += groupE[current];
						current = groupIndex[current];
						indexR++;
					}

				}

				outFile<<"Case #"<<indexT<<": "<<Euros<<endl;

				indexT++;
			}
		}
	}

	inFile.close();
	outFile.close();
	return 0;
}