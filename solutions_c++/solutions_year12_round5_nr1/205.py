#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
const int N = 1005;

struct Dataa {
    int l, p, n;
} a[N];

bool operator<(const Dataa &a, const Dataa &b)
{ return a.p > b.p || a.p == b.p && a.n < b.n; }
int n, T;

void work()
{
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) scanf("%d", &a[i].l);
    for (int i = 0; i < n; ++i) scanf("%d", &a[i].p);
    for (int i = 0; i < n; ++i) a[i].n = i;
    sort(a, a + n);
    static int ttt = 0;
    printf("Case #%d:", ++ttt);
    for (int i = 0; i < n; ++i) printf(" %d", a[i].n);
    printf("\n");
}

int main()
{
    scanf("%d", &T);
    while (T--) work();
}
