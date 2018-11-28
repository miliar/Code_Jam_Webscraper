
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <list>

using namespace std;

char scores[100][100];
double RPI[100];

int N;

double wp(int j)
{
	double wins = 0;
	double losses = 0;
	for (int k=0; k<N; ++k)
	{
		if (scores[j][k] == '1') ++wins;
		if (scores[j][k] == '0') ++losses;
	}
	return wins/(wins+losses);
}

double wp(int j, int not)
{
	double wins = 0;
	double losses = 0;
	for (int k=0; k<N; ++k)
	{
		if (k == not) continue;
		if (scores[j][k] == '1') ++wins;
		if (scores[j][k] == '0') ++losses;
	}
	return wins/(wins+losses);
}

double owp(int j)
{
	double owp = 0;
	double opponents = 0;
	for (int k=0; k<N; ++k)
	{
		if (scores[j][k] != '.')
		{
			owp += wp(k, j);
			++opponents;
		}
	}

	return owp / opponents;
}

double oowp(int j)
{
	double oowp = 0;
	double opponents = 0;
	for (int k=0; k<N; ++k)
	{
		if (scores[j][k] != '.')
		{
			oowp += owp(k);
			++opponents;
		}
	}

	return oowp / opponents;
}

int main()
{
	ifstream in("A-large.in");
	//ifstream in("A-small.in");
	ofstream out("A_big.out");

	int T;
	in >> T;

	for (int i=0; i<T; ++i)
	{
		cout << "Case #" << i+1 << ":" << endl;
		out << "Case #" << i+1 << ":" << endl;
		in >> N;

		for (int j=0; j<N; ++j)
		{
			for (int k=0; k<N; ++k)
			{
				in >> scores[j][k];
			}
		}

		for (int j=0; j<N; ++j)
		{
			double rpi = 0.25 * wp(j);
			rpi += 0.5 * owp(j);
			rpi += 0.25 * oowp(j);

			cout << rpi << endl;
			out << rpi << endl;
		}

	}

	return 0;
}
