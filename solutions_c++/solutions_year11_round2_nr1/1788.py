// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>

#include <math.h>

#define GET(x,y,width) ( x*width + y  )

using namespace std;

vector<double> GetWP( char *mat, int numTeams )
{
	vector<double> wp;
	for (int k = 0; k < numTeams; k++ )
	{
		double numOpp = 0;
		double numWin = 0;
			
		for (int j = 0; j < numTeams; j++ )
		{
			if (mat[GET(k,j,numTeams)] != '.')
			{
				numOpp++;
			}
			if (mat[GET(k,j,numTeams)] == '1')
			{
				numWin++;
			}					
		}
		if (numOpp>0)
		{
			wp.push_back(numWin/numOpp);
		}
		else
		{
			wp.push_back(0);
		}
	}
	return wp;
}

int _tmain(int argc, _TCHAR* argv[])
{
	string line;
	ifstream myfile ("A-large (1).in");
	ofstream outFile;
	outFile.open("A-large.out");

	int cases;
	myfile>>cases;

	for( int i = 0; i < cases; i++ )
	{
		outFile<<"Case #"<<i+1<<": "<<endl;
		cout<<"Case #"<<i+1<<": "<<endl;
		int numTeams;
		myfile>>numTeams;
		char *mat = new char[numTeams*numTeams];
		for (int i = 0; i < numTeams; i++ )
		{	
			for (int j = 0; j < numTeams; j++ )
			{
				myfile>>mat[GET(i,j,numTeams)];
			}

		}

		vector<double> wp,owp,oowp, rpi;

		wp = GetWP(mat,numTeams);

		//owp
		for (int k = 0; k < numTeams; k++ )
		{
			char *matCopy =  new char[numTeams*numTeams];
			memcpy(matCopy,mat,numTeams*numTeams*sizeof(char));

			for (int r = 0; r < numTeams; r++ )
			{
				matCopy[GET(r,k,numTeams)] = '.';
			}
			vector<double> tempwp = GetWP(matCopy,numTeams);
			double sum = 0, count = 0;
			for (int l = 0; l < numTeams; l++ )
			{
				if (k != l && mat[GET(l,k,numTeams)] != '.' )
				{
					sum+= tempwp[l];
					count++;
				}
			}
			owp.push_back(  sum/count );
			
		}
		
		

		//oowp
		for (int k = 0; k < numTeams; k++ )
		{
			double sum = 0, count = 0;
			for (int l = 0; l < numTeams; l++ )
			{
				if (k != l && mat[GET(l,k,numTeams)] != '.')
				{
					sum+= owp[l];
					count++;
				}
			}
			oowp.push_back(sum/count);
		}
		
		//rpi
		for (int k = 0; k < numTeams; k++ )
		{
			double rpi = 0.25f * wp[k] + 0.5f*owp[k] + 0.25*oowp[k];
			cout<<rpi<<endl;
			outFile<<rpi<<endl;	
		}
		delete []mat;
	}

	myfile.close();
	outFile.close();
	return 0;
}



