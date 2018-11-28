#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <fstream>
using namespace std;

int main( )
{
	int t, tt;

	ifstream fin("a.in");
	ofstream fout("a.out");

	fin >> tt;
	for( t = 1; t <= tt; ++ t )
	{
		int n;
		fin >> n;
		int ** pos = new int*[n];
		for (int i=0; i<n; i++)
			pos[i] = new int[n];
		for (int i=0; i<n; i++)
		{
			string s;
			fin >> s;
			for (int j=0; j<n; j++)
			{
				if (s[j] == '1')
					pos[i][j] = 1;
				if (s[j] == '0')
					pos[i][j] = 0;
				if (s[j] == '.')
					pos[i][j] = -1;
			}
		}
		double *wp = new double[n];
		double *owp = new double[n];
		double *oowp = new double[n];
		for (int i=0; i<n; i++)
		{
			wp[i] = 0;
			owp[i] = 0;
			oowp[i] = 0;
		}
		for (int i=0; i<n; i++)
		{
			int wc = 0;
			int ac = 0;
			for (int j=0; j<n; j++)
				if (pos[i][j]>=0)
				{
					ac++;
					if (pos[i][j]==1)
						wc++;
				}
				wp[i] = (double)wc/ac;
		}
		for (int i=0; i<n; i++)
		{
			int pc = 0;
			double swp = 0;
			for (int j=0; j<n; j++)
			{
				if (pos[i][j]>=0)
				{
					pc++;
					int ac = 0;
					int wc = 0;
					double as = 0;
					for (int k=0; k<n; k++)
					{
						if (k!=i && pos[j][k]>=0)
						{
							ac++;
							if (pos[j][k]==1)
								wc++;
						}
					}
					swp += (double) wc/ac;
				}
			}
			owp[i] = swp/pc;
		}

		for (int i=0; i<n; i++)
		{
			int pc = 0;
			double sowp = 0;
			for (int j=0; j<n; j++)
				if (pos[i][j]>=0)
				{
					pc++;
					sowp += owp[j];
				}
			oowp[i] = sowp/pc;
		}

		fout.precision(10);
		fout << "Case #" << t << ":" << endl;
		for (int i=0; i<n; i++)
			fout << (0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]) << endl;

	}

	return 0;
}
