#include "MatchHead.h"
#ifdef TTTT

#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
using namespace std;

char check(char board[4][4])
{
	char t;
	for( int i = 0; i < 4; i ++)
	{
		t = board[i][0];
		if(t == 'T') t = board[i][1];
		if(board[i][1] == 'T' || board[i][1] == t)
		{
			if(board[i][2] == 'T' || board[i][2] == t)
			{
				if(board[i][3] == 'T' || board[i][3] == t)
				{
					if(t == 'X' || t == 'O')
						return t;
				}
			}
		}
	}
	for( int i = 0; i < 4; i ++)
	{
		t = board[0][i];
		if(t == 'T') t = board[1][i];
		if(board[1][i] == 'T' || board[1][i] == t)
		{
			if(board[2][i] == 'T' || board[2][i] == t)
			{
				if(board[3][i] == 'T' || board[3][i] == t)
				{
					if(t == 'X' || t == 'O')
						return t;
				}
			}
		}
	}
	t = board[0][0];
	if(t == 'T') t = board[1][1];
	if(board[1][1] == 'T' || board[1][1] == t)
	{
		if(board[2][2] == 'T' || board[2][2] == t)
		{
			if(board[3][3] == 'T' || board[3][3] == t)
			{
				if(t == 'X' || t == 'O')
					return t;
			}
		}
	}
	t = board[0][3];
	if(t == 'T') t = board[1][2];
	if(board[1][2] == 'T' || board[1][2] == t)
	{
		if(board[2][1] == 'T' || board[2][1] == t)
		{
			if(board[3][0] == 'T' || board[3][0] == t)
			{
				if(t == 'X' || t == 'O')
					return t;
			}
		}
	}
	return 0;
}

int main(int argc, char* argv[])
{
	ifstream in;
	ofstream out;
	in.open("A-small-attempt0.in");
	out.open("A-small-attempt0.out");
	string snum;
	int num;
	getline(in, snum);
	sscanf(snum.c_str(),"%d", &num);
	string str;
	char board[4][4];
	bool complete;
	char result;
	for(int l = 0; l < num; l ++)
	{
		complete = true;
		result = 0;
		for(int i = 0; i < 4; i ++)
		{
			getline(in, str);
			for(int j = 0; j < 4; j ++)
			{
				board[i][j] = str[j];
				if(board[i][j] == '.') complete = false;
			}
		}
		result = check(board);
		if(result == 'X' || result == 'O')
			out << "Case #" << l+1 << ": " <<  result << " won" << endl;
		else
		{
			if(complete)
				out << "Case #" << l+1 << ": " << "Draw" << endl;
			else
				out << "Case #" << l+1 << ": " << "Game has not completed" << endl;
		}
		getline(in, str);
	}
	in.close();
	out.close();
	return 0;
}

#endif