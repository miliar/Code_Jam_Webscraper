#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>

#define MAX 1024

using namespace std;
FILE *in; FILE *out;

int n, m, a;

inline int findArea(int x1, int y1, int x2, int y2, int x3, int y3)
{
	return x1 * y2 + x2 * y3 + x3 * y1 -
	       x1 * y3 - x2 * y1 - x3 * y2 ;
}


void doWork(int testNum)
{
	int i, c, j, k, l, r;
	
	fscanf(in, "%d %d %d", &n, &m, &a);
	if (n * m < a) {fprintf(out, "IMPOSSIBLE\n"); return;}
	
	for (i=0; i<=n; i++)
		for (c=0; c<=m; c++)
			for (j=i; j<=n; j++)
				for (k=0; k<=m; k++)
					for (l=j; l<=n; l++)
						for (r=0; r<=m; r++)
							if (findArea(i, c, j, k, l, r) == a)
								{fprintf(out, "%d %d %d %d %d %d\n", i, c, j, k, l, r); return;}
	
	cout << "Finished test " << testNum << endl;
	
	return;
}

int main(void)
{
	int tests, i;
	
	in = fopen("triangleAreas.in", "rt");
	out = fopen("triangleAreas.out", "wt");
	
	fscanf(in, "%d", &tests);
	for (i=0; i<tests; i++)
	{
		fprintf(out, "Case #%d: ", i+1);
		doWork(i + 1);
	}
	
	return 0;
}
