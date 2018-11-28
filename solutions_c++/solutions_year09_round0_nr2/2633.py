#include <iostream>
#include <string>
#include <fstream>
 
using namespace std;
 
#define MAX_H	100;
#define MAX_W	100;
 
ifstream fin("B-large.in");
ofstream fout("B-large.out");
 
#define cin fin
#define cout fout
 
int map[100][100] = {0};
char mark[100][100] = {0};
 
int W;
int H;
 
char ch_mark;
 
int rec_mark(int r, int c)
{
	if (mark[r][c] != 0)
	{
		return mark[r][c];
	}
	else
	{
		// Calculate diff of altitude
		int up, left, right, down;
		up = left = right = down = -1;
		if (r > 0)
		{
			up = map[r][c] - map[r-1][c];
		}
		if (c > 0)
		{
			left = map[r][c] - map[r][c-1];
		}
		if (c < W - 1)
		{
			right = map[r][c] - map[r][c+1];
		}
		if (r < H - 1)
		{
			down = map[r][c] - map[r+1][c];
		}
		if (up <= 0 && left <= 0 && right <= 0 && down <= 0)
		{
			// Sink
			mark[r][c] = ch_mark;
			ch_mark++;
		}
		else
		{
			// Find the flow direction
			int max_diff = up;
			int dr = -1; int dc = 0;
			if (left > max_diff)
			{
				max_diff = left;
				dr = 0; dc = -1;
			}
			if (right > max_diff)
			{
				max_diff = right;
				dr = 0; dc = 1;
			}
			if (down > max_diff)
			{
				dr = 1; dc = 0;
			}
			if (mark[r + dr][c + dc] != 0)
			{
				mark[r][c] = mark[r + dr][c + dc];
			}
			else
			{
				mark[r][c] = rec_mark(r + dr, c + dc);
			}
		}
		return mark[r][c];
	}
}
 
int main()
{
	int N;
	cin >> N;
 
	for (int n = 0; n < N; ++n)
	{
		ch_mark = 'a';
		int a;
		cin >> H >> W;
		for (int i = 0; i < H; ++i)
		{
			for (int j = 0; j < W; ++j)
			{
				cin >> a;
				map[i][j] = a;
				mark[i][j] = 0;
			}
		}
		// Look for next cell to eval
		for (int r = 0; r < H; r++)
		{
			for (int c = 0; c < W; c++)
			{
				if (mark[r][c] == 0)
				{
					rec_mark(r, c);
				}
			}
		}
		cout << "Case #" << n + 1 << ":" << endl;
		for (int r = 0; r < H; r++)
		{
			for (int c = 0; c < W; c++)
			{
				cout << mark[r][c] << ' ';
			}
			cout << endl;
		}
	}
	return 0;
}
