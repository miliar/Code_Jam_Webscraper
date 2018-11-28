#include <iostream>
#include <cstdio>
#include <fstream>

using namespace std;

int tree[10010][2];
int gate[10010];
bool can[10010];

int N, M, V;

int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");

	fin >> N;
	for (int ni = 1; ni <= N; ni++)
	{
		fin >> M >> V;
		for (int i = 1; i <= M; i++)
		{
			tree[i][0] = tree[i][1] = -1;
			can[i] = false;
			gate[i] = -1;
		}

		int num_in = (M-1)/2;
		for (int i = 1; i <= num_in; i++)
		{
			int G, C;
			fin >> G >> C;
			gate[i] = G;
			if (C == 1) can[i] = true;
		}

		for (int i = num_in+1; i <= M; i++)
		{
			int I;
			fin >> I;
			if (I == 0) tree[i][0] = 0;
			else tree[i][1] = 0;
		}

		for (int i = num_in; i >= 1; i--)
		{
			int l = i * 2;
			int r = i * 2 + 1;

			int and_t = -1;
			if (gate[i] == 1) and_t = 0;
			else if (can[i]) and_t = 1;
			if (and_t >= 0)
			{
				if (tree[l][0] != -1 && tree[r][0] != -1)
				{
					if (tree[i][0] == -1 || 
						tree[i][0] > tree[l][0] + tree[r][0] + and_t)
						tree[i][0] = tree[l][0] + tree[r][0] + and_t;
				}
				if (tree[l][0] != -1 && tree[r][1] != -1)
				{
					if (tree[i][0] == -1 || 
						tree[i][0] > tree[l][0] + tree[r][1] + and_t)
						tree[i][0] = tree[l][0] + tree[r][1] + and_t;
				}
				if (tree[l][1] != -1 && tree[r][0] != -1)
				{
					if (tree[i][0] == -1 || 
						tree[i][0] > tree[l][1] + tree[r][0] + and_t)
						tree[i][0] = tree[l][1] + tree[r][0] + and_t;
				}
				if (tree[l][1] != -1 && tree[r][1] != -1)
				{
					if (tree[i][1] == -1 || 
						tree[i][1] > tree[l][1] + tree[r][1] + and_t)
						tree[i][1] = tree[l][1] + tree[r][1] + and_t;
				}
			}

			int or_t = -1;
			if (gate[i] == 0) or_t = 0;
			else if (can[i]) or_t = 1;
			if (or_t >= 0)
			{
				if (tree[l][0] != -1 && tree[r][0] != -1)
				{
					if (tree[i][0] == -1 || 
						tree[i][0] > tree[l][0] + tree[r][0] + or_t)
						tree[i][0] = tree[l][0] + tree[r][0] + or_t;
				}
				if (tree[l][0] != -1 && tree[r][1] != -1)
				{
					if (tree[i][1] == -1 || 
						tree[i][1] > tree[l][0] + tree[r][1] + or_t)
						tree[i][1] = tree[l][0] + tree[r][1] + or_t;
				}
				if (tree[l][1] != -1 && tree[r][0] != -1)
				{
					if (tree[i][1] == -1 || 
						tree[i][1] > tree[l][1] + tree[r][0] + or_t)
						tree[i][1] = tree[l][1] + tree[r][0] + or_t;
				}
				if (tree[l][1] != -1 && tree[r][1] != -1)
				{
					if (tree[i][1] == -1 || 
						tree[i][1] > tree[l][1] + tree[r][1] + or_t)
						tree[i][1] = tree[l][1] + tree[r][1] + or_t;
				}
			}
		}

		fout << "Case #" << ni << ": ";
		if (tree[1][V] != -1) fout << tree[1][V] << endl;
		else fout << "IMPOSSIBLE" << endl;
	}

	return 0;
};