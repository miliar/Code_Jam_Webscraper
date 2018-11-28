#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

#define MAX 200

int matrix[MAX][MAX];

void swap(int& x, int& y)
{
	int t = x; x = y; y = t;
}

int good(int r, int c)
{
	if (r < 0 || c < 0) return 0;
	return matrix[r][c];
}

void print();

int iter()
{
	int mat[MAX][MAX] = {0};
	for(int i=0; i < MAX; i++)
	for(int j=0; j < MAX; j++)
	{
		if (!good(i-1,j) && !good(i,j-1))
			mat[i][j] = 0;
		else if (good(i-1,j) && good(i,j-1))
			mat[i][j] = 1;
		else
			mat[i][j] = matrix[i][j];
	}
	int ret = 0;
	for(int i=0; i < MAX; i++)
	for(int j=0; j < MAX; j++)
	{
		ret += mat[i][j];
		matrix[i][j] = mat[i][j];
	}
	//cout << "iter:\n";
	//print();
	return ret;
}

void print()
{
	for(int i=1; i < 6; i++)
	{
	for(int j=1; j < 6; j++)
		cout << matrix[i][j] << " ";
	cout << endl;
	}
}

void solve()
{
	memset(matrix, 0, sizeof matrix);
	int ret=0;
	int nbox; cin >> nbox;
	for(int ibox=0; ibox < nbox; ibox++)
	{
		int x1,y1,x2,y2; cin >> x1 >> y1 >> x2 >> y2;
		//cout << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
		if (x1 > x2) swap(x1,x2);
		if (y1 > y2) swap(y1,y2);

		for(int y=y1; y <= y2; y++)
		for(int x=x1; x <= x2; x++)
			matrix[y][x] = 1;
	}
	//print();
	while(iter())
		ret++;
	cout << (ret+1) << endl;
}

int main()
{
	int ncase; cin >> ncase;
	for(int icase=0; icase < ncase; icase++)
	{
		cout << "Case #" << (icase+1) << ": ";
		solve();
	}
}
