// GoogleCodeJam2011ProbA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
    ifstream inputFile;
	inputFile.open("A-large.in");
	
	ofstream outfile;
	outfile.open("A-large.out");

	int caseNum=0;
	string line;
	char *cline; 

	if (inputFile.is_open()) 
	{
		getline(inputFile,line);
		cline = new char [line.size()+1];
		strcpy(cline,line.c_str());
        // Extract number of cases 
		caseNum = atoi(strtok(cline," "));
	    
		// Handle case by case:
		for (int i=0; i<caseNum; i++)
		{
			getline(inputFile,line);
		    cline = new char [line.size()+1];
		    strcpy(cline,line.c_str());
			int steps = atoi(strtok(cline," "));
			vector<pair<char,int>> stepsInfo;
			for (int j=0; j<steps; j++) 
			{
				char robot = *strtok(NULL," ");
				int location = atoi(strtok(NULL," "));
				stepsInfo.push_back(pair<char,int>(robot,location));
			}

			vector<int> seqO;
			vector<int> seqB;
			for (int k=0; k<steps; k++)
			{
				if (stepsInfo[k].first=='O')
					seqO.push_back(stepsInfo[k].second);
				else
					seqB.push_back(stepsInfo[k].second);
			}

			int sizeO=seqO.size();
			int sizeB=seqB.size();
			int *timeO = new int[sizeO*2];
			int *timeB = new int[sizeB*2];
			//initialize O array
			int tmp=1;
			int current=0;
			for (int k=0; k<sizeO; k++)
			{
				timeO[2*k]=current+abs(seqO[k]-tmp);
				timeO[2*k+1]=timeO[2*k]+1;
				tmp=seqO[k];
				current=timeO[2*k+1];
			}

			//initialize B array
			tmp=1;
			current=0;
			for (int k=0; k<sizeB; k++)
			{
				timeB[2*k]=current+abs(seqB[k]-tmp);
				timeB[2*k+1]=timeB[2*k]+1;
				tmp=seqB[k];
				current=timeB[2*k+1];
			}
			
			int ptrO=-1;
			int ptrB=-1;
			int cp; //check point
			for (int j=0; j<steps; j++)
			{
				if (j==0)
				{
					if (stepsInfo[j].first=='O')
					{	ptrO=1; cp=timeO[ptrO]; }
					else
					{	ptrB=1; cp=timeB[ptrB]; }
				}
				else
				{
					if (stepsInfo[j].first=='O')
					{
						ptrO += 2;
						int diff = cp - timeO[ptrO];
						if (timeO[ptrO] <= cp)
							for (int m=ptrO; m<2*sizeO; m++)
								timeO[m] += diff+1;
						cp = timeO[ptrO];
					}
					else
					{
						ptrB += 2;
						int diff = cp - timeB[ptrB];
						if (timeB[ptrB] <= cp)
							for (int m=ptrB; m<2*sizeB; m++)
							{
								timeB[m] += diff+1;
							}
						cp = timeB[ptrB];
					}

				}
			}
			outfile<<"Case #"<<i+1<<": "<<cp<<endl;

		}















			/*

			cout<<endl;
			*/

	
		


	}



	return 0;
}

