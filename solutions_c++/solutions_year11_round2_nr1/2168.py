#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
#define INPUT "A-large.in"
#define OUTPUT "prob1.out"

ifstream inp;
ofstream out;

int T;

double WP[100];
double OWP[100];
double OOWP[100];
double RPI[100];
int op[10000];
int totalOp[100];
int N;
char buffer[102];

void solve(int index)
{
	inp >> N;
	for (int i = 0; i< N; i++)
	{
		WP[i] = 0;
		OWP[i] = 0;
		OOWP[i] = 0;
		RPI[i] = 0;
		totalOp[i] = 0;
		for (int j=i+1; j<N; j++)
			op[i*N + j] = 0;
	}
	for (int i = 0; i< N ; i++)
	{
		int win = 0;
		int lose = 0;
		inp >> buffer;
		for (int j = 0; j < N; j++)
		{
			if (buffer[j] == '1') 
			{
				win ++;
				op[i*N+j] = 1;
			}
			else
				if (buffer[j] == '0')
				{
					lose ++;
					op[i*N+j] = -1;
				}
		}
		totalOp[i] = win + lose;
		WP[i] = win * 1.0 / totalOp[i] ;
	}
	for (int i = 0; i < N; i++)
		for (int j =i+1; j< N ; j++)
			if (op[i*N+j]!= 0)
			{
				if (op[i*N+j] == 1)
				{
					OWP[i] += (WP[j]*totalOp[j])/(totalOp[i]*(totalOp[j]-1));
					OWP[j] += (WP[i]*totalOp[i]-1)/(totalOp[j]*(totalOp[i]-1));
				}
				else
				{
					OWP[i] += (WP[j]*totalOp[j]-1)/(totalOp[i]*(totalOp[j]-1));
					OWP[j] += (WP[i]*totalOp[i])/(totalOp[j]*(totalOp[i]-1));
				}

			}
	for (int i = 0 ; i<N; i++)
		for (int j = i+1; j < N; j++)
			if (op[i*N+j])
			{
				OOWP[i] += OWP[j]/totalOp[i];
				OOWP[j] += OWP[i]/totalOp[j];
			}

	out << "Case #" << index << ": " << endl;
	for (int i = 0; i<N; i++)
	{
		RPI[i] =WP[i]*0.25+ 0.5 * OWP[i] + 0.25 * OOWP[i];
		out <<  setprecision(7) << RPI[i];
		out << endl;
	}
}

void main()
{
	inp.open(INPUT);
	out.open(OUTPUT);
	out << setiosflags(ios::left);
	inp >> T;
	for (int i = 1; i <= T; i++)
		solve(i);
	inp.close();
	out.close();
}