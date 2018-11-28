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

int rec(int n, int a, int b)
{
	hash_set<int> M;
	int res = 0;
	int q10 = 10;
	while (n / q10 > 0) q10 *= 10;
	int p10 = 10;
	while (n / p10 > 0)
	{
		int r = n % p10;
		int m = n / p10 + r * q10 / p10;
		if (m >= a && m <= b && m > n && M.find(m) == M.end()) 
		{
			M.insert(m);
			++res;
		}
		p10 *= 10;
	}
	return res;
}

void mainImpl(int _c)
{
	int res = 0;
	int a, b, i;
	fscanf(fi, "%d%d", &a, &b);
	for (i = a; i <= b; ++i)
	{
		res += rec(i, a, b);
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