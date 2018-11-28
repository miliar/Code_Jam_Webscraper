#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <utility>
#define MAXN (1 << 7)
using namespace std;

int t, brt, n, sol;
int a[MAXN][MAXN], newa[MAXN][MAXN];


int main ()
{
	scanf ("%d" , &t);

	while ( t -- )
	{
        scanf ("%d" , &n);
        int x1,x2,y1,y2; sol = 0;
        memset (a, 0, sizeof (a));

        for (int i=0; i < n; ++i)
        {
            scanf ("%d%d%d%d" , &x1, &y1, &x2, &y2);
            for (int jx=x1; jx <= x2; ++jx)
                for (int jy=y1; jy <= y2; ++jy)
                    a[jx][jy] = 1;
        }

        int key = 1;
        while (key)
        {
            key = 0;
            for (int i=0; i <= 100; ++i)
                for (int j=0; j <= 100; ++j)
                {
                    if (i == 0 || j == 0) { newa[i][j] = 0; continue; }
                    newa[i][j] = a[i][j];
                    if (a[i-1][j] == 0 && a[i][j-1] == 0) newa[i][j] = 0;
                    if (a[i-1][j] == 1 && a[i][j-1] == 1) newa[i][j] = 1;
                }
            for (int i=0; i <= 100; ++i)
                for (int j=0; j <= 100; ++j)
                {
                    a[i][j] = newa[i][j];
                    if (a[i][j]) key = 1;
                }

            ++sol;
        }

		printf ("Case #%d: %d\n", ++brt , sol);
	}
	return 0;
}
