#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

//////////////////////////////////////////////////////////////////////////

struct ONE_CASE
{
	long long N;
	int PD, PG;
};

//////////////////////////////////////////////////////////////////////////

int T;

ONE_CASE allCases[2000];
string results[2000];

int LoadData(char * filename)
{
	fstream f(filename);
	if (!f.is_open()) {
		return 0;
	}

	f >> T;

	for (int i = 0; i < T; ++i) {
		f >> allCases[i].N;
		f >> allCases[i].PD;
		f >> allCases[i].PG;
	}

	return 1;
}

void Process()
{
	int i;
	long long j, D, N, G, winD, winG, temp;
	int PD, PG;
	int flag = 0;

	for (i = 0; i < T; ++i)
	{
		flag = 0;
		N = allCases[i].N;
		PD = allCases[i].PD;
		PG = allCases[i].PG;

		if (PG == 0 && PD != 0)
		{
			results[i] = "Broken";
			continue;
		}

		if (PG == 100 && PD != 100)
		{
			results[i] = "Broken";
			continue;
		}

		for (D = N; D > 0; --D)
		{
			for (j = 0; j <= D; ++j)
			{
				if ((j * 100 / D) == PD)
				{
					flag = 1;
					break;
				}
			}
			if (flag)
			{
				break;
			}
		}

		if (!flag)
		{
			results[i] = "Broken";
			continue;
		}

		flag = 0;
		for (D = N; D > 0; --D)
		{
			winD = (D * PD) / 100;
			if ((D * PD) % 100 != 0)
			{
				continue;
			}

			for (G = D; ; ++G)
			{
				for (winG = winD; winG <= G; ++winG)
				{
					if ((winG * 100 / G) == PG)
					{
						results[i] = "Possible";
						flag = 1;
						break;
					}
				}

				if (flag)
				{
					break;
				}
			}

			if (flag)
				break;
		}

		if (!flag)
		{
			results[i] = "Broken";
		}
	}
}

void Output()
{
	stringstream ss;
	fstream f("output.txt", ios::out | ios::trunc);

	for (int i = 0; i < T; ++i) {
		ss << "Case #" << i + 1 <<": " << results[i] << "\r\n";
		f << ss.str();
		ss.str("");
	}
}

int main(int argc, char * agrv[])
{
	if (!LoadData("A-small-attempt11.in")) {
		return -1;
	}

	Process();
	Output();

	return 0;
}