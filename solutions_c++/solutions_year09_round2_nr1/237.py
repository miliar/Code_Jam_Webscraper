/**
*** Google Code Jam - Round 1B
***
*** Problem: A
*** Author: druidu
**/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>

#define LINESIZE		90
#define MAXL			100
#define BUFSIZE			(LINESIZE * MAXL)
#define MAXA			100
#define MAXNAME			16
#define MAXFEAT			100

// XXX!
#define MAXTREES		1000

#define SKIPWS(p)		while (*p == ' ' || *p == '\n') p++
#define SKIPNUMBER(p)		while (isdigit(*p) || *p == '.') p++;

char treebuf[BUFSIZE];
char tmpbuf[MAXNAME];

char animals[MAXA][MAXNAME];
char nfeats, feats[MAXFEAT][MAXNAME];
int hasfeat[MAXA][MAXFEAT];
int ntrees;
double treew[MAXTREES];
int treef[MAXTREES], treel[MAXTREES], treer[MAXTREES];

int findfeat(char *name)
{
	int i;
	for (i = 0; i < nfeats; i++)
		if (!strcmp(feats[i], name))
			return i;
	return -1;
}

int allocfeat(char *name)
{
	int id = findfeat(name);

	if (id == -1) {
		id = nfeats++;
		strcpy(feats[id], name);
	}

	return id;
}

int alloctree()
{
	return ntrees++;
}

int parsetree(char **buf)
{
	char *p = *buf;
	int id;

	SKIPWS(p);
	if (*p != '(') {
		fprintf(stderr, "Tree parse error: expected '('\n");
		exit(1);
	}
	p++;
	SKIPWS(p);

	id = alloctree();
	treef[id] = -1;
	sscanf(p, "%lf", &treew[id]);

	SKIPWS(p);
	SKIPNUMBER(p);
	SKIPWS(p);

	if (*p != ')') {
		sscanf(p, "%s", tmpbuf);
		p += strlen(tmpbuf);
		treef[id] = allocfeat(tmpbuf);
		treel[id] = parsetree(&p);
		treer[id] = parsetree(&p);
	}

	SKIPWS(p);
	if (*p != ')') {
		fprintf(stderr, "Tree parse error: expected ')'\n");
		exit(1);
	}
	p++;
	SKIPWS(p);

	*buf = p;

	return id;
}

double computehappiness(int animal)
{
	double happiness = 1.0;
	int root;

	root = 0;
	while (1) {
		happiness *= treew[root];
		if (treef[root] == -1)
			break;
		root = hasfeat[animal][treef[root]] ? treel[root] : treer[root];
	}

	return happiness;
}

void solve()
{
	int L, A;
	int i, j, k, n, id;
	char *buf;

	assert(scanf("%d\n", &L) == 1);
	*treebuf = '\0';
	n = 0;
	for (i = 0; i < L; i++) {
		assert(fgets(treebuf + n, sizeof(treebuf) - n, stdin));
		n = strlen(treebuf);
	}

	nfeats = 0;
	ntrees = 0;
	buf = treebuf;
	parsetree(&buf);
	if (*buf != '\0') {
		fprintf(stderr, "Warning: extra stuff at end of tree: '%s'\n", buf);
		exit(1);
	}

#if 0
	for (i = 0; i < ntrees; i++) {
		printf("tree %d w=%.2lf f=%d(%s) l=%d r=%d\n", i, treew[i], treef[i], treef[i] != -1 ? feats[treef[i]] : "", treel[i], treer[i]);
	}
#endif

	memset(hasfeat, 0, sizeof(hasfeat));
	assert(scanf("%d", &A) == 1);
	for (i = 0; i < A; i++) {
		assert(scanf("%s", animals[i]) == 1);
		assert(scanf("%d", &k) == 1);
		for (j = 0; j < k; j++) {
			assert(scanf("%s", tmpbuf) == 1);
			id = findfeat(tmpbuf);
			if (id != -1) {
				hasfeat[i][id] = 1;
			} else {
//				fprintf(stderr, "Warning: symbol not in tree: '%s'\n", tmpbuf);
			}
		}
	}

	for (i = 0; i < A; i++) {
		printf("%.7lf\n", computehappiness(i));
	}
}

int main(int argc, char **argv)
{
	int N, X;

	if (argc > 1 && !freopen(argv[1], "rt", stdin)) {
		perror(argv[1]);
		return 1;
	}
	if (argc > 2 && !freopen(argv[2], "wt", stdout)) {
		perror(argv[2]);
		return 1;
	}

	assert(scanf("%d", &N) == 1);
	fprintf(stderr, "N=%d\n", N);

	for (X = 1; X <= N; X++) {
		printf("Case #%d:\n", X);
		solve();
	}

	return 0;
}
