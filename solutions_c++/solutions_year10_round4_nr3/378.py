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



long long dp [2200][15][15];
long long m[2200];
long long pr[15][2200];
int main(void){
	
	//freopen("input.txt","rt",stdin);
	//freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	int tests;
	inf >> tests;

 	for(int test = 0; test < tests; test++)
	{
		int  anw = 0;
		int r, x1,y1,x2,y2;
		inf >> r;
		int mx = 210;
		int st[2][230][230];
		memset(st, 0, sizeof(st));
		for(int i = 0; i < r; i++)
		{
			inf >> x1 >> y1 >> x2 >> y2;
			for(int x = x1; x <= x2; x++)
				for(int y =y1; y <= y2; y++)
					st[0][x][y] = 1;
		}
		anw = 0;
		int step = 0;
		while(true)
		{
			int bre = 0;
			for(int x = 1; x < mx; x++)
				for(int y = 1; y < mx; y++)
				{

					if(st[step][x][y]) // est
						if((!st[step][x - 1][y]) && (!st[step][x][y - 1]))
							st[step ^ 1][x][y] = 0;
						else
							st[step ^ 1][x][y] = 1;
					else
						// pustaya
						if(st[step][x - 1][y] && st[step][x][y - 1])
							st[step ^ 1][x][y] = 1;
						else
							st[step ^ 1][x][y] = 0;
					if (st[step ^ 1][x][y])
						bre++;
				}
			if (bre == 0)
				break;
			step = step ^ 1;
			anw++;
		}

		
	




		outf << "Case #"  << test+1 << ": " ;
		outf <<  anw + 1 << endl;
		
	}
	
	outf.close();
	return 0;
}
