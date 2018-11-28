#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>

using namespace std;

int    o[200], b[200], to[200], tb[200], no, nb;


int solve()
{
	int i = 0, j = 0;
	int time = 0;
	int oToTarget, bToTarget;

	oToTarget = o[i] - 1;
	bToTarget = b[i] - 1;

	while ( (i < no) && (j < nb) )
	{
		if (to[i] < tb[j])
		{
			if (oToTarget == 0)
			{
				time++;
				i++;

				if (bToTarget != 0)
				{
					bToTarget--;
				}

				if (i < no)
				{
					oToTarget = abs(o[i] - o[i-1]);
				}
			}
			else
			{
				time += oToTarget;

				if (bToTarget != 0)
				{
					bToTarget -= min(oToTarget, bToTarget);
				}

				oToTarget = 0;
			}
		}
		else
		{
			if (bToTarget == 0)
			{
				time++;
				j++;

				if (oToTarget != 0)
				{
					oToTarget--;
				}

				if (j < nb)
				{
					bToTarget = abs(b[j] - b[j-1]);
				}
			}
			else
			{
				time += bToTarget;

				if (oToTarget != 0)
				{
					oToTarget -= min(oToTarget, bToTarget);
				}

				bToTarget = 0;
			}
		}
	}


	if (i == no)
	{
		if (j < nb)
		{
			time += bToTarget + 1;
			j++;
		}

		for ( ; j < nb; j++)
		{
			time += abs(b[j] - b[j-1]) + 1;
		}
	}
	else
	{
		if (i < no)
		{
			time += oToTarget + 1;
			i++;
		}

		for ( ; i < no; i++)
		{
			time += abs(o[i] - o[i-1]) + 1;
		}
	}

	return time;
}



int main()
{
	fstream		f, g;
	int			tests;
	string      s;
	int         n, idx;

	f.open("in.txt", ios :: in);
	g.open("out.txt", ios :: out);

	f >> tests;

	for (int k = 1; k <= tests; k++)
	{
		f >> n;

		idx = no = nb = 0;
		for (int i = 0; i < n; i++)
		{
			f >> s;

			if (s[0] == 'O')
			{
				f >> o[no];
				to[no++] = idx++;
			}
			else
			{
				f >> b[nb];
				tb[nb++] = idx++;
			}
		}

		g << "Case #" << k << ": " << solve();

		if (k != tests)
		{
			g << "\n";
		}
	}

	f.close();
	g.close();

	return 0;
}