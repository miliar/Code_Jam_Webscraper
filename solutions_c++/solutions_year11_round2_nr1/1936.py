#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int Add(int a, int b);


double CalculateRPI(int team, int teams);

char pStats[100][101];

int main(void)
{
	double              rpi[100];
	ifstream            input;
	int                 candies   = 0;
	int                 candy     = 0;
	int                 cc        = 0;
	int                 p1        = 0;
	int                 p2        = 0;
	int                 result    = 0;
	int                 teams     = 0;
	int                 team      = 0;
	int                 testCase  = 0;
	int                 testCases = 0;
	int                 value     = 0;
	ofstream            output;
	std::vector < int > candiesVector;

	//----------------------------------------------------------------------------------------------
	//  Open the input file.
	//----------------------------------------------------------------------------------------------
	input.open("A-large.in");
	if (false == input.is_open())
	{
		cout << "Unable to open input file!" << endl;
		return 1;
	}

	//----------------------------------------------------------------------------------------------
	//  Open the output file.
	//----------------------------------------------------------------------------------------------
	output.open("A-large.out");
	if (false == output.is_open())
	{
		cout << "Unable to open output file!" << endl;
		input.close();
		return 2;
	}

	//----------------------------------------------------------------------------------------------
	//  Load the input file.
	//----------------------------------------------------------------------------------------------
	input >> testCases;

	//----------------------------------------------------------------------------------------------
	//  Read all the test cases.
	//----------------------------------------------------------------------------------------------
	for (testCase = 1; testCase <= testCases; testCase++)
	{
		memset(rpi, 0, sizeof (rpi));
		memset(pStats, 0, sizeof (pStats));

		input >> teams;
		for (team = 0; team < teams; team++)
		{
			input >> pStats[team];
		}

		output << "Case #" << testCase << ":" << endl;

		output.precision(9);
		for (team = 0; team < teams; team++)
			output << CalculateRPI(team, teams) << endl;
	}

	input.close();
	output.close();

	return 0;
}

double CalculateRPI(int team, int teams)
{
	double owp       = 0;
	double owps[100] = {0};
	double result    = 0.0;
	int    games     = 0;
	int    losses    = 0;
	int    tt        = 0;
	int    uu        = 0;
	int    vv        = 0;
	int    ww        = 0;
	int    wins      = 0;

 	for (tt = 0; tt < teams; tt++)
	{
		if (tt == team)
			continue;

		switch (pStats[team][tt])
		{
			case '0':
				losses++;
				break;

			case '1':
				wins++;
				break;
		}
	}
	result = ((double) wins / ((double) (wins + losses))) / 4.0;

	losses = 0;
	wins   = 0;
	for (vv = 0; vv < teams; vv++)
	{
		owp    = 0.0;
		ww     = 0;
		for (tt = 0; tt < teams; tt++)
		{
			if (tt == vv)
				continue;
			if ('.' == pStats[vv][tt])
				continue;

			ww++;

			losses = 0;
			wins   = 0;
			for (uu = 0; uu < teams; uu++)
			{
				if (uu == tt)
					continue;
				if (uu == vv)
					continue;

				switch (pStats[tt][uu])
				{
					case '0':
						losses++;
						break;

					case '1':
						wins++;
						break;
				}
			}

			owps[vv] += (double) wins / ((double) wins + losses);
		}

		owps[vv] /= ww;
	}

	result += owps[team] / 2.0;

	owp = 0.0;
	uu  = 0;
	for (tt = 0; tt < teams; tt++)
	{
		if (tt == team)
			continue;

		if ('.' == pStats[team][tt])
			continue;

		owp += owps[tt];
		uu++;
	}
	owp /= uu;

	result += (owp / 4.0);

	return result;
}
