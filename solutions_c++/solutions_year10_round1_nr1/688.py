#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <utility>
#define MAXN (1 << 6)
using namespace std;

int t, brt;
int n, m, win[2];
char a[MAXN][MAXN], b[MAXN][MAXN];

int main ()
{
	scanf ("%d" , &t);

	while ( t -- )
	{
        scanf ("%d%d", &n, &m);

        win[0] = win[1] = 0;

        for (int i=0; i < n; ++i)
            scanf ("%s" , &a[i]);

        for (int i=0; i < n; ++i)
            for (int j=0; j < n; ++j)
                b[i][j] = '.';

        for (int i=n-1; i >= 0; --i)
        {
            int br=n-1;
            for (int j=n-1; j >= 0; --j)
                if (a[i][j] != '.')
                    b[br--][n-1-i] = a[i][j];
        }

        for (int i=0; i < n; ++i)
            for (int j=0; j < n; ++j)
            {
                if (b[i][j] == '.') continue;

                if (i+m <= n)
                {
                    for (int k=1; k < m; ++k)
                        if (b[i+k][j] != b[i][j])
                            goto skip;
                    win[(b[i][j] == 'R')] = 1;
                    skip:;
                }
                if (j+m <= n)
                {
                    for (int k=1; k < m; ++k)
                        if (b[i][j+k] != b[i][j])
                            goto skip2;
                    win[(b[i][j] == 'R')] = 1;
                    skip2:;
                }
                if ((j+m <= n) && (i+m <= n))
                {
                    for (int k=1; k < m; ++k)
                        if (b[i+k][j+k] != b[i][j])
                            goto skip3;
                    win[(b[i][j] == 'R')] = 1;
                    skip3:;
                }
                if ((i+m <= n) && (j-m+1 >= 0))
                {
                    for (int k=1; k < m; ++k)
                        if (b[i+k][j-k] != b[i][j])
                            goto skip4;
                    win[(b[i][j] == 'R')] = 1;
                    skip4:;
                }
            }

		printf ("Case #%d: ", ++brt );
		//printf ("%d %d\n" , win[0], win[1]);
		if (!win[0] && !win[1]) { printf ("Neither\n"); continue; }
		if (win[0] && win[1]) { printf ("Both\n"); continue; }
		if (win[1]) printf ("Red\n");
		else printf ("Blue\n");
	}
	return 0;
}
