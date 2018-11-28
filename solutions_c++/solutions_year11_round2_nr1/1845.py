#include<iostream>
#include<vector>
using namespace std;

int main()
{

	int TESTCASES;
	cin >> TESTCASES;
	for(int testCase = 0; testCase < TESTCASES;testCase++)
	{
		vector<string> teams;
		vector<double> wp;
		vector<double> owp;
		vector<double> oowp;
		int numTeams;
		cin >> numTeams;
		for(int i = 0; i < numTeams;i++)
		{
			string g;
			cin >> g;
			teams.push_back(g);
		}
		vector<double> gamesPlayed;
		vector<double> gamesWon;
		for(int i = 0; i < teams.size();i++)
		{
			double numGames = 0;
			double numWins = 0;
			for(int j = 0; j < teams.size();j++)
			{
				if(teams[i][j] == '1')
				{
					numGames++;
					numWins++;
				}
				if(teams[i][j] == '0')
				{
					numGames++;
				}
			}
			gamesPlayed.push_back(numGames);
			gamesWon.push_back(numWins);
		}
		
		//calculate wp
		for(int i = 0; i < teams.size();i++)
		{
			double percentage = 0;
			if(gamesWon[i] != 0)
			{
				percentage = gamesWon[i] / gamesPlayed[i];
			}
			wp.push_back(percentage);
		}
			
		
		//calc owp
		for(int i = 0; i < teams.size();i++)
		{
			double sum = 0;
			double num  = 0;
			for(int j = 0; j < teams.size();j++)
			{
				if(teams[i][j] == '1')
				{
					if(gamesPlayed[j] == 1)
						sum += 0;
					else
						sum += (gamesWon[j])/(gamesPlayed[j] -1);
					num++;
				}
				if(teams[i][j] == '0')
				{
					if(gamesPlayed[j] == 1)
						sum += 0;
					else
						sum += (gamesWon[j]-1)/(gamesPlayed[j] -1);
					num++;
				}
			}
			double x= 0;
			if(num != 0)
				x = sum/num;
			
			owp.push_back(x);
		}
		
		for(int i = 0; i < teams.size();i++)
		{
			double num = 0;
			double sum = 0;
			for(int j = 0; j < teams.size();j++)
			{
				if(teams[i][j] != '.')
				{
					num++;
					sum += owp[j];
				}
			}
			double x = 0;
			if(num != 0)
				x = sum/num;
			oowp.push_back(x);
		}
		cout << "Case #" << (testCase+1) << ":" << endl;
		for(int i = 0; i < teams.size();i++)
		{
			double x = .25*wp[i];
			double y = .5*owp[i];
			double z = .25*oowp[i];
			cout << x + y + z << endl;
		}
	
	
	}
	
}