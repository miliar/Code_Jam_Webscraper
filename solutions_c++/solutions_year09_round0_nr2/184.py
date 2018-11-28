#include "stdafx.h"

#include <fstream>
using namespace std;

char m[102][102];
int a[102][102];

int dx[4] = {0,-1,1,0};
int dy[4] = {-1,0,0,1};
char nextChar;

void calcSquare(int row, int col)
{
	if (m[row][col] <= 'z')
		return;

	int lowest = a[row][col], loc = -1;
	for (int i=0; i<4; ++i)
		if (a[row+dy[i]][col+dx[i]] < lowest) {
			loc = i; lowest = a[row+dy[i]][col+dx[i]]; }

	if (loc == -1) {
		m[row][col] = nextChar++; return; }

	calcSquare(row+dy[loc],col+dx[loc]);
	m[row][col] = m[row+dy[loc]][col+dx[loc]];
}

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	int T,H,W; // T is number, H is height, W is width
	fin >> T;

	for (int z=1; z<=T; ++z)
	{
		nextChar = 'a';
		memset(m, 'z'+1, sizeof(m));
		memset(a, 1, sizeof(a)); //produce some large positive value...
		fin >> H >> W;
		for (int i=1; i<=H; ++i)
			for (int j=1; j<=W; ++j)
				fin >> a[i][j];
		
		fout << "Case #" << z << ": "<< endl;
		for (int i=1; i<=H; ++i)
		{
			for (int j=1; j<=W; ++j) {
				calcSquare(i,j); fout << m[i][j] << " "; }
			fout << endl;
		}
	}

	return 0;
}

