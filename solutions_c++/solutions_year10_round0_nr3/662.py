/*
 * $File: theme_park.cpp
 * $Date: Sat May 08 23:46:44 2010 +0800
 */
#include <cstdio>
#include <cstring>

namespace Solve
{
	const int NGRP_MAX = 1005;
	int grp[NGRP_MAX], ngrp, next[NGRP_MAX];
	int nrun, size;
	typedef long long int Bignum;
	Bignum income[NGRP_MAX];

	Bignum work();

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int t;
	fscanf(fin, "%d", &t);
	for (int id = 1; id <= t; id ++)
	{
		fscanf(fin, "%d%d%d", &nrun, &size, &ngrp);
		for (int i = 0; i < ngrp; i ++)
			fscanf(fin, "%d", &grp[i]);
		fprintf(fout, "Case #%d: %lld\n", id, work());
	}
}

Solve::Bignum Solve::work()
{
	memset(next, -1, sizeof(next));
	income[0] = 0;
	int pos = 0;
	while (1)
	{
		int ne = pos;
		Bignum in1 = income[pos];
		for (int r = size; r >= grp[ne]; )
		{
			in1 += grp[ne];
			r -= grp[ne];
			ne ++;
			if (ne == ngrp)
				ne = 0;
			if (r != size && ne == pos)
				break;
		}
		if (next[ne] != -1)
		{
			int loop_size = 1;
			for (int i = ne; i != pos; i = next[i], loop_size ++);
			Bignum ans = in1;
			nrun --;
			pos = ne;
			ans += (in1 - income[ne]) * (nrun / loop_size);
			nrun %= loop_size;
			while (nrun --)
			{
				ans += income[next[pos]] - income[pos];
				pos = next[pos];
			}
			return ans;
		}
		next[pos] = ne;
		nrun --;
		if (!nrun)
			return in1;
		income[ne] = in1;
		pos = ne;
	}
}

int main()
{
	Solve::solve(stdin, stdout);
	return 0;
}

