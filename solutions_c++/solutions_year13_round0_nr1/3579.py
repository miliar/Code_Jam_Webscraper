#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");


char vals[4][4];

int idx(char c)
{
	if(c=='X')
		return 0;
	else if(c=='O')
		return 1;
	else if(c=='T')
		return 2;
	else return 3;
}


int ret;

int res(char a, char b, char c, char d)
{
	int curr[4];
	
	for(int i=0; i<4; i++)
		curr[i]=0;
	
	curr[idx(a)]++;
	curr[idx(b)]++;
	curr[idx(c)]++;
	curr[idx(d)]++;
	
	if(curr[0]+curr[2]==4)
		return -1;
	else if(curr[1]+curr[2]==4)
		return 0;
	return 1;
}

void solve(char a, char b, char c, char d)
{
	int x= res(a,b,c,d);
	if(x==0 || x==-1)
		ret=x;
	return;
}
	
	

int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	cout.precision(9);
	fout.precision(9);
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int i,j,k;
		
		
		int countx, counto,countt, countd;
		
		countx=counto=countt=countd=0;
		
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				fin >> vals[i][j];
				if(vals[i][j]=='.')
				{
					countd++;
				}
				else if(vals[i][j]=='X')
				{
					countx++;
				}
				else if(vals[i][j]=='O')
					counto++;
				else if(vals[i][j]=='T')
					countt++;
				else {
					cout << "FAIL TO RECOGNISE " << vals[i][j] << endl;
				}
			}
		}
		
		ret = -2;
		
		for(i=0; i<4; i++)
		{
			solve(vals[i][0],vals[i][1],vals[i][2],vals[i][3]);
			solve(vals[0][i],vals[1][i],vals[2][i],vals[3][i]);
		}
		solve(vals[0][0],vals[1][1],vals[2][2],vals[3][3]);
		solve(vals[3][0],vals[2][1],vals[1][2],vals[0][3]);
		
		
		
		
		
		cout << "Case #" << ct << ": ";
		fout << "Case #" << ct << ": ";
		
			
		string xwon = "X won";
		string owon = "O won";
		string draw = "Draw";
		string incomp = "Game has not completed";
		
		if(ret==-1)
		{
			cout << xwon;
			fout << xwon;
		}
		else if(ret==0)
		{
			cout << owon;
			fout << owon;
		}
		else if(countd==0)
		{
			cout << draw;
			fout << draw;
		}
		else {
			cout << incomp;
			fout << incomp;
		}

		
	
		
		
		
		fout << endl;
		cout << endl;
		
	}
	
	
	return 0;
}

