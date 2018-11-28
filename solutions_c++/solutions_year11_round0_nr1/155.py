/*
 * $File: a.cpp
 * $Date: Sat May 07 10:03:17 2011 +0800
 */

#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

namespace Solve
{
	const int SEQLEN_MAX = 105;
	struct Seq_node
	{
		int robot, pos;
	};
	Seq_node seq[SEQLEN_MAX];
	int seqlen;

	int work();
	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int ncase;
	fscanf(fin, "%d", &ncase);
	for (int casenu = 1; casenu <= ncase; casenu ++)
	{
		fscanf(fin, "%d", &seqlen);
		for (int i = 0; i < seqlen; i ++)
		{
			char str[5];
			fscanf(fin, "%s%d", str, &seq[i].pos);
			seq[i].robot = (str[0] == 'B');
		}
		fprintf(fout, "Case #%d: %d\n", casenu, work());
	}
}

int Solve::work()
{
	int time[2] = {0, 0}, pos[2] = {1, 1},
		cur_time = 0;
	for (int i = 0; i < seqlen; i ++)
	{
		int r = seq[i].robot;
		cur_time = max(cur_time, time[r] + abs(pos[r] - seq[i].pos)) + 1;
		pos[r] = seq[i].pos;
		time[r] = cur_time;
	}
	return cur_time;
}

int main()
{
	Solve::solve(stdin, stdout);
}

