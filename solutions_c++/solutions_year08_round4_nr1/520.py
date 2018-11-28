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

#define AND 0
#define OR 1

struct Node
{
	int idx;
	int kind;
	int init;
	bool chg;

	Node () {}

	int leftidx () {return 2*idx + 1;}
	int rightidx () {return 2*idx + 2;}
	int paridx () {return (idx - 1) / 2;}

	Node& left ();
	Node& right ();
	Node& parent ();

	bool haschild ();
};

vector <Node> tree;

Node& Node::left ()
{
	return tree [leftidx ()];
}

Node& Node::right ()
{
	return tree [rightidx ()];
}

Node& Node::parent ()
{
	return tree [paridx ()];
}

bool Node::haschild ()
{
	return (leftidx () < tree.size ());
}

void setvals (Node& cur)
{
	if (!cur.haschild ()) return;
	setvals (cur.left ());
	setvals (cur.right ());
	if (cur.kind == AND) cur.init = (cur.left ().init && cur.right ().init);
	else cur.init = (cur.left ().init || cur.right ().init);
}

int minchg (Node& cur, int des)
{
	if (cur.init == des) return 0;
	if (! cur.haschild ()) return 1000000;
	int l0 = minchg (cur.left (), 0);
	int l1 = minchg (cur.left (), 1);
	int r0 = minchg (cur.right (), 0);
	int r1 = minchg (cur.right (), 1);
	int now = 0;
	if (cur.kind == OR && des == 0) now = l0 + r0;
	if (cur.kind == OR && des == 1) now =  min (l1, r1);
	if (cur.kind == AND && des == 0) now = min (l0, r0);
	if (cur.kind == AND && des == 1) now = l1 + r1;
	if (!cur.chg) return now;
	int chg = 0;
	if (cur.kind == AND && des == 0) chg = l0 + r0;
	if (cur.kind == AND && des == 1) chg =  min (l1, r1);
	if (cur.kind == OR && des == 0) chg = min (l0, r0);
	if (cur.kind == OR && des == 1) chg = l1 + r1;
	return min (now, chg + 1);
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
		int sz  = 0, des = 0;

		fscanf (fin, "%d%d", &sz, &des);

		tree.clear ();
		tree.resize (sz);

		int j = 0, k  =0, l = 0;

		for (j = 0; j < (sz - 1) / 2; j ++)
		{
			fscanf (fin, "%d%d", &tree [j].kind, &l);
			tree [j].kind = 1 - tree [j].kind ;
			tree [j].chg = (l == 1);
		}

		for (; j < sz; j ++)
			fscanf (fin, "%d", &tree [j].init);

		for (j = 0; j < sz; j ++) tree [j].idx = j;

		setvals (tree [0]);

		k = minchg (tree [0], des);

		fprintf (fout, "Case #%d: ", i + 1);
		if (k > 500000) fprintf (fout, "IMPOSSIBLE\n");
		else fprintf (fout, "%d\n", k);
	}

	fclose (fin);
	fclose (fout);

	return 0;
}
