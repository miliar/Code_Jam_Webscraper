#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>

using namespace std;

const int MaxN = 60;

int diamond[MaxN*2][MaxN*2];
int runs, N, NN;

bool checkCenter(int dx, int dy)
{
	dx += N-1;
	dy += N-1;

	for (int i = 0; i < NN; ++i)
		for (int j = 0; j < NN; ++j)
		{
			int i1, j1;
			i1 = 2*dx - i;
			j1 = j;

			if (i1 >= 0 && i1 < NN)
				if (diamond[i][j] != diamond[i1][j1] && diamond[i1][j1] != -2 && diamond[i][j] != -2)
				{
					//if (dx == N-1 && dy == N)
					//	cout << i << " " << j << " " << i1 << " " << j1 << endl;
					return false;
				}
			i1 = i;
			j1 = 2*dy - j;
			if (j1 >= 0 && j1 < NN)
				if (diamond[i][j] != diamond[i1][j1] && diamond[i1][j1] != -2 && diamond[i][j] != -2) 
				{
					return false;
				}

		}
	return true;
}

int main()
{
	freopen("a-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);
	cin >> runs;
	for (int run = 1; run <= runs; ++run)
	{
		cin >> N;
		NN = 2*N-1;
		string line;
		getline(cin, line);
		for (int i = 0; i < NN; ++i)
			for (int j = 0; j < NN; ++j)
				diamond[i][j] = -2;
		for (int i = 0; i < NN; ++i)
		{
			getline(cin, line);
			bool hasNumber = false;
			for (int j = 0; j < line.size(); ++j)
				if (line[j] == ' ')
				       if (hasNumber)
					       diamond[i][j] = -1;
					else;
				else
				{
					diamond[i][j] = line[j] - '0';
					hasNumber = true;
				}
		}

		int best = INT_MAX;
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
				if (checkCenter(i, j) || checkCenter(i, -j) || checkCenter(-i, j) || checkCenter(-i, -j))
					if (best > i+j) best = i+j;
		best += N;

		//cout << best << endl;
		cout << "Case #" << run << ": " << best*best - N*N << endl;
	}
}
