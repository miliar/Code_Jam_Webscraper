#include <iostream>
#include <fstream>
using namespace std;

ifstream input("A-large.in");
ofstream output("A-large.txt");
// #define input cin
// #define output cout

int T,N;
char r[101][101];
double wp[101];
double owp[101];
double oowp[101];
double rpi[101];
int total[101];
int w[101];

int main()
{
	input >> T;
	int count;
	for(count = 0; count < T; count++)
	{
		input >> N;
		int i,j;
		for(i = 0; i < N; i++)
		{
			w[i] = total[i] = 0;
			for(j = 0; j < N; j++)
			{
				input >> r[i][j];
				if(r[i][j] != '.')
					total[i]++;
				if(r[i][j] == '1')
					w[i]++;
			}
			wp[i] = 1.0*w[i]/total[i];
		}
		for(i = 0; i < N; i++)
		{
			owp[i] = 0.0;
			for(j = 0; j < N; j++)
			{
				if(r[i][j] == '1')
				{
					owp[i] += 1.0*w[j]/(total[j]-1);
				}
				else if(r[i][j] == '0')
				{
					owp[i] += 1.0*(w[j]-1)/(total[j]-1);					
				}
			}
			owp[i] /= total[i];
		}
		for(i = 0; i < N; i++)
		{
			oowp[i] = 0.0;
			for(j = 0; j < N; j++)
			{
				if(r[i][j] != '.')
					oowp[i] += owp[j];
			}
			oowp[i] /= total[i];
		}
		for(i = 0; i < N; i++)
		{
			rpi[i] = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
		}
		output << "Case #" << count+1 << ":" << endl;
		for(i = 0; i < N; i++)
		{
			output << rpi[i] << endl;
		}
	}
	return 0;
}