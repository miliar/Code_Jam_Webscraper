/*
 * $File: snapper_chain.cpp
 * $Date: Sat May 08 19:40:08 2010 +0800
 */
#include <cstdio>

namespace Solve
{
	bool check(int n, int k)
	{
		int mask = (1 << n) - 1;
		return (k & mask) == mask;
	}
	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int t;
	fscanf(fin, "%d", &t);
	int id = 0;
	while (t --)
	{
		int n, k;
		id ++;
		fscanf(fin, "%d%d", &n, &k);
		fprintf(fout, "Case #%d: %s\n", id, check(n, k) ? "ON" : "OFF");
	}
}

int main()
{
	Solve::solve(stdin, stdout);
}

