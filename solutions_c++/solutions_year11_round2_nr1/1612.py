// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MAXTEAM=100;
const int Wins=0;
const int Matches=0;
char table[MAXTEAM][MAXTEAM];

double wp[MAXTEAM];
double wp_without_team[MAXTEAM][MAXTEAM];
double owp[MAXTEAM];
double oowp[MAXTEAM];

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for (int t=1;t<=T;t++)
	{
		cout << "Case #" << t <<":" << endl;
		int N;
		cin >> N;
		for (int i=0;i<N;i++)
		{
			string s;
			cin >> s;
			for(int j=0;j<N;j++)
			{
				table[i][j]=s[j];
			}
		}

		for(int i=0;i<N;i++)
		{
			int wins=0; int teams=0;
			for(int j=0;j<N;j++)
			{
				if(table[i][j]=='1')
				{
					wins++;teams++;
				}
				else if(table[i][j]=='0')
				{
					teams++;
				}
			}
			wp[i] = (double)wins/teams;
		}

		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				int wins=0;	int teams=0;
				for(int k=0;k<N;k++)
				{
					if(k!=j && table[i][k]=='1')
					{
						wins++;teams++;
					}
					else if(k!=j && table[i][k]=='0')
					{
						teams++;
					}
				}
				wp_without_team[i][j] = (double)wins/teams;
			}
		}

		for(int i=0;i<N;i++)
		{
			double sum=0;
			int teams=0;
			for(int j=0;j<N;j++)
			{
				if(table[i][j]!='.')
				{
					sum+=wp_without_team[j][i];
					teams++;
				}
			}
			owp[i] = sum /teams;
		}

		for(int i=0;i<N;i++)
		{
			double sum=0;
			int teams=0;
			for(int j=0;j<N;j++)
			{
				if(table[i][j]!='.')
				{
					sum += owp[j];
					teams++;
				}
			}
			oowp[i] = sum/teams;
		}

		for(int i=0;i<N;i++) cout <<  0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
	}

	return 0;
}

