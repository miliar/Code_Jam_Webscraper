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

enum ev_kind
{
	app_a = 0,
	app_b = 1,
	need_a = 2,
	need_b = 3
};

struct Ev
{
	int tm_;
	ev_kind kind;

	Ev () {}

	void read (FILE* fin, ev_kind k, int t)
	{
		kind = k;
		int hh = 0, mm = 0;
		fscanf (fin, "%d:%d", &hh, &mm);
		tm_ = hh * 60 + mm;
		if (kind == app_a || kind == app_b) tm_ += t;
	}
};

bool operator< (const Ev& a, const Ev& b)
{
	if (a.tm_ < b.tm_) return true;
	if (a.tm_ > b.tm_) return false;
	if ((int) a.kind < (int) b.kind) return true;
	return false;
}

vector <Ev> evs;

int main ()
{
	FILE* fin, *fout;

	fin = stdin;
	fout = stdout;

	int i = 0, n= 0;
	fscanf (fin, "%d", &n);

	for (i = 0; i < n; i ++)
	{
		int na = 0, nb = 0;
		int t = 0;
		int j = 0;
		fscanf (fin, "%d%d%d", &t, &na, &nb);

		evs.clear ();

		for (j = 0; j < na; j ++)
		{
			Ev ee;
			ee.read (fin, need_a, t);
			evs.push_back (ee);
			ee.read (fin, app_b, t);
			evs.push_back (ee);
		}
		for (j = 0; j < nb; j ++)
		{
			Ev ee;
			ee.read (fin, need_b, t);
			evs.push_back (ee);
			ee.read (fin, app_a, t);
			evs.push_back (ee);
		}

		sort (evs.begin (), evs.end ());

		int init_a = 0, init_b = 0;
		int now_a = 0, now_b = 0;

		for (j = 0; j < evs.size (); j ++)
		{
			switch (evs [j].kind)
			{
				case app_a :
					now_a ++;
					break;
				case app_b :
					now_b ++;
					break;
				case need_a :
					if (now_a > 0) now_a --;
					else init_a ++;
					break;
				case need_b :
					if (now_b > 0) now_b --;
					else init_b ++;
					break;
			}
		}

		fprintf (fout, "Case #%d: %d %d\n", i + 1, init_a, init_b);
	}

	fclose (fin);
	fclose (fout);

	return 0;
}
