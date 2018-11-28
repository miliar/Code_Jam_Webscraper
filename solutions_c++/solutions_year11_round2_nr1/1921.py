#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>
#include <list>
#include <map>

using namespace std;

int main()
{
	FILE *in=fopen("d:/input.in.txt","r");
    FILE *out=fopen("d:/output.txt","w");
	int T = 0;
    fscanf(in,"%d",&T); 
    for (int ii=0;ii < T ;ii++)
    {
		int N = 0;
 		fscanf(in,"%d %d ",&N);
		vector<string> dict;
		vector<double> WP;
		vector<double> OWP;
		vector<double> OOWP;
		vector<double> RPI;
		for (int i=1;i<=N;i++)
		{
			char s[101];
			fscanf(in,"%s ",&s); 
			string ss(s);
			dict.push_back(ss);
		}

		for (int i=0;i<N;i++)
		{
			int totalGames=0;
			int totalWins=0;
			for (int j=0;j<dict[i].size();j++)
			{
				if ( dict[i][j] != '.' )
				{
					totalGames++;
					if ( dict[i][j] == '1' )
						totalWins++;
				}
			}
			double temp=(double)totalWins/(double)totalGames;
			WP.push_back(temp);
		}

		for (int i=0;i<N;i++)
		{
			double temp=0.0;
			int tgames=0;
			for (int j=0;j<dict[i].size();j++)
			{
				if ( dict[i][j] != '.' )
				{
					tgames++;
					int totalGames=0;
					int totalWins=0;
							
					if ( dict[i][j] != '.' )
					{
						for (int k=0;k<N;k++)
						{
							if ( k != i && dict[j][k] != '.' )
							{
								totalGames++;
								if ( dict[j][k] == '1' )
									totalWins++;
							}
						
						}
					}
					temp = temp+((double)totalWins/(double)totalGames);
				}
			}
			OWP.push_back(temp/tgames);
		}

		for (int i=0;i<N;i++)
		{
			double tsum=0.0;
			int totalGames=0;
			for (int j=0;j<dict[i].size();j++)
			{
				if ( dict[i][j] != '.' )
				{
					totalGames++;
					tsum+=OWP[j];
				}
			}
			OOWP.push_back(tsum/totalGames);
			RPI.push_back((((double)0.25)*WP[i])+(((double)0.50)*OWP[i])+(((double)0.25)*OOWP[i]));
		}

		fprintf(out,"Case #%d:\n",ii+1); 
		for (int j=0;j<N;j++)
		{
			fprintf(out," %lf\n",RPI[j]); 
		}
	}
	return 0;
}
