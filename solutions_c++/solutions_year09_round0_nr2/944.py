#include <map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;
ifstream inf;
ofstream outf;
#define FOR(i,a,b) for(int _b=(b),i=(a);i<=_b;i++)
#define FORD(i,a,b) for(int _b=(b),i=(a);i>=_b;i--)

char tmpb[100000];
int dp [600][600];
const int modd = 10000;
int basin [200][200];
int res [200][200];
int h, w, idd;
//North, West, East, South.
int dx[4] = {0, -1, 1, 0};
int dy[4] = {-1, 0, 0, 1};
void go(int x, int y)
	{
		if (res[y][x] != 0)
			return;
		//outf << x << " - " << y << ": " << basin[y][x]<<endl;
		int best = basin[y][x];
		int besti = -1;
		int nx, ny;
		for(int i = 0; i < 4; i++)
		{
			nx = x + dx[i];
			ny = y + dy[i];
			if (nx < 0  || ny < 0 || nx >= w || ny >= h)
				continue;
			if (basin[ny][nx] < basin[y][x])
			{
				go(nx, ny);
				if (best >  basin[ny][nx])
				{
				best = basin[ny][nx];
				besti = i;
				}
			}

		}
		if (besti != -1) 
		{
			nx = x + dx[besti];
			ny = y + dy[besti];
			res[y][x] = res[ny][nx];
		}
		else
		{
			res[y][x] = idd++;
		}
		

		return;
	}
int main(void){
	//freopen("input.txt","rt",stdin);
	//freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	
	int tests;
	inf  >> tests;

	for(int test = 0; test < tests; test++)
	{

		inf >> h >> w;
		for(int i = 0; i < h; i++)
			for(int j = 0; j <  w; j++)
			{
				inf >> basin[i][j];
				res[i][j] = 0;
			}
		
		idd = 1;
		for(int i = 0; i < h; i++)
			for(int j = 0; j <  w; j++)
				go(j , i);
		map<int,char> ma;
		ma.clear();
		char cur = 'a';
		for(int i = 0; i < h; i++)
			for(int j = 0; j <  w; j++)
			{
				
				if (ma[res[i][j]] == 0)
					ma[res[i][j]] = cur++;
		/*
				int t = res[i][j];
				if (ma[t] == 0)
					ma[t] = cur++;
		*/	
			}




		
	   
		
		outf << "Case #"  << test+1 << ":"  << endl;
		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j <  w; j++)
			{
				outf << ma[res[i][j]];
				if (j != w - 1) outf << " ";
			}
			outf << endl;
		}

	}
	
	outf.close();
	return 0;
}
