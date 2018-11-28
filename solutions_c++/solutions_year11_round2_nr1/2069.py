#include <iostream>
#include <fstream>

using namespace std;

typedef unsigned int uint;
typedef unsigned long ulong;

int numCases;
int N;
char m[100][100];
int numOpponents[100];
double wp[100];
double owp[100];
double oowp[100];
double rpi[100];

int main (int argc, char * const argv[]) 
{
	if ( argc != 2 ) return -1;

	FILE * f = fopen(argv[1], "r");
	fscanf(f, "%d", &numCases);

	for ( int caseIndex = 0; caseIndex < numCases; caseIndex++ )
	{
		cout << "Case #" << caseIndex + 1 << ": " << endl;

		fscanf(f, "%d", &N);
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				fscanf(f, " %c", &(m[i][j]));
			}
		}

//		printf("N = %d\n", N);
//		for (int i = 0; i < N; i++)
//		{
//			for (int j = 0; j < N; j++)
//			{
//				printf("%c ", m[i][j]);
//			}
//			printf("\n");
//		}

		// Calculate WPs
		for (int i = 0; i < N; i++)
		{
			numOpponents[i] = 0;
			int numWins = 0;
			for (int j = 0; j < N; j++)
			{
				if (m[i][j] == '1')
				{
					numWins++;
					numOpponents[i]++;
				} else if (m[i][j] == '0')
				{
					numOpponents[i]++;
				}
			}
			
//			cout << "WP for " << i << ". Wins: " << numWins << " Opponents: " << numOpponents[i] << endl;
			if (numOpponents[i] == 0)
			{
				wp[i] = 0;
			} else
			{
				wp[i] = (double)numWins / numOpponents[i];
			}
		}

//		cout << "WPs:" << endl;
//		for (int i = 0; i < N; i++)
//		{
//			cout << wp[i] << endl;
//		}
		
		// Calculate OWPs
		for (int i = 0; i < N; i++)
		{
			double wpSum = 0;
			for (int j = 0; j < N; j++)
			{
				if (m[i][j] == '0')
				{
					wpSum += ((wp[j] * numOpponents[j]) - 1) / (numOpponents[j] - 1);
				} else if (m[i][j] == '1')
				{
					wpSum += ((wp[j] * numOpponents[j])) / (numOpponents[j] - 1);
				}
			}
			
			if (numOpponents[i] == 0)
			{
				owp[i] = 0;
			} else
			{
				owp[i] = wpSum / numOpponents[i];
			}			
		}

//		cout << "OWPs:" << endl;
//		for (int i = 0; i < N; i++)
//		{
//			cout << owp[i] << endl;
//		}
		
		// Calculate OOWPs
		for (int i = 0; i < N; i++)
		{
			double owpSum = 0;
			for (int j = 0; j < N; j++)
			{
				if (m[i][j] != '.')
				{
					owpSum += owp[j];
				}
			}
			
			if (numOpponents[i] == 0)
			{
				oowp[i] = 0;
			} else
			{
				oowp[i] = owpSum / numOpponents[i];
			}			
		}

//		cout << "OOWPs:" << endl;
//		for (int i = 0; i < N; i++)
//		{
//			cout << oowp[i] << endl;
//		}
		
		for (int i = 0; i < N; i++)
		{
			rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
		}
		
//		cout << "RPIs:" << endl;
		for (int i = 0; i < N; i++)
		{
			cout << rpi[i] << endl;
		}
	}

	fclose(f);
	return 0;
}
