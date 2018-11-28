#include <fstream>
#include <cstring>
#include <cstdlib>

using namespace std;

ifstream in("rpi.in");
ofstream out("rpi.out");

const int N = 101;

int n;

int sc[N][N];
double awp[N];
double wp[N][N];
double owp[N];
double oowp[N];
double rpi[N];

void ReadCase()
{
	char ch;

	in >> n;

	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= n; ++j)
		{
			in >> ch;
			if (ch == '0')
				sc[i][j] = -1;
			else if (ch == '1')
				sc[i][j] = 1;
		}
}

void CalculateAwp()
{
	for (int j = 1; j <= n; ++j)
	{
		double noG = 0, noW = 0;

		for (int k = 1; k <= n; ++k)
			if ( sc[j][k])
			{
				++noG;

				if (sc[j][k] == 1)
					++noW;
			}

		awp[j] = noW / noG;
	}
}

void CalculateWp()
{
	for (int i = 1; i <= n; ++i)
	{
		for (int j = 1; j <= n; ++j)
		{
			double noG = 0, noW = 0;

			for (int k = 1; k <= n; ++k)
				if (k != i && sc[j][k])
				{
					++noG;

					if (sc[j][k] == 1)
						++noW;
				}

			wp[i][j] = noW / noG;
		}
	}
}

void CalculateOwp()
{
	for (int i = 1; i <= n; ++i)
	{
		int noG = 0;

		for (int j = 1; j <= n; ++j)
			if (sc[i][j])
			{
				owp[i] += wp[i][j];
				++noG;
			}

		owp[i] /= noG;
	}
}

void CalculateOowp()
{
	for (int i = 1; i <= n; ++i)
	{
		int noG = 0;

		for (int j = 1; j <= n; ++j)
			if (sc[i][j])
			{
				oowp[i] += owp[j];
				++noG;
			}

		oowp[i] /= noG;
	}
}

void GetRpi()
{
	for (int i = 1; i <= n; ++i)
	{
		rpi[i] = (awp[i]/4) + (owp[i]/2) + (oowp[i]/4);
		out << rpi[i] << "\n";
	}
}

void SolveCase(int test)
{
	out << "Case #" << test << ":\n";

	memset(awp, 0, sizeof(awp));
	memset(sc, 0, sizeof(sc));
	memset(owp, 0, sizeof(owp));
	memset(oowp, 0, sizeof(oowp));
	memset(rpi, 0, sizeof(rpi));

	ReadCase();
	CalculateAwp();
	CalculateWp();
	CalculateOwp();
	CalculateOowp();
	GetRpi();
}

int main()
{
	int t;
	in >> t;

	for (int i = 1; i <= t; ++i)
		SolveCase(i);

	return 0;
}
