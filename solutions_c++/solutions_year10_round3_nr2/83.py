#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <cassert>
using namespace std;
char a[11][1001][1001];
int brute(int c, int l, int p)
{
    char &v = a[c][l][p];
    if (v != -1)
        return v;
    if (l * c >= p)
        return v = 0;
    char best = 120;
    for (int i = l + 1; i < p; i++) {
        char r1 = brute(c, l, i);
        char r2 = brute(c, i, p);
        best = min(best, max(r1, r2));
    }
    return v = best + 1;
}
void problem(int id)
{
    int l, p, c;
    assert(3 == scanf("%d%d%d", &l, &p, &c));
    int r = brute(c, l, p);
    printf("Case #%d: %d\n", id + 1, r);
}
int main(int argc, char **argv)
{
    memset(a, -1, sizeof(a));
    int n;
    assert(1 == scanf("%d", &n));
    int id = 0;
    while (n--) {
        problem(id++);
    }
    return 0;
}
