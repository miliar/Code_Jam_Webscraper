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

char st [2000] = {0};

string pstr (string s, vector <int> perm)
{

	int k = perm.size ();
	int i = 0, j = 0;
	int n = s.size ();

	string ans ("");

	for (i = 0; i < n ; i +=k)
	{
		for (j = 0; j < k ; j ++)
		{
			ans.push_back (s [i + perm [j]]);
		}
	}
	return ans;
}

int gr (string s)
{
	int ans = 1;
	int i = 0;
	for (i = 1; i < s.size (); i ++)
		if (s [i] != s [i - 1]) ans ++;
	return ans;
}

int main ()
{
	FILE* fin, *fout;

	fin = stdin;
	fout = stdout;

	int i = 0, n = 0;
	fscanf (fin, "%d", &n);

	for (i = 0; i < n; i ++)
	{
		memset (st, 0, sizeof (st));
		int k = 0;

		fscanf (fin, "%d%s", &k, st);

		string s (st);

		vector <int> perm;
		perm.resize (k);

		int j = 0;

		for (j = 0; j < k ; j ++)
			perm [j] = j;

		int ans = s.size ();
		bool b = true;
		for (b = true; b; b = next_permutation (perm.begin (), perm.end ()))
		{
			string ps = pstr (s, perm);
			j = gr (ps);
			if (j < ans) ans = j;
		}

		fprintf (fout, "Case #%d: %d\n", i + 1, ans);


	}

	fclose (fin);
	fclose (fout);

	return 0;
}
