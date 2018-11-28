#include <map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;
ifstream inf;
ofstream outf;
#define FOR(i,a,b) for(int _b=(b),i=(a);i<=_b;i++)
#define FORD(i,a,b) for(int _b=(b),i=(a);i>=_b;i--)


		int n, k;
		string a[66];
int ok(int x)
{
	return (x >= 0) && (x < n);
}
int solve (char c)
{
	int dx[4] = {0, 1, 1, 1};
	int dy[4] = {1, 0, 1, -1};
	for(int z = 0; z < 4; z++)
	for(int x = 0; x < n; x++)
		for(int y = 0; y < n; y++)
		{
			int fl = 0;
			for (int p = 0; p < k; p++)
			{
				int nx = x + p * dx[z];
				int ny = y + p * dy[z];
				if (ok(nx) && ok(ny) && (a[nx][ny] == c))
					fl = fl;
				else
					fl = 1;
			}
			if(fl == 0)
				return 1;
		}

		return 0;
}
int main(void){
	//freopen("input.txt","rt",stdin);
	//freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	int tests;
	inf >> tests;

 	for(int test = 0; test < tests; test++)
	{
		int anw = 0;

		inf >> n >> k;
		for (int i = 0; i < n; i++)
			inf >> a[i];
		for (int i = 0; i < n; i++)
		{
			string nw = a[i];
			for(int j = 0; j < n; j++)
				nw[j] = '.';
			int ind = n - 1;
			for(int j = n - 1; j >= 0; j--)
				if (a[i][j] != '.')
					nw[ind--] = a[i][j];
			a[i] = nw;
		}
			
		int rw = solve('R');
		int bw = solve('B');
		string slv;
		if (bw)
		{
			if (rw)
				slv = "Both";
			else 
				slv = "Blue";
		}
		else
		{
			if (rw)
				slv = "Red";
			else 
				slv = "Neither";
		}



		outf << "Case #"  << test+1 << ": " ;
		outf <<  slv << endl;
		
	}
	
	outf.close();
	return 0;
}
