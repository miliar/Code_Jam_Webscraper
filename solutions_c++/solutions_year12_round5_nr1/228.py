#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

struct node
{
    int x, y;
};

inline bool cmp(node a, node b)
{
    if (a.x != b.x) return a.x > b.x;
    return a.y < b.y;
}

int main()
{
    int t;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++) {
        int n, x;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf("%d", &x);
        node p[n];
        for (int i = 0; i < n; i++) scanf("%d", &p[i].x), p[i].y = i;
        sort(p, p + n, cmp);
        printf("Case #%d:", cases);
        for (int i = 0; i < n; i++) printf(" %d", p[i].y);
        printf("\n");
    }
    return 0;
}
