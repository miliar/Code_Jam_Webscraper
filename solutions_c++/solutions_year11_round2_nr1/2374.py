#include<iostream>
#include<fstream>
#include<vector>
#include<cstdlib>
#include<cstring>
#include<iterator>
#define FILE
using namespace std;
int main()
{
// Read from file
#ifdef FILE
	ifstream readStream;
	ofstream writeStream;
	readStream.open("A-small-attempt0.in", ios::in);
	writeStream.open("A_B1.out", ios::out);
#endif
	const int inputSize = 1000;
	char temp[inputSize];
	readStream.getline(temp, inputSize, '\n');
	int i;
	int nCase = atoi(temp);
	float *WP;
	float **WP_thrown;
	float *OWP;
	float *OOWP;
	float *RPI;
	int *totalScore;
	int *totalGame;
	int **table;
	for(i=0; i<nCase; i++)
	{
		readStream.getline(temp, inputSize, '\n');
		char *splitted;
		splitted = strtok(temp," ");
		int nTeam = atoi(splitted);
		WP = new float[nTeam];
		OWP = new float[nTeam];
		OOWP = new float[nTeam];
		RPI = new float[nTeam];
		totalGame = new int[nTeam];
		totalScore = new int[nTeam];
		table = new int*[nTeam];
		WP_thrown = new float*[nTeam];
		for(int r=0; r<nTeam; r++)
		{
			readStream.getline(temp, inputSize, '\n');
			table[r] = new int[nTeam];
			WP_thrown[r] = new float[nTeam];
			int tG = 0;
			int tS = 0;
			totalScore[r] = 0;
			for(int c=0; c<nTeam; c++)
			{
				char score = temp[c];
				if(score == '.') {
					table[r][c] = -1;
					continue;
				} else {
					tG++;
					table[r][c] = atoi(&score);
					tS += atoi(&score);
					totalScore[r] += atoi(&score);
				}
			}
			totalGame[r] = tG;
			if(tG > 0) WP[r] = tS / (float)tG;
			else WP[r] = 0.0;
			for(int c=0; c<nTeam; c++)
			{
				if(table[r][c] != -1)
				{
					WP_thrown[r][c] = totalScore[r] - table[r][c];
					WP_thrown[r][c] /= (totalGame[r]-1);
				}
				else
					WP_thrown[r][c] = WP[r];
			}
		}
		// Compute OWP
		for(int r=0; r<nTeam; r++)
		{
			int tA = 0;
			float totalWP = 0.0;
			for(int c=0; c<nTeam; c++)
			{
				if(table[r][c] != -1)
				{
					//totalWP += WP[c];
					totalWP += WP_thrown[c][r];
					tA++;
				}
			}

			if(totalGame[r] > 0) OWP[r] = totalWP / (float)tA;
			else OWP[r] = 0.0;
		}
		// Compute OOWP
		for(int r=0; r<nTeam; r++)
		{
			float totalOWP = 0.0;
			for(int c=0; c<nTeam; c++)
			{
				if(table[r][c] != -1)
					totalOWP += OWP[c];
			}

			if(totalGame[r] > 0) OOWP[r] = totalOWP / (float)totalGame[r];
			else OOWP[r] = 0.0;
		}
		// Compute RPI
		writeStream<<"Case #"<<(i+1)<<": "<<"\n";
		for(int r=0; r<nTeam; r++)
		{
			RPI[r] = 0.25 * WP[r] + 0.5 * OWP[r] + 0.25 * OOWP[r];
			writeStream<<RPI[r]<<"\n";
		}
		delete []WP;
		delete []RPI;
		delete []totalGame;
		delete []OWP;
		delete []OOWP;
		delete []table;
	}

	readStream.clear();
	readStream.close();
	writeStream.clear();
	writeStream.close();
	return 0;
}

