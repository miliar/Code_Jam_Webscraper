

#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <stdlib.h>

using namespace std;

int num_team;
int table[100][100];
int wins[100];
int games[100];
float wp[100];
float owp[100];
float oowp[100];
string str;

int main ()
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("input.txt");
	outFile.open("output.txt");
	int num_cases;
	inFile >> num_cases;
	
	for (int curr_case = 0 ; curr_case < num_cases ; curr_case++ )
	{
		memset(table, 0, sizeof(table));
		memset(wins, 0, sizeof(wins));
		memset(games, 0, sizeof(games));
		memset(wp, 0, sizeof(wp));
		memset(owp, 0, sizeof(owp));
		memset(oowp, 0, sizeof(oowp));
		inFile >> num_team;
		
		for (int curr_team = 0 ; curr_team < num_team ; curr_team++)
		{
			inFile >> str;

			for (int i = 0 ; i < num_team ; i++)
			{
				if (str[i] == '.')
					table[curr_team][i] = 2;
				else if (str[i] == '1')
					table[curr_team][i] = 1;
				else
					table[curr_team][i] = 0;
			}
		}
		
		for (int i = 0 ; i < num_team ; i++)
		{
			int win = 0;
			int game = 0;

			for (int j = 0 ; j < num_team ; j++)
			{
				if (table[i][j] == 0)
					game++;
				else if (table[i][j] == 1)
				{
					win++; game++;
				}
			}
			wp[i] = (float)win/(float)game;
			wins[i] = win;
			games[i] = game;
		}

		for (int i = 0 ; i < num_team ; i++)
		{
			float acc_per = 0;
			int team_game = 0;
			for (int j = 0 ; j < num_team ; j++)
			{
				int win = 0;
				int game = 0;
				if (((table[i][j] == 0) || (table[i][j] == 1)) && (i != j))
				{
					if (table[j][i] == 0)
					{
						win = wins[j];
						game = games[j] - 1;
					} else {
						win = wins[j] - 1;
						game = games[j] - 1;
					}
					acc_per += (float)win / (float)game;
					team_game++;
				}
			}
			owp[i] = acc_per / (float)team_game;
		}

		for (int i = 0 ; i < num_team ; i++)
		{
			float acc_per = 0;
			int team_game = 0;
			for (int j = 0 ; j < num_team ; j++)
			{
				if (table[i][j] != 2)
				{
					acc_per += owp[j];
					team_game++;
				}
			}
			oowp[i] = acc_per / (float)team_game;
		}

		outFile << "Case #" << curr_case + 1 << ": " << endl;
		for (int i = 0 ; i < num_team ; i++)
		{
			float rpi = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			outFile << setprecision (12) << rpi << endl;
		}
	}

	return 0;
}
