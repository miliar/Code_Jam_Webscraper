#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>


using namespace std;

int main()
{
	ifstream in_file("A-large.in");
	ofstream out_file("A.out");
	out_file.precision(25);
	
	int trials;
	in_file >> trials;
	
	cout << trials << endl;

	for(int i = 1; i <= trials; i++)
	{
		cout << i << endl;

		out_file << "Case #" << i << ": " << endl;
		
		//debug code
		if(i == 2)
			cout << "ham";
		//end debug

		int teams;
		in_file >> teams;
		
		string scores[teams];
		
		for(int c = 0; c < teams; c++)
		{
			in_file >> scores[c];
		}

		double wp[teams];
		
		for(int c = 0; c < teams; c++)
		{
			int games_played = 0;
			int games_won = 0;
			
			for(int c1 = 0; c1 < teams; c1++)
			{
				if(scores[c][c1] == '0')
				{
					games_played++;
				}
				
				else if(scores[c][c1] == '1')
				{
					games_played++;
					games_won++;
				}
			}
			
			wp[c] = ((double)games_won ) / games_played;
		}
		
		double owp[teams];

		for(int c = 0; c < teams; c++)
		{
			double total = 0.0;
			int teams_played = 0;

			for(int c1 = 0; c1 < teams; c1++)
			{
				if(scores[c][c1] != '.') //if teams did not play
				{

					teams_played++;

					int games_played = 0;
					int games_won = 0;
					
					for(int c2 = 0; c2 < teams; c2++)
					{
						if(c2 == c) //skip if the original team
						{
							continue;
						}
						
						else if(scores[c1][c2] == '0')
						{
							games_played++;
						}
						
						else if(scores[c1][c2] == '1')
						{
							games_played++;
							games_won++;
						}
					}
					
					total += (((double)games_won ) / games_played);
				}
			}
			
			owp[c] = total / teams_played;
		}

		double oowp[teams];
		
		for(int c = 0; c < teams; c++)
		{
			double total = 0.0;
			int teams_played = 0;
			
			for(int c1 = 0; c1 < teams; c1++)
			{
				if(scores[c][c1] != '.')
				{
					
				
				
					teams_played++;
					
					total += owp[c1];
				}
			}
			
			oowp[c] = total / teams_played;
		}

		for(int c = 0; c < teams; c++)
		{
			double rpi = (0.25 * wp[c]) + (0.50 * owp[c]) + (0.25 * oowp[c]);
			
			out_file << rpi << endl;
		}
	}
	
	return 0;
}


