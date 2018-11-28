#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int solve(bool pris [], int rel [], int P, int Q)
{
	//cout<<"ok";
	long mincoins = 0;
	do
	{
		long coins = 0;
		bool pristemp [10000] = {false};

		for(int i = 1; i <= P; i++)
		{
			pristemp[i] = pris[i];
		}

		for(int i = 0; i < Q; i++)
		{
			//cout << rel[i] <<endl;
			pris[rel[i]] = false;
			int temp = rel[i] - 1;

			while(pris[temp])
			{
				if(temp > P)
					break;
				coins++;
				temp--;
			}

			temp = rel[i] + 1;

			while(pris[temp])
			{
				if(temp == 0)
					break;
				coins++;
				temp++;
			}

		}

		if(mincoins == 0 || coins < mincoins)
		{
			mincoins = coins;
		}

		for(int i = 1; i <= P; i++)
		{
			pris[i] = pristemp[i];
		}

	}while(next_permutation(rel, rel + Q));

	return mincoins;
}


int main()
{
	ifstream fin;
	ofstream fout;

	fin.open("C-small-attempt0.in");
	fout.open("C-small-attempt0.out");

	int N;
	fin >> N;

	for(int i = 0; i < N; i++)
	{
		unsigned int P, Q;
		int rel[100];

		fin >> P >> Q;

		for(int j = 0; j < Q; j++)
		{
			fin >> rel[j];
		}

		bool pris[10000] = {false};

		for(int j = 1; j <= P; j++)
		{
			pris[j] = true;
		}

		fout << "Case #" << i + 1 << ": " << solve(pris, rel, P, Q) << endl;
	}
}

