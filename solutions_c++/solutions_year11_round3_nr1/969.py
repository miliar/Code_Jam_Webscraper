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
		int r, c;
		fin >> r >> c;
		
		int **a = new int*[r];
		for (int i=0; i<r; i++)
		{
			string s;
			fin >> s;
			a[i] = new int[c];
			for (int j=0; j<c; j++)
				if (s[j]=='#')
					a[i][j] = 1;
				else
					a[i][j] = 0;
		}

		for (int i=0; i<r-1; i++)
			for (int j=0; j<c-1; j++)
				if (a[i][j]==1 && a[i][j+1]==1 && a[i+1][j]==1 && a[i+1][j+1]==1)
				{
					a[i][j] = a[i+1][j+1] = 2;
					a[i+1][j] = a[i][j+1] = 3;
				}

		bool ok = true;
		for (int i=0; i<r; i++)
		{
			for (int j=0; j<c; j++)
				if (a[i][j]==1)
				{
					ok = false;
					break;
				}
		}
		fout << "Case #" << t << ":" << endl;
		if (!ok)
		{
			fout << "Impossible" << endl;
		}
		else
		{
			for (int i=0; i<r; i++)
			{
				for (int j=0; j<c; j++)
				{
					if (a[i][j] == 0)
						fout << ".";
					if (a[i][j] == 2)
						fout << "/";
					if (a[i][j] == 3)
						fout << "\\";
				}
				fout << endl;
			}
		}
	}

	return 0;
}
