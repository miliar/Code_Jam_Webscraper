#include <windows.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace::std;

char* pc;
int n;
char* getteam(int i)
{
	return pc + i * n;
}

double calcWP(int team, int except)
{
	char* ps = getteam(team);
	double win = 0, t = 0;
	for(int i = 0; i < n; i++)
	{
		if(i == except)
			continue;
		if(ps[i] == '1')
		{
			win++;
			t++;
		}
		else if(ps[i] == '0')
			t++;
	}
	return win / t;
}

double calcOWP(int team)
{
	char* ps = getteam(team);
	double d = 0;
	int t = 0;
	for(int i = 0; i < n; i++)
	{
		if(i == team || ps[i] == '.')
			continue;
		d += calcWP(i, team);
		t++;
	}
	return (t > 0 ? d / t : 0);
}

int main(int argc, char* argv[])
{
	ifstream cin(argv[1]);

	int nCount, numCase = 1;
	cin >> nCount;

	while (numCase <= nCount)
	{
		cin >> n;
		pc = new char[n * n];

		for(int i = 0; i < n; i++)
		{
			char s[256];
			cin >> s;
			memcpy(pc + i * n, s, n);
		}

		double* pOWP = new double[n];

		for(int i = 0; i < n; i++)
			pOWP[i] = calcOWP(i);

		cout << "Case #" << numCase << ": \n";

		for(int i = 0; i < n; i++)
		{
			char* ps = getteam(i);
			double d = 0;
			int t = 0;
			for(int j = 0; j < n; j++)
			{
				if(ps[j] != '.')
				{
					d += pOWP[j];
					t++;
				}
			}
			double OOWP = (t > 0 ? d / t : 0);

			double RPI = 0.25 * calcWP(i, -1) + 0.5 * calcOWP(i) + 0.25 * OOWP;

			printf("%.12f\n", RPI);
			//cout << RPI << "\n";
		}

		delete pOWP;
		delete pc;

		numCase++;
	}
	return 0;
}
