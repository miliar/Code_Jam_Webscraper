#include <stdio.h>
#include <string.h>
#include <iostream>
#include <map>
using namespace std;

#define MAXN 1010
#define MAXL 500
int n, m;

struct node
{
    int x, y;
    bool operator<(const node &p)const
    {
        if (x != p.x) return x < p.x;
        return y < p.y;
    }
}a[MAXN];


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int i, j, cs, csnum,cnt1, cnt0, ans = 0, top;

    scanf ("%d", &csnum);

    for (cs = 1; cs <= csnum; cs++)
    {
        scanf ("%d", &n);
        for (i = 0; i < n; i++)
        {
            scanf ("%d %d", &a[i].x, &a[i].y);
        }

        //sort(a, a+n);
        ans = 0;
        //if (a[0].y > a[1].y) ans = 1;
       // printf ("Case #%d: %d\n", cs, ans);

        for (i = 0; i < n; i++)
        {
            for (j = 0; j < i; j++)
            {
                if ((a[i].x < a[j].x && a[i].y > a[j].y)
                || (a[i].x > a[j].x && a[i].y < a[j].y) ) ans++;
            }
        }
        printf ("Case #%d: %d\n", cs, ans);

    }
}

/*

*/

