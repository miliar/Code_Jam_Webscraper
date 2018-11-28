
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <string>

using namespace std;

const int sL=19;
const int sM=500;
char* ss="welcome to code jam";
int buff[sL][sM];


string Process(int p_nLen, string p_Params)
{	
	memset(buff,0,sizeof(int)*sL*sM);
	
	for (int i=0;i<sL;++i)
	{
		for (int j=0;j<p_Params.size();++j)
		{
			if (ss[i]==p_Params[j])
			{
				if (i==0)
				{
					buff[i][j]=1;
				}
				else
				{	
					for (int k=j-1;k>=0;--k)
					{
						buff[i][j]+=buff[i-1][k];
					}
				}
			}			
		}
	}

	int r=0;
	for (int j=0;j<p_Params.size();++j)	
	{
		r+=buff[sL-1][j];
	}
	char res[1024];
	sprintf(res,"%04d",r);
	return res;
}

void ProcessFile(ifstream &fIn,ofstream &fOut)
{	
	
	string line;
	getline(fIn,line);
	int nN=atoi(line.c_str());
	
	
	for (int i=0;i<nN;++i)
	{
		getline(fIn,line);		
		fOut << "Case #" << (i+1) << ": " << Process(1,line)<<"\n";
		
	}
}



int main(int argc, char* args[])
{
	string fsIn(args[1]);
	string fsOut(fsIn+".out");
	ifstream fIn(fsIn.c_str());
	ofstream fOut(fsOut.c_str());
	ProcessFile(fIn,fOut);
	fIn.close();
	fOut.close();
}