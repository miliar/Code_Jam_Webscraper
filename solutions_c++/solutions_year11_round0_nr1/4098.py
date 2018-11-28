#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int findNumSteps(vector<int>& oranges,vector<int>& blues,vector<char>& seq)
{
	int orPos = 1, bluePos=1,curSteps=0, orSeq=0, blueSeq=0;
	for(unsigned int i=0;i<seq.size();i++)
	{
		if (seq[i]=='O')
		{			
			int orDiff = abs(oranges[orSeq]-orPos);
			curSteps += orDiff;
			orPos = oranges[orSeq];
			if(blues.size()>(unsigned int)blueSeq)
			{
				int blueDiff = abs(blues[blueSeq]-bluePos);
				if (blueDiff<=orDiff+1) // blue bu arada yerine giderse
					bluePos = blues[blueSeq]; // onu yerine gotur
				else if (blues[blueSeq]-bluePos>0) // yoksa gidecegi yonde
					bluePos += orDiff+1; // gittigi kadar ilerlet
				else 
					bluePos -= orDiff+1;
			}
			orSeq++;
		}
		else 
		{
			int blueDiff = abs(blues[blueSeq]-bluePos);
			curSteps += blueDiff;
			bluePos = blues[blueSeq];
			if(oranges.size()>(unsigned int)orSeq)
			{
				int orDiff = abs(oranges[orSeq]-orPos);
				if (orDiff<=blueDiff+1)
					orPos = oranges[orSeq];
				else if (oranges[orSeq]-orPos>0)
					orPos += blueDiff+1;
				else 
					orPos -= blueDiff+1;
			}
			blueSeq++;
		}
		curSteps+= 1;
	}
	return curSteps;
}

int main() 
{
	int numLines;
	cin>>numLines;
	vector<int> output;
	for(int i=0;i<numLines;i++)
	{
		vector<char> seq;
		vector<int> oranges;
		vector<int> blues;
		int numIter;
		cin>>numIter;
		for(int j=0;j<numIter;j++)
		{
			char robot;
			int button;
			cin>>robot>>button;
			seq.push_back(robot);
			if (robot=='O')
				oranges.push_back(button);
			else 
				blues.push_back(button);
		}
		output.push_back(findNumSteps(oranges,blues,seq));
	}
	for(unsigned int i=0;i<output.size();i++)
		cout<<"Case #"<<i+1<<": "<<output[i]<<endl;
	return 0;
}
