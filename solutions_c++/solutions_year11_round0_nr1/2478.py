#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

const string inputFile ="A-large.in";

int max(int a, int b)
{
if(a>b)
return a;
return b;
}

int main()
{
	
	ifstream input;
	input.open(inputFile.c_str());
	int T;
	input>>T;
	ofstream output;
	output.open((inputFile+".out").c_str());
	
	for(int t=1;t<=T; t++)	
	{
			int N, currentPosition, previousPosition=1, lastPositionBeforeColorChange=1;
			int continousSum=0, totalSteps=0;
			char currentColor, previousColor='N'; // N : nothing
			input>>N;
			
			for(int n=1; n<=N; n++)
			{
				input>>currentColor>>currentPosition;
				if(currentColor==previousColor)
				{
						totalSteps += abs(currentPosition-previousPosition) + 1;
						continousSum += abs(currentPosition-previousPosition) + 1;
				}	
				else
				{
				//	cout<<t<<" "<<lastPositionBeforeColorChange<<" "<<continousSum<<endl;
				 	totalSteps += max(abs(currentPosition-lastPositionBeforeColorChange)-continousSum,0) +1;
					continousSum = max(abs(currentPosition-lastPositionBeforeColorChange)-continousSum,0) +1;
					lastPositionBeforeColorChange = previousPosition;
				//	cout<<totalSteps<<endl;
				}
				previousPosition = currentPosition;
				previousColor = currentColor;
	
				
			}
						output<<"Case #"<<t<<": "<<totalSteps<<endl;
	}

	return 0;
}
