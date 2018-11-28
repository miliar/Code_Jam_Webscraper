#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <strstream>
#include <math.h>
#include <stdio.h>
#include <conio.h>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int nTestCases;
int caseNumber;
int N;
char teamRecord[100][100];
double WP[100];
double WP2[100];	//for calc OWP
double OWP[100];
double OOWP[100];
int win[100];
int lose[100];
int play[100];

void Process()
{
	//WP
	for (int team=0; team<N; team++)
	{
		win[team]=0;
		lose[team]=0;
		for (int opp=0; opp<N; opp++)
		{
			if (team!=opp)
			{
				if (teamRecord[team][opp]=='1')
					win[team]++;
				else if (teamRecord[team][opp]=='0')
					lose[team]++;
			}
		}
		play[team]= win[team]+lose[team];
		WP[team] = (double)win[team]/play[team];
	}
	//OWP
	for (int team=0; team<N; team++)
	{
		int cnt=0;
		double totwp2=0;
		for (int opp=0; opp<N; opp++)
		{
			WP2[opp] = 0;
			if (team!=opp)
			{
				if (teamRecord[team][opp]=='1')
				{
					WP2[opp] = (double)win[opp] / (play[opp]-1); 
					cnt++;
				}
				else if (teamRecord[team][opp]=='0')
				{
					WP2[opp] = (double)(win[opp]-1) / (play[opp]-1); 
					cnt++;
				}
				else
					continue;
			}
			totwp2+=WP2[opp];
		}
		OWP[team] = totwp2/cnt;
	}
	//OOWP
	for (int team=0; team<N; team++)
	{
		int cnt=0;
		double totowp=0;
		for (int opp=0; opp<N; opp++)
		{
			if (team!=opp)
			{
				if (teamRecord[team][opp]!='.')
				{
					totowp += OWP[opp];
					cnt++;
				}
				else
					continue;
			}
		}
		OOWP[team] = totowp/cnt;
	}
	double RPI;
	for (int team=0; team<N; team++)
	{
		RPI = 0.25*WP[team] + 0.5*OWP[team] + 0.25*OOWP[team];
		cout << RPI << endl;
	}
	return;
}


int main()
{
	string file1;
	string file2;
	file1 = "e:\\A-large.in";
	file1 = "e:\\zin.txt";
	file2 = "e:\\z2.out";
	FILE * ps;
	freopen_s(&ps, file1.c_str(), "rt", stdin);
	// comment this line for console output:
	freopen_s(&ps, file2.c_str(), "wt", stdout);

	scanf("%d", &nTestCases);
	char s[105];
	for (int caseNumber=1; caseNumber<=nTestCases; caseNumber++)
	{
		cin >> N;
		for (int i=0; i<N; i++)
		{
			cin >> s;
			for (int j=0; j<N; j++)
				teamRecord[i][j] = s[j];
		}
		cout << "Case #" << caseNumber << ": " << endl;
		Process();
//		cout << result << endl;
	}
	return 0;
}
