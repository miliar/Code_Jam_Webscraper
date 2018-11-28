#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

#define INF (1<<30)
#define MAXN 200
int ABS(int x)
{
    return x > 0 ? x : -x;
}
int MAX(int x, int y)
{
    return x > y ? x : y;
}

int n, m;
int c, d, k;
char s[MAXN];
char ans[MAXN];
char cflg[30][30];
int dflg[30][30];
int has[30];

void insert(char ch)
{
    k++;

    ans[k] = ch;
    has[ans[k] - 'A']++;
}
void remove()
{
    has[ans[k] - 'A']--;
    k--;
}

int findD(char ch)
{
    int x = ch - 'A';
    int i;

    for (i = 0; i < 26; i++)
        if (has[i] > 0 && dflg[x][i])
        {
            //printf ("Find %c %c\n", (char)x+'A', i+'A');
            return 1;
        }

    return 0;
}

void clear()
{
    memset(has, 0, sizeof(has));
    k = -1;
}

void print()
{
    int i;
    printf ("[");

    if (k >= 0)
        printf ("%c", ans[0]);

    for (i = 1; i <= k; i++)
        printf (", %c", ans[i]);

    printf ("]\n");
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int cs, csnum, i, j, x, y;

    scanf (" %d", &csnum);
    for (cs = 1; cs <= csnum; cs++)
    {
        memset(cflg, 0, sizeof(cflg));
        memset(dflg, 0, sizeof(dflg));
        memset(has, 0, sizeof(has));

        scanf (" %d", &c);
        for (i = 0; i < c; i++)
        {
            scanf (" %s", s);
            x = s[0] - 'A';
            y = s[1] - 'A';
            cflg[x][y] = cflg[y][x] = s[2];
        }

        scanf (" %d", &d);
        for (i = 0; i < d; i++)
        {
            scanf (" %s", s);
            x = s[0] - 'A';
            y = s[1] - 'A';
            dflg[x][y] = dflg[y][x] = 1;
        }

        scanf (" %d %s", &n, s);
        k = -1;
        insert(s[0]);

        printf ("Case #%d: ", cs);

       //print();

        for (i = 1; i < n; i++)
        {
            insert(s[i]);
           // printf ("i=%d (%c)", i, s[i]);

            if (k < 1) continue;
            x = ans[k-1] - 'A';
            y = ans[k] - 'A';


            if (cflg[x][y] > 0)
            {
                remove();
                remove();
                insert(cflg[x][y]);
            }

            if (k < 1) continue;

            if (findD(ans[k]))
            {
                clear();
            }

           // print();
        }

        print();
    }
}
/*


*/


