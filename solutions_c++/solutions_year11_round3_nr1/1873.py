#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <strstream>
#include <math.h>
#include <stdio.h>
#include <conio.h>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int nTestCases;
int caseNumber;
int R;
int C;
char tiles[55][55];

char sets(char top, char left)
{
	if (top=='.' && left=='.')
	{
		return '1';
	}
	if (left=='1')
		return '2';
	if (top=='1')
		return '3';
	if (top=='2' && left=='3')
		return '4';
	return '1';
}

void Process()
{
	char top;
	char left;
	bool impossible = false;
	for (int row=0; row<R; row++)
		tiles[row][C] = '.';
	for (int col=0; col<C; col++)
		tiles[R][C-1] = '.';
	for (int row=0; row<R; row++)
	{
		for (int col=0; col<C; col++)
		{
			char c = tiles[row][col];
			if (c=='.')
				continue;
			impossible = false;
			if (row==0)
				top='.';
			else
				top = tiles[row-1][col];
			if (col==0)
				left='.';
			else
				left = tiles[row][col-1];
			c = tiles[row][col] = sets(top, left);
		}
	}
	for (int row=0; row<R; row++)
	{
		for (int col=0; col<C; col++)
		{
			char c=tiles[row][col];
			if (c=='1')
			{
				bool valid = 
					tiles[row][col+1]=='2' && 
					tiles[row+1][col]=='3' && 
					tiles[row+1][col+1]=='4';
				if (!valid)
				{
					cout << "Impossible" << endl;
					return;
				}
			}
		}
	}
	for (int row=0; row<R; row++)
	{
		for (int col=0; col<C; col++)
		{
			if (tiles[row][col]=='1' || tiles[row][col]=='4')
				tiles[row][col] = '/';
			if (tiles[row][col]=='2' || tiles[row][col]=='3')
				tiles[row][col] = '\\';
			cout << tiles[row][col];
		}
		cout << endl;
	}

}


int main()
{
	string file1;
	string file2;
	file1 = "e:\\A-small-attempt0.in";
	//file1 = "e:\\zin.txt";
	file2 = "e:\\z2.out";
	FILE * ps;
	freopen_s(&ps, file1.c_str(), "rt", stdin);
	// comment this line for console output:
	freopen_s(&ps, file2.c_str(), "wt", stdout);

	scanf("%d", &nTestCases);
	for (int caseNumber=1; caseNumber<=nTestCases; caseNumber++)
	{
		cin >> R;
		cin >> C;
		string s;
		for (int i=0; i<R; i++)
		{
			cin >> s;
			for (int j=0; j<C; j++)
			{
				tiles[i][j] = s[j];
			}
		}
		cout << "Case #" << caseNumber << ": " << endl;
		Process();
		//cout << d << endl;
	}
	return 0;
}
