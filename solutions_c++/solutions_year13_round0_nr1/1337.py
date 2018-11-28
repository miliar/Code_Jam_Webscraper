#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>


using namespace std;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int testnum;
	in >> testnum;

	int d[4][4] = {0};
	string s;
	for (int testcase = 1; testcase <= testnum; testcase++)
	{

		getline(in, s);
		for (int i = 0; i < 4; i++)
		{
			getline(in, s);
			for (int j = 0; j < 4; j++)
			{
				if (s[j] == 'X')
					d[i][j] = 1;
				else if (s[j] == 'O')
					d[i][j] = 10;
				else if (s[j] == 'T')
					d[i][j] = 100;
				else
					d[i][j] = 0;
			}
		}


		int res = -1, count = 0;
		//row
		for (int j = 0; j < 4; j++)
		{
			int cur = 0;
			for (int i = 0; i < 4; i++)
				if (d[i][j] > 0)
				{
					cur += d[i][j];
					count++;
				}
			if (cur == 4 || cur == 103)
				res = 1;
			else if (cur == 40 || cur == 130)
				res = 2;
		}
		//column
		for (int i = 0; i < 4; i++)
		{
			int cur = 0;
			for (int j = 0; j < 4; j++)
					cur += d[i][j];

			if (cur == 4 || cur == 103)
				res = 1;
			else if (cur == 40 || cur == 130)
				res = 2;
		}
		//diag
		int c1 = 0, c2 = 0;
		for (int i = 0; i < 4; i++)
		{
			c1 += d[i][i];
			c2 += d[i][3-i];
		}
		if (c1 == 4 || c1 == 103 || c2 == 4 || c2 == 103)
				res = 1;
			else if (c1 == 40 || c1 == 130 || c2 == 40 || c2 == 130)
				res = 2;

		if (res == -1 && count == 16)
			res = 0;
		
		out << "Case #" << testcase << ": ";
		if (res == -1)
			out << "Game has not completed" << endl;
		else
		if (res == 0)
			out << "Draw" << endl;
		else
		if (res == 1)
			out << "X won" << endl;
		else
		if (res == 2)
			out << "O won" << endl;
	}
	return 0;
}

