// Using libUtil from libGlov (Graphics Library of Victory) available at http://bigscreensmallgames.com/libGlov
#include "utils.h"
#include "file.h"
#include "strutil.h"
#include "assert.h"
#include "array.h"
#include <string.h>
#include <stdio.h>
#include <stdarg.h>
#include <conio.h>
#include "rand.h"
#include <ctype.h>
#include <vector>
using namespace std;

typedef struct Node
{
	int b;
	vector<int> deps;
	char *name;
} Node;

Node nodes[1001];
int nn;

int lookup(char *name)
{

	int myi=-1;
	for (int j=0; j<nn; j++)
	{
		if (strcmp(nodes[j].name, name)==0)
		{
			myi = j;
		}
	}
	if (myi==-1)
	{
		myi=nn;
		nn++;
		nodes[myi].name = name;
		nodes[myi].deps.clear();
	}
	return myi;
}

int doit(int n)
{
	for (unsigned int i=0; i<nodes[n].deps.size(); i++)
	{
		doit(nodes[n].deps[i]);
	}
	for (unsigned int i=0; i<nodes[n].deps.size(); i++)
	{
		for (unsigned int j=i+1; j<nodes[n].deps.size(); j++)
		{
			if (nodes[nodes[n].deps[i]].b < nodes[nodes[n].deps[j]].b)
			{

				int t = nodes[n].deps[i];
				nodes[n].deps[i] = nodes[n].deps[j];
				nodes[n].deps[j] = t;
			}
		}
	}
	nodes[n].b=1 + nodes[n].deps.size();
	for (unsigned int i=0; i<nodes[n].deps.size(); i++)
	{
		int v = nodes[nodes[n].deps[i]].b + i;
		if (v > nodes[n].b)
			nodes[n].b = v;
	}
	return nodes[n].b;
}

char *doA(char **&toks)
{
	static char buf[1024];
	nn=0;
	int N = atoi(*toks++);
	for (int i=0; i<N; i++)
	{
		char *m = *toks++;
		int myi=lookup(m);
		int M = atoi(*toks++);
		for (int j=0; j<M; j++)
		{
			char *m2 = *toks++;
			if (isupper(m2[0]))
			{
				nodes[myi].deps.push_back(lookup(m2));
			}
		}
	}
	int r = doit(0);
	sprintf(buf, "%d", r);
	return buf;
}

