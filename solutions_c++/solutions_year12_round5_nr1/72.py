#include <iostream>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <cstdio>
using namespace std;

#define double long double
const double EPS = 1e-8;

struct lev
{
    double k;
    double l;
    int num;
    friend bool operator <(lev a, lev b)
    {
        double ta = ((1 + a.l) * a.k + b.l) * b.k;
        double tb = ((1 + b.l) * b.k + a.l) * a.k;
        if (abs(ta - tb) < EPS)
            return a.num < b.num;
        else
            return ta < tb;
    }
};

const int N = 2020;
    int L[N];
    int P[N];
    lev Q[N];

void solve(int C)
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int l;
        scanf("%d", &l);
        Q[i].l = l;
        Q[i].num = i;
    }
    for (int i = 0; i < n; i++)
    {
        int p;
        scanf("%d", &p);
        Q[i].k = 100.0 / (100 - p);
    }
    sort(Q, Q + n);
    printf("Case #%d: ", C);
    for (int i = 0; i < n; i++)
        printf("%d ", Q[i].num);
    printf("\n");
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
        solve(i + 1);
}
