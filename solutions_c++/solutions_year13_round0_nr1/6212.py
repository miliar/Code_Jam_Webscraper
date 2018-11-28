// 2013codejam_1.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string map[4];


int solve()
{
	int i,j;
	int cnt=0;
	int x[4][4],o[4][4];

	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			x[i][j]=o[i][j]=0;
			if(map[i][j] == 'T')
			{
				x[i][j]++;
				o[i][j]++;
			}
			else if(map[i][j] == 'X')
				x[i][j]++;
			else if(map[i][j] == 'O')
				o[i][j]++;
			else cnt++;
		}
	}
	for(i=0;i<4;i++)
	{
		if(x[i][0]+x[i][1]+x[i][2]+x[i][3] == 4 || x[0][i] + x[1][i] + x[2][i] + x[3][i] == 4)
			return 1;
		else if(o[i][0]+o[i][1]+o[i][2]+o[i][3] == 4 || o[0][i] + o[1][i] + o[2][i] + o[3][i] == 4)
			return 2;
	}
	if(x[0][0] + x[1][1] + x[2][2] + x[3][3] == 4 || x[0][3] + x[1][2] + x[2][1]+ x[3][0] == 4)
		return 1;
	if(o[0][0] + o[1][1] + o[2][2] + o[3][3] == 4 || o[0][3] + o[1][2] + o[2][1]+ o[3][0] == 4)
		return 2;

	if( cnt == 0)
		return 3;

	return 4;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int n,i,j,k;
	ifstream ifs;
	ifs.open("input.txt");
	
	ofstream ofs;
	ofs.open("output.txt");

	ifs >> n;

	for(i=0;i<n;i++)
	{
		for(j=0;j<4;j++)
				ifs >> map[j];
		k= solve();

		if(k == 1)
			ofs << "Case #" << i+1 << ": X won" << endl;
		else if(k == 2)
			ofs << "Case #" << i+1 << ": O won" << endl;
		else if(k == 3)
			ofs << "Case #" << i+1 << ": Draw" << endl;			
		else if(k == 4)
			ofs << "Case #" << i+1 << ": Game has not completed" << endl;
	}
	return 0;
}

