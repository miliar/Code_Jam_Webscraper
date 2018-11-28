#include <string>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdio>
#include <fstream>

using namespace std;

#define N 4

char pattern [N][N];
int T;

bool judge_row(int index, char player)
{
	for (int i=0; i<N; i++)
	{
		if (pattern[index][i] != player && 
			pattern[index][i] != 'T')
			return false;
	}
	return true;
}
bool judge_col(int index, char player)
{
	for (int i=0; i<N; i++)
	{
		if (pattern[i][index] != player &&
			pattern[i][index] != 'T')
			return false;
	}
	return true;
}
bool judge_cross(char player)
{
	for (int i=0; i<N; i++)
	{
		if (pattern[i][i] != player && 
			pattern[i][i] != 'T')
			return false;
	}
	return true;
}
bool judge_back_cross(char player)
{
	for (int i=0; i<N; i++)
	{
		if (pattern[i][N-i-1] != player && 
			pattern[i][N-i-1] != 'T')
			return false;
	}
	return true;
}
bool judge_win(char player)
{
	for (int i=0; i<N; i++)
	{
		if (judge_row(i, player) == true)
			return true;
		if (judge_col(i, player) == true)
			return true;
	}
	if (judge_cross(player) == true)
		return true;
	if (judge_back_cross(player) == true)
		return true;
	return false;
}
bool find_blank()
{
	for (int i=0; i<N; i++)
		for (int j=0; j<N; j++)
			if (pattern[i][j] == '.')
				return true;
	return false;
}
int main()
{
	ofstream fout;
	fout.open("A_small.txt");
	cin >> T;
	for (int cases = 1; cases<=T; cases++)
	{
		for (int i=0; i<N; i++)
			for (int j=0; j<N; j++)
				cin >> pattern[i][j];
		if (judge_win('X') == true)
		{
			fout << "Case #" << cases << ": X won\n";
		}
		else if (judge_win('O') == true)
		{
			fout << "Case #" << cases << ": O won\n";
		}
		else if (find_blank() == true)
		{
			fout << "Case #" << cases << ": Game has not completed\n";
		}
		else if (find_blank() == false)
		{
			fout << "Case #" << cases << ": Draw\n";
		}
		else
		{
			// should never be here ...
		}
	}
	fout.close();
	system("pause");
	return 1;
}