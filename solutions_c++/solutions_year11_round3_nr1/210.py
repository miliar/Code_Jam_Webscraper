/*
  ID: nigo1
  LANG: C++
  TASK: A
*/
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <stack>

#define pf printf
#define sf scanf
#define TIME pf("%f", (double)clock()/CLOCKS_PER_SEC);

using namespace std;

int N, R, C, T;

char a[64][64];

void fill () {
    for (int i = 0; i < R - 1; i++)
        for (int j = 0; j < C - 1; j++)
            if (a[i][j] == '#' and a[i + 1][j] == '#' and a[i][j + 1] == '#' and a[i + 1][j + 1] == '#') {
                a[i][j] = a[i + 1][j + 1] = '/';
                a[i + 1][j] = a[i][j + 1] = '\\';
            }
}

bool ok () {
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            if (a[i][j] == '#') return 0;

    return 1;
}

void print () {
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++)
            printf ("%c", a[i][j]);
        printf ("\n");
    }
}
int main()
{
	freopen ("A.in", "r", stdin);
	freopen ("A.out", "w", stdout);

    scanf ("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf ("Case #%d:\n", t);

        scanf ("%d %d\n", &R, &C);
        for (int i = 0; i < R; i++)
            scanf ("%s\n", &a[i]);

        fill ();

        if (!ok ())
            printf ("Impossible\n");
        else
            print();
    }
}
