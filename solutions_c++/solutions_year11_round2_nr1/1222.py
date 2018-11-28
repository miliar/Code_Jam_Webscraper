// RPI

#include <fstream>
#include <cstdlib>
#include <iomanip>

using namespace std;

double wp[110];
double owp[110];
double oowp[110];
double RPI[110];
int c[110];
char s[110][110];
int N;

void deal (fstream &ouf)
{
	int i, count, win, j;
	for (i = 0; i < N; i++)
	{
		count = win = 0;
		for (j = 0; j < N; j++)
		{
			if (s[i][j] == '1')
			{
				count++;
				win++;
			}
			else if (s[i][j] == '0')
			{
				count++;
			}
		}
		c[i] = count;
		wp[i] = (double)win / (double)count;
	}
	for (i = 0; i < N; i++)
	{
		owp[i] = 0.;
		count = 0;
		for (j = 0; j < N; j++)
		{
			if (s[i][j] != '.')
			{
				count++;
				if (s[i][j] == '1')
				{
				    owp[i] += (wp[j] * c[j]) / (double)(c[j] - 1);
				}
				else
				{
					owp[i] += (wp[j] * c[j] - 1) / (double)(c[j] - 1);
				}
			}
		}
		owp[i] /= (double)count;
	}
	for (i = 0; i < N; i++)
	{
		oowp[i] = 0.;
		count = 0;
		for (j = 0; j < N; j++)
		{
			if (s[i][j] != '.')
			{
				count++;
				oowp[i] += owp[j];
			}
		}
		oowp[i] /= (double)count;
	}
	for (i = 0; i < N; i++)
	{
		RPI[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
		ouf << setprecision(12) << RPI[i] << endl;
	}
}

int main()
{
	fstream inf;
	inf.open("A-large.txt", ios::in);
	if (!inf)
	{
		exit(0);
	}
	fstream ouf;
	ouf.open("result.txt", ios::out);
	if (!ouf)
	{
		exit(0);
	}
	int T;
	inf >> T;
	int i, j;
	for (i = 0; i < T; i++)
	{
		inf >> N;
		for (j = 0; j < N; j++)
		{
			inf >> s[j];
		}
		ouf << "Case #" << i + 1 << ":" << endl;
		deal(ouf);
	}
	inf.close();
	ouf.close();
	return 0;
}