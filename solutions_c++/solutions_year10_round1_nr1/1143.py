#include <stdio.h>
#include <vector>

#define BLUE 1
#define RED 2
#define NMAX 100

using namespace std;

int t, test, n, k;
vector< vector<int> > v, w;
	

int win(int colour)
{
	int s = 0;
	int i, j;
	for (i = 0; i < n; i++)
	{
		if (w[i].size() < k) break;
		s = 0;
		for (j = 0; j < w[i].size(); j++)
		{
			if (w[i][j] == colour) s++;
			else s = 0;
			if (s == k) return 1;
		}
	}
	for (i = 0; i < w[0].size(); i++)
	{
		s = 0;
		for (j = 0; j < n; j++)
		{
			if (i >= w[j].size()) break;
			if (w[j][i] == colour) s++;
			else s = 0;
			if (s == k) return 1;
		}
	}
	for (i = 0; i < w[0].size(); i++)
	{
		s = 0;
		for (j = 0; j < n; j++)
		{
			if (i+j >= n || i+j >= w[j].size()) break;
			if (w[j][i+j] == colour) s++;
			else s = 0;
			if (s == k) return 1;
		}
	}
	for (i = 1; i < n; i++)
	{
		s = 0;
		for (j = 0; j < n; j++)
		{
			if (i+j >= n || j >= w[i+j].size()) break;
			if (w[i+j][j] == colour) s++;
			else s = 0;
			if (s == k) return 1;
		}
	}
	for (i = 0; i < w[0].size(); i++)
	{
		s = 0;
		for (j = 0; j < n; j++)
		{
			if (i-j < 0 || i-j >= w[j].size()) break;
			if (w[j][i-j] == colour) s++;
			else s = 0;
			if (s == k) return 1;
		}
	}
	for (i = 1; i < n; i++)
	{
		s = 0;
		for (j = 0; j < n; j++)
		{
			if (w[i].size() - j < 1 || i+j >= n || w[i].size()-1-j >= w[i+j].size()) break;
			if (w[i+j][w[i].size()-1-j] == colour) s++;
			else s = 0;
			if (s == k) return 1;
		}
	}
	return 0;
}


int main()
{
	FILE *fin, *fout;
	fin = fopen("date.in", "rt");
	fout = fopen("date.out", "wt");
	fscanf(fin, "%d", &t);
	for (test = 1; test <= t; test++)
	{
		fscanf (fin, "%d %d", &n, &k);
		char s[NMAX];
		int i, j;
		for (i = 0; i < n; i++)
		{
			v.push_back(vector<int>());
			fscanf(fin, "%s", s);
			printf("%s\n", s);
			for (j = 0; j < n; j++)
			{
				if (s[j] == 'B') v[i].push_back(BLUE);
				if (s[j] == 'R') v[i].push_back(RED);
			}
		}
		for (i = 0; i < n; i++)
		{
			w.push_back(vector<int>());
			for (j = n-1; j >= 0; j--)
				if (!v[j].empty()) 
				{
					w.back().push_back(v[j].back());
					v[j].pop_back();
				}
		}
		int a, b;
		a = win(BLUE);
		b = win(RED);
		fprintf(fout, "Case #%d: ", test);
		if (a == 0 && b == 0) fprintf(fout, "Neither\n");
		if (a == 1 && b == 1) fprintf(fout, "Both\n");
		if (a == 1 && b == 0) fprintf(fout, "Blue\n");
		if (a == 0 && b == 1) fprintf(fout, "Red\n");
		for (i = 0; i < n; i++)
		{
			v[i].clear();
			w[i].clear();
		}
		v.clear();
		w.clear();
	}

fclose(fin);
fclose(fout);
return 0;
}
