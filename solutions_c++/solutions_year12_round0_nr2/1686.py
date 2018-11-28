#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <algorithm>
#include <hash_map>
#include <hash_set>

using namespace std;

#define FOR(i,n) for((i) = 0; (i) < (n); ++(i))

FILE *fi, *fo;

void mainImpl(int _c)
{
	int res = 0;
	int n, s, p;
	fscanf(fi, "%d%d%d", &n, &s, &p);
	int i;
	FOR(i, n)
	{
		int a;
		fscanf(fi, "%d", &a);
		if (a - p < 0 || (p - (a - p) / 2 > 2)) continue;
		if (p - (a - p) / 2 <= 1) {++res; continue;}
		if (s > 0) {++res; --s; continue;}
	}
	fprintf(fo, "Case #%d: %d\n", _c, res);
}


int main()
{
	fi = fopen("a.in", "rt");
	fo = fopen("a.out", "wt");

	int t, tt;
	fscanf(fi, "%d\n", &tt);

	FOR(t, tt) mainImpl(t + 1);

	fclose(fo);
	fclose(fi);
	return 0;
}