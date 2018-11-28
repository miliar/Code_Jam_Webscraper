#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

ifstream fin ("A.in");
ofstream fout ("A.txt");

char val[4][4];

bool full()
{
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (val[i][j] == '.')
				return false;
	return true;
}

bool win (char ch)
{
	for (int i = 0; i < 4; i++)
	{
		bool check = true;
		for (int j = 0; j < 4; j++)
			if (val[i][j] != ch && val[i][j] != 'T')
				check = false;
		if (check) return true;
		
		check = true;
		for (int j = 0; j < 4; j++)
			if (val[j][i] != ch && val[j][i] != 'T')
				check = false;
		if (check) return true;
	}
	
	bool check = true;
	for (int j = 0; j < 4; j++)
		if (val[j][j] != ch && val[j][j] != 'T')
			check = false;
	if (check) return true;
	
	check = true;
	for (int j = 0; j < 4; j++)
		if (val[j][3-j] != ch && val[j][3-j] != 'T')
			check = false;
	if (check) return true;
	
	return false;
}

int main()
{
	int T; fin >> T;
	
	for (int test = 1; test <= T; test++)
	{
	
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			fin >> val[i][j];
	
	fout << "Case #" << test << ": ";
	
	if (win ('X'))
		fout << "X won\n";
	else if (win ('O'))
		fout << "O won\n";
	else if (full())
		fout << "Draw\n";
	else
		fout << "Game has not completed\n";
	
	}
	
	return 0;
}
	
