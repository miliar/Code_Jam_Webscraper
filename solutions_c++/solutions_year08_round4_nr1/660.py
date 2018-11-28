#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <algorithm>
#include <iomanip>

using namespace std;

ifstream fin;
ofstream fout;

const int MAXN = 40000;

bool change [MAXN];
bool intern [MAXN];
bool AND [MAXN];
int value [MAXN];
int minValue [MAXN][2];
int m ;

int getMin (int num, int req)
{
	if (minValue[num][req] != -1) return minValue[num][req];
	minValue [num][req] = -2;

	for (int i = 0; i < 2; ++ i)
	{
		if (num + num <= m) getMin(num + num, i);
		if (num + num + 1 <= m) getMin (num + num + 1, i);
	}

	for (int i = 0; i < 2; ++ i)
		if (minValue [num + num][i] != -2)
			for (int j = 0; j < 2; ++ j)
				if (minValue[num + num + 1][j] != -2)
				{
					int newVal = 0;
					if (AND[num]) newVal = i & j;
					else newVal = i | j;

					if (newVal == req && 
						(minValue[num][req] == -2 || minValue[num + num][i] + minValue[num + num + 1][j] < minValue[num][req]))
					{
						minValue[num][req] = minValue[num + num][i] + minValue[num + num + 1][j];
					}

					if (! change[num]) continue;

					if (AND[num]) newVal = i | j;
					else newVal = i & j;

					if (newVal == req && 
						(minValue[num][req] == -2 || minValue[num + num][i] + minValue[num + num + 1][j] + 1 < minValue[num][req]))
					{
						minValue[num][req] = minValue[num + num][i] + minValue[num + num + 1][j] + 1;
					}
				}
	
	return minValue[num][req];
}

int main (int argc, char * argv [])
{

	if (argc == 1)  
	{
		fin.open("input.txt");
		fout.open("output.txt");
	}
	else 
	{
		fin.open(argv[1]);
		fout.open(argv[2]);
	}

	int tests = 0;
	fin >> tests;

	while (tests -- > 0)
	{

		int val;

		fin >> m >> val;

		memset (intern, 0, sizeof (intern));
		memset (minValue, 0xff, sizeof (minValue));
		memset (AND, 0, sizeof (AND));
		memset (change, 0, sizeof (change));

		for (int i = 1; i <= (m - 1) / 2; ++ i)
		{
			int g, c;
			fin >> g >> c;

			intern[i] = true;
			change [i] = c == 1;
			AND [i] = g == 1;
		}

		for (int i = (m - 1) / 2 + 1; i <= m; ++ i)
		{
			int l;
			fin >> l;
			minValue [i][l] = 0;
			minValue [i][1 - l] = -2;
		}

		int res = getMin(1, val);

		static int caseNum = 0;
		fout << "Case #" <<  (++ caseNum) << ": ";
		if (res >= 0) fout << res ;
		else fout << "IMPOSSIBLE";
		fout << endl;
	}

	return 0;
}