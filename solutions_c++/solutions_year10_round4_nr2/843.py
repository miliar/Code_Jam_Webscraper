#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>

int main()
{
	char* temp = NULL;
	size_t size = 0;
	size_t len = getline(&temp, &size, stdin);
	int cases = atoi(temp);

	int test;
	for (test = 0; test < cases; test++)
	{
		len = getline(&temp, &size, stdin);
		int rounds = atoi(temp);
		int num_teams = pow(2, rounds);
		int* M = new int[num_teams];
		bool* satisfied = new bool[num_teams];
		len = getline(&temp, &size, stdin);
		char* line = temp;
		for (int i = 0; i < num_teams; i++)
		{
			M[i] = atoi(strsep(&line, " \r\n"));
			satisfied[i] = false;
		}

		int** prices = new int*[rounds];
		bool** going = new bool*[rounds];

		for (int i = 0; i < rounds; i++)
		{
			prices[i] = new int[(int)pow(2, rounds-i-1)];
			going[i] = new bool[(int)pow(2, rounds-i-1)];
			len = getline(&temp, &size, stdin);
			line = temp;
			for (int j = 0; j < pow(2, rounds-i-1); j++)
			{
				prices[i][j] = atoi(strsep(&line, " \r\n"));
				going[i][j] = false;
			}
		}

		int total_cost = 0;
		for(;;)
		{
			int min_misses = 31;
			int mmt = -1;
			for (int i = 0; i < num_teams; i++)
			{
				if (satisfied[i]) continue;
				if (min_misses > M[i])
				{
					min_misses = M[i];
					mmt = i;
				}
			}
			if (mmt == -1) break;

			//get list of games for team
			int* games = new int[rounds];
			for (int i = 0; i < rounds; i++)
			{
				games[i] = floor(mmt/pow(2,i+1));
			}

get_missing:
			int missing = 0;
			for (int i = 0; i < rounds; i++)
			{
				if (!going[i][games[i]]) missing++;
			}
			if (missing <= M[mmt]) 
			{
				satisfied[mmt] = true;
				continue;
			}

			//get cheapest game
			int cheapest = 1e7;
			int round = -1;
			for (int i = 0; i < rounds; i++)
			{
				if (going[i][games[i]]) continue;
				if (cheapest >= prices[i][games[i]])
				{
					round = i;
					cheapest = prices[i][games[i]];
				}
			}

			going[round][games[round]] = true;
			total_cost += cheapest;
			goto get_missing;
		}

		printf("Case #%i: %i\n", test+1, total_cost);
		delete[] M;
		delete[] satisfied;
		for (int i = 0; i < rounds; i++)
		{
			delete[] prices[i];
			delete[] going[i];
		}
		delete[] prices;
		delete[] going;
	}
}
