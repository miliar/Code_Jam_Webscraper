// b.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>

using namespace std;

#define nmax 128

ifstream in;
int T, H, W;
int a[nmax][nmax];
char res[nmax][nmax], lastLetter;

int vx[] = {-1, 0, 0, 1};
int vy[] = {0, -1, 1, 0};

void Read()
{
	in >> H >> W;
	for(int i = 0; i <= H + 1; i++)
		for(int j = 0; j <= W + 1; j++)
			a[i][j] = -1;

	for(int i = 1; i <= H; i++)
		for(int j = 1; j <= W; j++)
			in >> a[i][j];
}

char drain(int x, int y)
{
	if(res[x][y] != '-')
		return res[x][y];

	int min = a[x][y];
	int dir = -1;
	for(int i = 0; i < 4; i++)
		if(a[vx[i] + x][vy[i] + y] != -1 && a[vx[i] + x][vy[i] + y] < min)
		{
			min = a[vx[i] + x][vy[i] + y];
			dir = i;
		}

	if(dir == -1)
	{
		lastLetter++;
		res[x][y] = lastLetter;
	}
	else 
		res[x][y] = drain(vx[dir] + x, vy[dir] + y);
	return res[x][y];
}

void SolveCase()
{
	Read();
	for(int i = 1; i <= H; i++)
		for(int j = 1; j <= W; j++)
			res[i][j] = '-';

	lastLetter = 'a' - 1;
	for(int i = 1; i <= H; i++)
		for(int j = 1; j <= W; j++)
			if(res[i][j] == '-')
				drain(i, j);

	for(int i = 1; i <= H; i++) {
		for(int j = 1; j <= W; j++)
		{
			cout << res[i][j];
			if(j != W) cout << " ";
		}
		cout << endl;
	}
}

int main()
{
	in.open("b.in");
	freopen("b.out", "w", stdout);
	in >> T;
	for(int t = 1; t <= T; t++)
	{
		cout << "Case #" << t <<":" << endl;
		SolveCase();
	}
	return 0;
}

