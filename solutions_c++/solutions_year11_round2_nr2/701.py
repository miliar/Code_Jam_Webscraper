/*
 * Google Code Jam 2011
 * Round 1B - Problem B - Revenge of the Hot Dogs
 */

#include <stdio.h>
#include <string.h>
#include <vector>
#include <math.h>

#define INPUT	"B-small-attempt0.in"
#define OUTPUT	"B-small-attempt0.out"

int T, C, D;
std::vector<int> V, Pos;


void ReadData()
{
	int i;

	scanf("%d %d", &C, &D);

	V.clear();
	V.resize(C);
	Pos.clear();
	Pos.resize(C);
	for (i = 0; i < C; i++)
	{
		scanf("%d %d", &Pos[i], &V[i]);
	}
}

double Solve()
{
	int i, j, x;
	double t, l = 0, r = 2000.0 * 1000.0 * 1000.0;
	double lastpos;
	bool ok, first;

	while (fabs(r - l) > 1e-6)
	{
		t = (l + r) / 2;

		ok = true;
		first = true;

		/* try to move the vendors in t seconds */
		for (i = C - 1; i >= 0 && ok; i--)
		{
			for (j = 0; j < V[i] && ok; j++)
			{
				x = Pos[i];
				if (first)
				{
					lastpos = x + t;
					first = false;
				}
				else if (x + t <= lastpos - D)
				{
					lastpos = x + t;
					continue;
				}
				else if (x + t > lastpos - D)
				{
					/* force it to be at dist D */
					lastpos = lastpos - D;
					if (lastpos < x - t)
					{
						ok = false;
					}
				}
			}
		}

		if (ok)
		{
			/* decrease t */
			r = t;
		}
		else
		{
			/* increase t */
			l = t;
		}
	}

	return r;
}


int main()
{
	int i, sol;

	freopen(INPUT, "rt", stdin);
	scanf("%d\n", &T);

	freopen(OUTPUT, "wt", stdout);
	for (i = 1; i <= T; i++)
	{
		ReadData();

		printf("Case #%d: %.6lf\n", i, Solve());
	}

	return 0;
}