#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

//istream& fin = cin;
//ifstream fin ("A-sample.txt");
//ifstream fin ("A-small-attempt0.in");
//ofstream fout ("A-small-attempt0.out");
ifstream fin ("A-large.in");
ofstream fout ("A-large.out");
//ostream& fout = cout;

char map[4][4];
bool allFill;

bool checkRow(char sym, int k)
{
	for(int i=0; i<4; i++)
	{
		if(map[k][i]!=sym && map[k][i]!='T')
			return false;
	}
	return true;
}

bool checkCol(char sym, int k)
{
	for(int i=0; i<4; i++)
	{
		if(map[i][k]!=sym && map[i][k]!='T')
			return false;
	}
	return true;
}

bool checkDia1(char sym)
{
	for(int i=0; i<4; i++)
	{
		if(map[i][i]!=sym && map[i][i]!='T')
			return false;
	}
	return true;
}

bool checkDia2(char sym)
{
	for(int i=0; i<4; i++)
	{
		if(map[i][3-i]!=sym && map[i][3-i]!='T')
			return false;
	}
	return true;
}

bool checkWin(char sym)
{
	for(int i=0; i<4; i++)
	{
		if(checkRow(sym,i))
			return true;
		if(checkCol(sym,i))
			return true;
	}
	if(checkDia1(sym))
		return true;
	if(checkDia2(sym))
		return true;
	return false;
}

inline void core(int n)
{
	if(checkWin('X'))
		fout << "Case #" << n << ": X won" << endl;
	else if(checkWin('O'))
		fout << "Case #" << n << ": O won" << endl;
	else if(allFill)
		fout << "Case #" << n << ": Draw" << endl;
	else
		fout << "Case #" << n << ": Game has not completed" << endl;
}

int main()
{
	int N;
	fin >> N;
	for(int n=1; n<=N; n++)
	{
		allFill = true;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
			{
				fin >> map[i][j];
				if(map[i][j]=='.')
					allFill = false;
			}
			
		core(n);
	}
	
	return 0;
}

