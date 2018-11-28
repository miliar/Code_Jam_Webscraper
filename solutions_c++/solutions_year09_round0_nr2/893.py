#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

typedef int Link;
enum 
{
	NONE = 0, UP = 1, LEFT = 2, RIGHT = 4, DOWN = 8
};

struct Ground
{
	Ground() {}
	Ground(int _l, Link _c) : level(_l), connection(_c), label(0) {}
	int level;
	Link connection;
	char label;
};

const int MAXHW = 100;
Ground t[MAXHW][MAXHW];
int r_size, c_size;


char dfs_s;
void dfs(int r, int c)
{
	if (t[r][c].label) return;
	t[r][c].label = dfs_s;
	if (t[r][c].connection & UP) dfs(r-1, c);
	if (t[r][c].connection & DOWN) dfs(r+1, c);
	if (t[r][c].connection & LEFT) dfs(r, c-1);
	if (t[r][c].connection & RIGHT) dfs(r, c+1);
}

void labela()
{
	dfs_s = 'a';
	for (int r = 0; r < r_size; r++)
		for (int c = 0; c < c_size; c++)
			if (!t[r][c].label)
			{
				dfs(r, c);
				dfs_s++;
			}
}

void linka()
{
	int up, lf, rg, dw, m;
	for (int r = 0; r < r_size; r++)
	{
		for (int c = 0; c < c_size; c++)
		{
			up = (r > 0 ? t[r-1][c].level : INT_MAX);
			dw = (r < r_size-1 ? t[r+1][c].level : INT_MAX);
			lf = (c > 0 ? t[r][c-1].level : INT_MAX);
			rg = (c < c_size-1 ? t[r][c+1].level : INT_MAX);
			m = min(min(up, dw), min(lf, rg));
			if (m < t[r][c].level)
			{
				if (m == up) { t[r][c].connection |= UP; t[r-1][c].connection |= DOWN; }
				else if (m == lf) { t[r][c].connection |= LEFT; t[r][c-1].connection |= RIGHT; }
				else if (m == rg) { t[r][c].connection |= RIGHT; t[r][c+1].connection |= LEFT; }
				else if (m == dw) { t[r][c].connection |= DOWN; t[r+1][c].connection |= UP; }
			}
		}
	}
}

void run(FILE* in, FILE* out)
{
	int casi, l;
	fscanf(in, "%d", &casi);
	for (int caso = 1; caso <= casi; caso++)
	{
		fscanf(in, "%d%d", &r_size, &c_size);
		for (int r = 0; r < r_size; r++)
			for (int c = 0; c < c_size; c++)
			{
				fscanf(in, "%d", &l);
				t[r][c] = Ground(l, NONE);
			}
		linka();
		labela();

		fprintf(out, "Case #%d:\n", caso);
		for (int r = 0; r < r_size; r++)
		{
			fprintf(out, "%c", t[r][0].label);
			for (int c = 1; c < c_size; c++)
				fprintf(out, " %c", t[r][c].label);
			fprintf(out, "\n");
		}
	}
}

int main()
{
	run(stdin, stdout);
	return 0;
}

