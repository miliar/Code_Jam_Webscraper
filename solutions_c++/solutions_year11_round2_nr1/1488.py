// ProblemA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>

using namespace std;

struct Rating
{
	double m_dPoints;
	double m_dGames;
	double m_dWP;
	double m_dOWP;
	double m_dOOWP;
	Rating():
	m_dWP(0.0),
	m_dOWP(0.0),
	m_dOOWP(0.0),
	m_dPoints(0.0),
	m_dGames(0.0)
	{}
};

int _tmain(int argc, _TCHAR* argv[])
{
	//ifstream in("A-small-attempt0.in");
 //   ofstream out("A-small-attempt0.out");

	ifstream in("A-large.in");
    ofstream out("A-large.out");

	map<char, double> mpPoints;
	mpPoints['1'] = 0.0;
	mpPoints['0'] = 1.0;
    int iTasks;
	in >> iTasks;
	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
		int nTeams;
		in >> nTeams;
		vector<string> vTable(nTeams);
		vector<Rating> vTableRatings(nTeams);
		for( int i = 0; i < nTeams; i++ )
		{
			in >> vTable[i];
		}
		for( int i = 0; i < nTeams; i++ )
		{
			double dWin = 0.0;
			double dGames = 0.0;
			for( int j = 0; j < nTeams; j++ )
			{
				if( vTable[i][j] == '1' )
					dWin += 1.0;
				if( vTable[i][j] != '.' )
					dGames += 1.0;
			}
			vTableRatings[i].m_dPoints = dWin;
			vTableRatings[i].m_dGames = dGames;
		}
		for( int i = 0; i < nTeams; i++ )
		{
			double dTmpWP = 0.0;
			double dGames = 0.0;
			for( int j = 0; j < nTeams; j++ )
			{
				if( i == j )
					continue;
				if( vTable[i][j] != '.' )
				{
					dTmpWP += (vTableRatings[j].m_dPoints - mpPoints[vTable[i][j]])/(vTableRatings[j].m_dGames - 1.0);	
					dGames += 1.0;
				}
			}
			vTableRatings[i].m_dOWP = dTmpWP / dGames; 
		}
		for( int i = 0; i < nTeams; i++ )
		{
			double dTmpWP = 0.0;
			double dGames = 0.0;
			for( int j = 0; j < nTeams; j++ )
			{
				if( i == j )
					continue;
				if( vTable[i][j] != '.' )
				{
					dTmpWP += vTableRatings[j].m_dOWP;	
					dGames += 1.0;
				}
			}
			vTableRatings[i].m_dOOWP = dTmpWP / dGames; 
		}
		out << "Case #" << iCount << ":\n";
		for( int i = 0; i < nTeams; i++ )
		{
			double dRes = vTableRatings[i].m_dPoints / vTableRatings[i].m_dGames * 0.25 +  vTableRatings[i].m_dOWP * 0.50 +  vTableRatings[i].m_dOOWP * 0.25;
			out << dRes << endl;
		}
	}
	return 0;
}
