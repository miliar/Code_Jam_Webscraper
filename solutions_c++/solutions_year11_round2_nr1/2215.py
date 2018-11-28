// ProgramA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

#define fabc(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fa0c(a,b) fabc( a, 0, ( b ) )
#define for_i(a) fa0c( i, ( a ) )
#define for_j(a) fa0c( j, ( a ) )
#define for_k(a) fa0c( k, ( a ) )
#define for_x(a) fa0c( x, ( a ) )
#define for_y(a) fa0c( y, ( a ) )

int _tmain(int argc, _TCHAR* argv[])
{
	int i,j,k,x,y;
	fstream f_input, f_output,f_output1;
	f_input.open(argv[1],fstream::in);
	f_output.open("ProgramAOut.txt",fstream::out);
	f_output1.open("ProgramAOutRead.txt",fstream::out);


	//read test cases
	int T = 0;
	f_input >> T;
	for_i(T)
	{
		f_output  << "Case #" << i+1 << ": " << endl;
		f_output1 << "Case #" << i+1 << ": " << endl;
		int TeamsN = 0;
		f_input >> TeamsN;
		char **TeamsData = new char*[TeamsN];

		for_j(TeamsN) //read teams scores
		{
			TeamsData[j] = new char[TeamsN];
			for_k(TeamsN) //read data
			{
				f_input >> TeamsData[j][k];
			}
		}
		

		//calculate RPI
		double *TeamWP = new double[TeamsN];
		double *TeamOWP = new double[TeamsN];
		double *TeamOOWP = new double[TeamsN];
		for_j(TeamsN) // j - current team
		{
			TeamWP[j] = 0;
			TeamOWP[j] = 0;
			TeamOOWP[j] = 0;
			int GamesPlayed = 0;
			int GamesWon = 0;
			int OTeams = 0;
			for_k(TeamsN) //k - opponents
			{
				
				if(TeamsData[j][k] != '.')
				{
					OTeams++;
					GamesPlayed++;
					if(TeamsData[j][k] == '1')
					{
						GamesWon++;
					}


					int OGamesWon = 0;
					int OGamesPlayed = 0;
					for_x(TeamsN) //x - opponents opponents
					{

						if(TeamsData[k][x] != '.' && x != j) //opponents opponents (x) cannot be current team (j)
						{
							
							OGamesPlayed++;
							if(TeamsData[k][x] == '1')
							{
								OGamesWon++;
							}
						}
						
					}
					TeamOWP[j] += (double)OGamesWon/(double)OGamesPlayed;
					

				}

			}
			TeamOWP[j] /= OTeams;
			TeamWP[j] = (double)GamesWon/(double)GamesPlayed;


		}
		
		for_j(TeamsN)
		{
			TeamOOWP[j]=0;
			int GamesPlayed = 0;
			for_k(TeamsN)
			{
				if(TeamsData[j][k] != '.')
				{
					GamesPlayed++;
					TeamOOWP[j]+=TeamOWP[k];
				}
			}
			TeamOOWP[j]/=GamesPlayed;
			double REI = (0.25*TeamWP[j])+(0.50*TeamOWP[j])+(0.25*TeamOOWP[j]);
			f_output  << setprecision (12) << REI << endl;
			f_output1 << setprecision (12) << REI << endl;
		}

		



	}


	f_input.close();
	f_output.close();
	f_output1.close();
	return 0;
}

