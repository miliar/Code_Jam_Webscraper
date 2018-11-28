#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <utility>

using namespace std;

int main()
{
	int t, tt;
	FILE *fi = fopen("a.in", "rt");
	FILE *fo = fopen("a.out", "wt");
	fscanf(fi, "%d", &tt);
	for (t = 0; t < tt; ++t)
	{
		int n,k;
		fscanf(fi, "%d%d", &n, &k);
		fprintf(fo, "Case #%d: %s\n", t+1, ((k % (1<<n)) >= (1<<n) - 1) ? "ON" : "OFF");
	}
	fclose(fi);
	fclose(fo);
	return 0;
}