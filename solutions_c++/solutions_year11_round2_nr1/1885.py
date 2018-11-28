#include <iostream>
#include <vector>

int nCases;
int nTeams;
std::vector< std::vector<int> > vSchedule;
std::vector<long double> vWins;
std::vector<long double> vOtherWins;
std::vector<long double> vOtherOtherWins;
std::vector<long double> vRPI;

void reset()
{
	nTeams = 0;
	vWins.clear();
	vSchedule.clear();
	vOtherWins.clear();
	vOtherOtherWins.clear();
	vRPI.clear();
}

void read_input()
{
	std::cin >> nTeams;
	for (int i = 0; i < nTeams; i++)
	{
		std::vector<int> teamSchedule;
		for (int j = 0; j < nTeams; j++)
		{
			char c;
			int v;
			std::cin >> c;
			switch (c)
			{
			case '.':
				v = -1;
				break;
			case '1':
				v = 1;
				break;
			case '0':
				v = 0;
				break;
			}
			teamSchedule.push_back(v);
		}
		vSchedule.push_back(teamSchedule);
	}
}

long double percent_wins(int iTeam, int iExcludeTeam)
{
	int wins = 0;
	int games = 0;
	for (int j = 0; j < nTeams; j++)
	{
		int nResult = vSchedule[iTeam][j];
		if (nResult != -1 && j != iExcludeTeam)
		{
			wins += nResult;
			games++;
		}
	}
	return (long double)wins / (long double)games;
}

void solve_input()
{
	// Percent Wins and OWP
	for (int i = 0; i < nTeams; i++)
	{
		long double nTotalPercentage = 0;
		int nTeamsPlayed = 0;
		vWins.push_back(percent_wins(i, i));
		for (int j = 0; j < nTeams; j++)
		{
			if (i != j && vSchedule[i][j] != -1)
			{
				nTotalPercentage += percent_wins(j, i);
				nTeamsPlayed++;
			}
		}
		long double owp = nTotalPercentage / (long double)(nTeamsPlayed);
		vOtherWins.push_back(owp);
	}

	// OOWP
	for (int i = 0; i < nTeams; i++)
	{
		long double nTotalPercentage = 0;
		int nTeamsPlayed = 0;
		for (int j = 0; j < nTeams; j++)
		{
			if (i != j && vSchedule[i][j] != -1)
			{
				nTotalPercentage += vOtherWins[j];
				nTeamsPlayed++;
			}
		}
		long double oowp = nTotalPercentage / (long double)(nTeamsPlayed);
		vOtherOtherWins.push_back(oowp);
	}

	// RPI
	for (int i = 0; i < nTeams; i++)
	{
		long double rpi = 0.25 * vWins[i]
			+ 0.5 * vOtherWins[i]
			+ 0.25 * vOtherOtherWins[i];
			vRPI.push_back(rpi);
	}
}

void print_solution(int nCase)
{
	std::cout << "Case #" << (nCase + 1) << ": " << std::endl;
	for (int i = 0; i < nTeams; i++)
	{
		std::cout.precision(12);
		std::cout << vRPI[i] << std::endl;
	}
}

int main()
{
	std::cin >> nCases;
	for (int i = 0; i < nCases; i++)
	{
		reset();
		read_input();
		solve_input();
		print_solution(i);
	}
	return 0;
}
