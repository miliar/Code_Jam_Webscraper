#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <string>
#include <memory>
#include <iomanip>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("1b_a.out");
//#define fout cout

const int WIN = 1;
const int LOSE = 0;
const int NONE = -1;

int d[200][200];
double wp[200];
int awinc[200], atotalc[200];
double owp[200], oowp[200];
int m;

int main()
{
	int N;
	fin >> N;
	for (int cases = 0; cases < N; cases++)
	{
		fout << "Case #" << cases+1 << ":" << endl;
		memset(d, 0, sizeof d);
		fin >> m;
		for (int j=0; j<m; j++)
		{
		string s;
		fin >> s;
		for (int i=0; i<m; i++)
		{
			switch (s[i])
			{
			case '0':
				d[j][i] = LOSE;
				break;
			case '1': 
				d[j][i] = WIN;
				break;
			default:
				d[j][i] = NONE;
				break;
			}
		}
		}
		for (int i=0; i<m; i++)
		{
			int winc = 0;
			int totalc = 0;
			for (int j=0; j<m; j++) {
				if (d[i][j] == WIN) winc++;
				if (d[i][j] != NONE) totalc++;
			}
			awinc[i] = winc;
			atotalc[i] = totalc;
			wp[i] = winc* 1.0 /totalc;
		}
		for (int i=0; i<m; i++)
		{
			double now = 0;
			for (int j=0; j<m; j++)
				if (NONE != d[i][j])
			{
				if (d[i][j] == WIN) now += awinc[j]*1.0 / (atotalc[j]-1);
				else now += (awinc[j] - 1) * 1.0 / (atotalc[j]-1);
			}
			now /= atotalc[i];
			owp[i] = now;
		}
		for (int i=0; i<m; i++)
		{
			double now = 0;
			for (int j=0; j<m; j++)
			{
				if (d[i][j] != NONE) now += owp[j];
			}
			oowp[i] = now/atotalc[i];
		}
		for (int i=0; i<m; i++)
		{
			fout << fixed << setprecision(12) << 0.25 * wp[i] + 0.5*owp[i] + 0.25*oowp[i] << "\n";
		}
	}
	return 0;
}