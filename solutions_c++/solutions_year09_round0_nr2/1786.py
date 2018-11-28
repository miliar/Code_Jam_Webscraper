
#include <stdio.h>
#include <string.h>
#include <queue>

using namespace std;

int flags[110][110];
int field[110][110];
int curDrain = 0 ;
int W, H;
int N;

int isSink(int i, int j)
{
	int r = 0;
	if (i > 0)
		r += (field[i][j] <= field[i-1][j]);
	else
		r++;
	if (i < H-1)
		r += (field[i][j] <= field[i+1][j]);
	else 
		r++;
	if (j > 0)
		r += (field[i][j] <= field[i][j-1]);
	else
		r++;
	if (j < W-1)
		r += (field[i][j] <= field[i][j+1]);
	else
		r++;
	return (r == 4);
}

int av(int i, int j)
{
	if (i < 0 || i >= H)
		return 0;
	if (j < 0 || j >= W)
		return 0;
	return 1;
}

pair<int, int> choice(int i, int j)
{
	pair<int, int> r = make_pair(i, j);
	if (av(i-1, j))
	{
		if (field[i-1][j] < field[r.first][r.second])
			r = make_pair(i-1, j);
	}
	if (av(i, j-1))
	{
		if (field[i][j-1] < field[r.first][r.second])
			r = make_pair(i, j-1);
	}
	if (av(i, j+1))
	{
		if (field[i][j+1] < field[r.first][r.second])
			r = make_pair(i, j+1);
	}
	if (av(i+1, j))
	{
		if (field[i+1][j] < field[r.first][r.second])
			r = make_pair(i+1, j);
	}
	return r;
}

int flows(int i, int j, int i1, int j1)
{
	if (!av(i1, j1))
		return 0;
	return (make_pair(i, j) == choice(i1, j1));
}

void findDrain(int i, int j)
{
	queue<pair<int, int>> q;

	q.push(make_pair(i, j));
	while (!q.empty())
	{
		pair<int, int> t = q.front();
		flags[t.first][t.second] = curDrain;
		if (flows(t.first, t.second, t.first - 1, t.second))
			q.push(make_pair(t.first - 1, t.second));
		if (flows(t.first, t.second, t.first + 1, t.second))
			q.push(make_pair(t.first + 1, t.second));
		if (flows(t.first, t.second, t.first, t.second - 1))
			q.push(make_pair(t.first, t.second - 1));
		if (flows(t.first, t.second, t.first, t.second + 1))
			q.push(make_pair(t.first, t.second + 1));
		q.pop();
	}
}

void rename(int n, int m, int newN)
{
	int v = flags[n][m];
	for (int i=0;i<H;i++)
	{
		for (int j = 0; j < W; j++)
		{
			if (flags[i][j] == v)
				flags[i][j] = newN+26;
		}
	}
}

void solve()
{
	curDrain = 0;
	memset(flags, -1, sizeof(flags));
	
	for (int i=0;i<H;i++)
	{
		for (int j = 0; j < W; j++)
		{
			if ((flags[i][j] == -1) && isSink(i, j))
			{
				findDrain(i,j);
				curDrain++;
			}
		}
	}
	//rename properly
	int drain = 0;
	for (int i=0;i<H;i++)
	{
		for (int j = 0; j < W; j++)
		{
			if (flags[i][j] < 26)
			{
				rename(i, j, drain);
				drain++;
			}
		}
	}
}

int main()
{
	FILE *fp=fopen("B-large.in","rt");
	FILE *fpo=fopen("output.out","wt");
	fscanf(fp, "%d" , &N);
	for (int i = 0;i<N;i++)
	{
		fscanf(fp, "%d%d", &H, &W);
		for (int j = 0; j < H; j++)
		{
			for (int k = 0; k < W; k++)
			{
				fscanf(fp,"%d", &field[j][k]);
			}
		}
		solve();
		fprintf(fpo,"Case #%d:\n", i+1);
		for (int j = 0; j < H; j++)
		{
			for (int k = 0; k < W; k++)
				fprintf(fpo,"%c ", flags[j][k]+'a'-26);
			fprintf(fpo,"\n");
		}
	}
	fclose(fp);
	fclose(fpo);
}
