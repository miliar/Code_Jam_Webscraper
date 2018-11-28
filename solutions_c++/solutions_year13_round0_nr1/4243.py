// Test.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

string winner(char c)
{
	string res;
	res += c;
	res += " won";
	return res;
}


string calc (const vector<string> &a)
{
	for (int i = 0; i < 4; ++i)
	{
		int j = 0;
		char c = a[i][j];
		if (c == 'T')
			c = a[i][++j];
		for (; j < 4 && (a[i][j] == c || a[i][j] == 'T'); ++j);
		if (j == 4 && c != '.') {
			return winner(c);
		}
	}

	for (int j = 0; j < 4; ++j)
	{
		int i = 0;
		char c = a[i][j];
		if (c == 'T')
			c = a[++i][j];
		for (; i < 4 && (a[i][j] == c || a[i][j] == 'T'); ++i);
		if (i == 4 && c != '.')
			return winner(c);
	}

	{
		int i = 0, j = 0;
		char c = a[i][j];
		if (c == 'T')
			c = a[++i][++j];
		for (; i < 4 && (a[i][j] == c || a[i][j] == 'T'); ++i, ++j);
		if (i == 4 && c != '.')
			return winner(c);
	}

	{
		int i = 0, j = 3;
		char c = a[i][j];
		if (c == 'T')
			c = a[++i][--j];
		for (; i < 4 && (a[i][j] == c || a[i][j] == 'T'); ++i, --j);
		if (i == 4 && c != '.')
			return winner(c);
	}

	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			if (a[i][j] == '.')
				return "Game has not completed";

	return "Draw";
}

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int c = 0; c < numCases; ++c) 
	{
		vector<string> a(4);
		for (int i = 0; i < 4; ++i)
			cin >> a[i];

		string res = calc(a);

		cout << "Case #" << c+1 << ": " << res << endl;
	}

	return 0;
}

