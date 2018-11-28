#include <iostream>
#include <fstream>

#define WIN 1
#define DRAW 0
#define LOSS -1

using namespace std;

int main()
{
	int T, N;
	int ** table, * wins, * matchs;
	double * rpi, *wp, *owp, oowp;
	char entry;
	
	ifstream input("A.in");
	ofstream output("A.out");

	input >> T;

	for (int i = 0; i < T; i++)
	{
		input >> N;
		
		table = new int * [N];
		for (int j = 0; j < N; j++)
			table[j] = new int[N];

		wins = new int[N];
		matchs = new int[N];
		rpi = new double[N];
		owp = new double[N];

		for (int j = 0; j < N; j++)
		{
			wins[j] = 0;
			matchs[j] = 0;
		}

		for (int j = 0; j < N; j++)
			for (int k = 0; k < N; k++)
			{
				input >> entry;
				if (entry == '1')
				{
					table[j][k] = WIN;
					wins[j]++;
					matchs[j]++;
				}
				else if (entry == '.')
					table[j][k] = DRAW;
				else
				{
					table[j][k] = LOSS;
					matchs[j]++;
				}
			}

		for (int j = 0; j < N; j++)
		{
			owp[j] = 0;
			for (int k = 0; k < N; k++)
			{
				if (table[j][k] == DRAW)
					continue;
				else if (table[j][k] == LOSS)
					owp[j] += (double)(wins[k]-1) / (double)(matchs[k]-1);
				else
					owp[j] += (double)wins[k] / (double)(matchs[k]-1);
			}
			owp[j] /= (double)matchs[j];
		}

		for (int j = 0;	j < N; j++)
		{
			rpi[j] = 0.25 * (double)wins[j] / (double)matchs[j];
			rpi[j] += 0.5 * owp[j];
			oowp = 0;
			for (int k = 0; k < N; k++)
			{
				if (table[j][k] == DRAW)
					continue;
				else
					oowp += owp[k];
			}
			rpi[j] += 0.25 * oowp/(double)matchs[j];
		}

		output << "Case #" << i+1 << ":" << endl;
		
		for (int j = 0; j < N; j++)
			output << rpi[j] << endl;
		

		delete [] owp;
		delete [] rpi;
		delete [] wins;
		delete [] matchs;
		for (int j = 0; j < N; j++)
			delete [] table[j];
		delete [] table;
	}

	input.close();
	output.close();
	
	return 0;
}
