#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <utility>
#define MAXN (1 << 11)
using namespace std;

int t, brt;
int m[MAXN], n, sol;

void gen (int from, int to)
{
    for (int i=from; i < to; ++i)
        if (m[i] > 0) goto skip;
    return ;
    skip:;

    for (int i=from; i < to; ++i)
        m[i]--;
    sol ++;
    int mid = (from + to)/2;
    gen (from, mid);
    gen (mid, to);
}

int main ()
{
	scanf ("%d" , &t);

	while ( t -- )
	{
        scanf ("%d", &n);
        sol = 0;

        for (int i=0; i < (1 << n); ++i)
        {
            scanf ("%d", &m[i]);
            m[i] = n - m[i];
        }

        int price;
        for (int i=n-1; i >= 0; --i)
            for (int j=0; j < (1 << i); ++j)
                scanf ("%d", &price);

        gen (0, (1 << n));

		printf ("Case #%d: %d\n", ++brt, sol );
	}
	return 0;
}
