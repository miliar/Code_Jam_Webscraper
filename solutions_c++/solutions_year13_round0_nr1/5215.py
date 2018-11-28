// round0.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;

bool iswon(vector<string> v, char c)
{
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		if (v[i][j] == 'T')
		{
			v[i][j] = c;
			break;
		}
	}
	for (int i = 0; i < 4; i++)
	{
		if (v[i][0] == c && v[i][1] == c && v[i][2] == c && v[i][3] == c) return true;
		if (v[0][i] == c && v[1][i] == c && v[2][i] == c && v[3][i] == c) return true;
	}
	if (v[0][0] == c && v[1][1] == c && v[2][2] == c && v[3][3] == c) return true;
	if (v[0][3] == c && v[1][2] == c && v[2][1] == c && v[3][0] == c) return true;
	return false;
}

string ttt(vector<string>& v)
{
	if (iswon(v, 'X')) return "X won";
	if (iswon(v, 'O')) return "O won";
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (v[i][j] == '.') return "Game has not completed";
	return "Draw";
}

int main(int argc, char* argv[])
{
	ifstream in("A-large.in");
	ofstream out("output.txt");
	string line;

	getline(in, line);
	int T = atoi(line.c_str());
	for (int i = 0; i < T; i++)
	{
		vector<string> v;
		for (int j = 0; j < 4; j++)
		{
			getline(in, line);
			v.push_back(line);
		}
		getline(in, line);
		out << "Case #" << i+1 << ": " << ttt(v) << endl;
	}
	return 0;
}

