#include <cstdio>
#include <cctype>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <utility>
#define MPI 3.141592653589793238462643
#define eps 1e-8
#define inf ((int)1e9)
#define pb push_back
#define mp make_pair
#define FI first
#define SE second
#define FF(i, s, e) for(i = s; i <= e; i++)
#define FB(i, s, e) for(i = s; i >= e; i--)
#define Ff(i, s, e) for(i = s; i < e; i++)
#define Fb(i, s, e) for(i = s; i > e; i--)
#define pos(x, y) ((x + y ) | (x != y))
#define sdis(x1, y1, x2, y2) ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
using namespace std;

int map[128];
char s[1000];
int main()
{
    int i, j, t, len;
    char x, y;
    freopen("out", "r", stdin);
    FF(i, 1, 26)
    {
        scanf("%c %c\n", &x, &y);
        map[x] = y;
    }
    map[' '] = ' ';
    freopen("A-small-attempt0.in", "r", stdin);
    scanf("%d", &t);
    getchar();
    FF(i, 1, t)
    {
        gets(s);
        len = strlen(s);
        printf("Case #%d: ", i);
        Ff(j, 0, len)
            printf("%c", map[s[j]]);
        printf("\n");
    }
}
