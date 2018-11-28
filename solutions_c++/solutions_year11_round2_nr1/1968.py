#include "codejam.h"

void R1B_A()
{
	int T;
	cin >> T;
	for (int testCase = 1; testCase <= T; testCase++)
	{
		int N;
		cin >> N;

		char* matches = new char[N*N];		
		int pos = 0;

		for (int i = 1; i <= N; i++)
		{
			char* team = NULL;
			team = new char[N];
			cin >> team;
			stringCopy(team, matches, pos);
			pos += N;
		}

		double* WP = new double[N];
		double* OWP = new double[N];
		double* OOWP = new double[N];
		int* numMatches = new int[N];
		int* numWins = new int[N];

		for (int i = 0; i < N; i++)
		{
			numWins[i] = 0;
			numMatches[i] = 0;
			for (int j = 0; j < N; j++)
			{
				if (matches[i*N+j] == '1')
				{
					numWins[i]++;
					numMatches[i]++;
				}
				else if (matches[i*N+j] == '0')
				{
					numMatches[i]++;
				}
			}
			WP[i] = (double)numWins[i] / (double)numMatches[i];
		}

		for (int i = 0; i < N; i++)
		{
			double sumWP = 0;
			for (int j = 0; j < N; j++)
			{
				if (matches[i*N+j] == '1')
				{
					sumWP += (double)numWins[j] / ((double)numMatches[j] - 1);
				}
				else if (matches[i*N+j] == '0')
				{
					sumWP += ((double)numWins[j] - 1) / ((double)numMatches[j] - 1);
				}
			}
			OWP[i] = sumWP / (double)numMatches[i];
		}

		for (int i = 0; i < N; i++)
		{
			double sumOWP = 0;
			for (int j = 0; j < N; j++)
			{
				if (matches[i*N+j] != '.')
				{
					sumOWP += OWP[j];
				}
			}
			OOWP[i] = sumOWP / (double)numMatches[i];
		}

		cout << "Case #" << testCase << ":\n";
		for (int i = 0; i < N; i++)
		{
			cout << 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i] << "\n";
		}

	}
}

void stringCopy(char from[], char to[], int toPos)
{
	for (int i = 0; from[i] != '\0'; i++)
	{
		to[i + toPos] = from[i];
	}
}