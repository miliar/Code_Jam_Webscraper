#define _USE_MATH_DEFINES

#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

struct sh
{
	int idx;
	bool mal;
};

bool less (const vector <sh> & a, const vector <sh> & b)
{
	if (a.size () < b.size ()) return true;
	if (a.size () > b.size ()) return false;
	return false;
}

bool operator < (const sh& a, const sh& b)
{
	if (!a.mal && b.mal) return true;
	if (!b.mal && a.mal) return false;
	return (a.idx < b.idx );
}


vector <vector <sh> > prefs ;
bool malt [2500];

int main ()
{
	FILE* fin, *fout;

	fin = stdin;
	fout = stdout;

	int i = 0, n = 0;
	fscanf (fin, "%d", &n);

	for (i = 0; i < n; i ++)
	{
		int j = 0, k = 0;
		int usr = 0, n_sh = 0;

		fscanf (fin, "%d%d", &n_sh, &usr);

		prefs.resize (usr);

		for (k = 0; k < usr; k ++)
		{
			prefs [k].clear ();

			int n_pref = 0;

			fscanf (fin, "%d", &n_pref);
			sh my_pref ;
			int u = 0;

			for (j = 0; j < n_pref; j ++)
			{
				fscanf (fin, "%d%d", &my_pref.idx, &u);
				my_pref.idx --;
				my_pref.mal = (u != 0);
				prefs [k].push_back (my_pref);
			}


			sort (prefs [k].begin (), prefs [k].end ());
		}

		sort (prefs.begin (),prefs.end (), less );

		for (k = 0; k < n_sh; k ++) malt [k] = false;

		bool pr = true;

		while (pr)
		{
			pr = false;

			for (j = 0; j < usr; j ++)
			{
				for (k = 0; k < prefs [j].size (); k ++)
				{
					if (malt [prefs [j][k].idx] == prefs [j][k].mal) break;
				}
				if (k < prefs [j].size ()) continue;
				k --;
				if (prefs [j][k].mal)
				{
					malt [prefs [j][k].idx] = true;
					pr = true;
				}
				else
				{
					pr= false;
					break;
				}
			}
		}

		for (j = 0; j < usr; j ++)
		{
			for (k = 0; k < prefs [j].size (); k ++)
			{
				if (malt [prefs [j][k].idx] == prefs [j][k].mal) break;
			}
			if (k >= prefs [j].size ()) break;
		}

		if (j < usr)
		{
			fprintf (fout, "Case #%d: IMPOSSIBLE\n", i + 1);
		}
		else
		{
			fprintf (fout, "Case #%d:", i + 1);
			for (j = 0, k  = 0; j < n_sh; j ++)
				if (malt [j]) fprintf (fout, " 1");
				else fprintf (fout, " 0");

			fprintf (fout, "\n");
		}
	}

	fclose (fin);
	fclose (fout);

	return 0;
}
