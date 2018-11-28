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
#include <set>

using namespace std;

struct my_pair
{
	int st, end;
	string name;

	my_pair () {st = end = 0; name = string ("");}

	my_pair (int s, int e, string ss) {st = s; end = e; name = ss;}
};

vector <my_pair> off;

bool operator < (const my_pair & a, const my_pair & b)
{
	if (a.st < b.st) return true;
	if (a.st > b.st) return false;
	if (a.end < b.end) return true;
	return false;
}

int DP = 0;

bool stupid (int dp, vector <my_pair> pu, int bb, std::set <string> used)
{
	int i = 0;
	if (dp >= DP)
	{
		if (used.size () > 3) 
			return false;
		//else
		//	printf ("used.sz == %u", used.size ());
		if (pu [0].st <= 1 && pu [pu.size () - 1].end >= 10000)
		{
			for (i = 0; i < dp - 1; i ++)
				if (pu [i].end < pu [i + 1].st - 1) 
				{
					//fprintf (stderr, "bad: %d %d\n", pu [i].end , pu [i + 1].st);
					return false;
				}
			return true;
		}
		return false;
	}
	for (i = bb + 1; i < off.size (); i ++)
	{
		bool nu = true;
		if (used.find (off [i].name) != used.end ()) nu = false;
		if (nu)
			used.insert (off [i].name);
		pu.push_back (off [i]);
		if (stupid (dp + 1, pu, i, used)) return true;
		pu.pop_back ();
		if (nu)
			used.erase (off [i].name);
	}
	return false;
}

char sss [100] = {0};

vector <my_pair> PU;

set <string> cols;

int main ()
{
	FILE* fin, *fout;

	fin = stdin;
	fout = stdout;

	int i = 0, n = 0;
	fscanf (fin, "%d", &n);

	for (i = 0; i < n; i ++)
	{
		int j = 0, no = 0;
		int s = 0, e = 0;

		fscanf (fin, "%d", &no);
		off.clear ();

		for (j = 0; j < no; j ++)
		{
			fscanf (fin, "%s%d%d", sss, &s, &e);
			string ss (sss);
			off.push_back (my_pair (s, e, ss));
		}

		sort (off.begin (), off.end ());

		for (j = 1; j <= 10; j ++)
		{
			PU.clear ();
			cols.clear ();
			//PU.resize (j);
			DP = j;

			if (stupid (0, PU, -1, cols))
			{
				fprintf (fout, "Case #%d: %d\n", i + 1, j);
				break;
			}
		}

		if (j > 10)
			fprintf (fout, "Case #%d: IMPOSSIBLE\n", i + 1);
	}

	fclose (fin);
	fclose (fout);

	return 0;
}
