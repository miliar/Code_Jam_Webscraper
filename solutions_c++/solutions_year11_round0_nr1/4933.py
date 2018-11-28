#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
	ofstream fout("smallA.out");
	ifstream fin ("smallA.in");


	int T=0, N=0;
	fin >> T;
	char robot;
	int pos;
	
		
	for (int i=1;i<=T;i++)
	{
		int LastPosO = 1, LastPosB = 1, ElapsedTimeO = 0, ElapsedTimeB = 0 , totalTime = 0;
		int move = 0, neededTime = 0, actualTime = 0;

		fin >> N ;
		for (int i=1; i<=N ; i++)
		{
			fin >> robot >> pos; 
			if (robot=='O')
			{	
				move = abs(pos - LastPosO);
				neededTime = move + 1;
				actualTime = neededTime - ElapsedTimeO;
				if (actualTime<=0)
					actualTime = 1;
				ElapsedTimeO = 0;
				ElapsedTimeB += actualTime;
				LastPosO = pos;
				totalTime += actualTime;
			}
			else if (robot=='B')
			{
				move = abs(pos - LastPosB);
				neededTime = move + 1;
				actualTime = neededTime - ElapsedTimeB;
				if (actualTime<=0)
					actualTime = 1;
				ElapsedTimeB = 0;
				ElapsedTimeO += actualTime;
				LastPosB = pos;
				totalTime += actualTime;

			}
			else
			{
				//error
			}
		}
		fout << "Case #" <<i << ": " << totalTime << endl;
	}


}