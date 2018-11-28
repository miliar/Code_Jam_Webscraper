// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

bool IsPalindrome(long long n)
{
	long long temp = n;
	long long invn = 0;
	while (temp)
	{
		invn = 10 * invn + temp % 10;
		temp /= 10;
	}
	if (n == invn)
		return true;
	return false;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream ifstr("A-large.in");
	ofstream ofstr("A-large.out");

	int T;
	ifstr >> T;
	for (int t = 0; t < T; ++t)
	{
		vector<string> field(4);
		for (int i = 0; i < 4; ++i)
			ifstr >> field[i];
		for (int i = 0; i < 4; ++i)
		{
			string column;
			for (int j = 0; j < 4; ++j)
			{
				column += field[j][i];
			}
			field.push_back(column);
		}
		string diag, invdiag;
		for (int i = 0; i < 4; ++i)
		{
			diag += field[i][i];
			invdiag += field[3 - i][i];
		}
		field.push_back(diag);
		field.push_back(invdiag);

		set<string> lines;

		vector<string> linesX = field;
		for (int i = 0; i < linesX.size(); ++i)
			replace(linesX[i].begin(), linesX[i].end(), 'T', 'X');
		lines.insert(linesX.begin(), linesX.end());

		vector<string> linesO = field;
		for (int i = 0; i < linesO.size(); ++i)
			replace(linesO[i].begin(), linesO[i].end(), 'T', 'O');
		lines.insert(linesO.begin(), linesO.end());

		bool hasDot = false;
		for (int i = 0; i < field.size(); ++i)
			if (find(field[i].begin(), field[i].end(), '.') != field[i].end())
			{
				hasDot = true;
				break;
			}

		string result;

		if (lines.find("XXXX") != lines.end())
			result = "X won";
		else if (lines.find("OOOO") != lines.end())
			result = "O won";
		else if (hasDot)
			result = "Game has not completed";
		else
			result = "Draw";

		ofstr << "Case #" << t + 1 << ": " << result << endl;
	}

	return 0;
}

