#include <fstream>
#include <iostream>
#include <cstdlib>

#define ABS(a) ((a)<0 ? (-(a)):(a))
#define MAX(a,b) ((a)>(b) ? (a):(b))

using namespace std;

struct Person
{
	Person(char c)
	{
		ID = c;
		lastTimeUpdated = 0;
		lastPosition = 1;
	}
	char ID;
	int lastTimeUpdated;
	int lastPosition;
	int moveTo(int nextLoc, char _ID, int currentTime)
  	{
		if(_ID != ID)   return 0;

		int deltaPos = ABS(nextLoc - lastPosition);
		int deltaT = ABS(currentTime - lastTimeUpdated);
		
		int ret = MAX(deltaPos - deltaT,0) + 1; //amount of extra time required to be at position nextLoc and THEN push button
		
		lastTimeUpdated = currentTime + ret;
		lastPosition = nextLoc;
		return ret;
	}
};

int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");
	int T;
	fin>>T;
	for(int i=1;i<=T; i++)
	{
		int totalTime = 0;
		int N;
		Person oj('O'), blue('B');
		
        fin>>N;
		for(int j=1;j<=N;j++)
		{
			int tInt;
			string tStr;
			fin>>tStr;
			fin>>tInt;
			char currentMover = tStr[0];
			
			totalTime += oj.moveTo(tInt, currentMover, totalTime);
			totalTime += blue.moveTo(tInt, currentMover, totalTime);
		}
		fout<<"Case #"<<i<<": "<<totalTime<<"\n";
	}
	return 0;
}
