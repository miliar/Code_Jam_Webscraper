#include <cstdio>

using namespace std;

int t, n, s, p, rez, sol;

int surprinzator(int a, int b)
{
    int i, j, k;
    for(i = 0; i <= 10; ++i) {
        j = i;
        k = j + 2;
        if(i + j + k == a && (i >= b || j >= b || k >= b))
            return 1;
        j = i + 2;
        k = j;
        if(i + j + k == a && (i >= b || j >= b || k >= b))
            return 1;
        j = i + 1;
        k = j + 1;
        if(i + j + k == a && (i >= b || j >= b || k >= b))
            return 1;
    }
    return 0;
}

int normal(int a, int b)
{
    int i, j, k;
    for(i = 0; i <= 10; ++i) {
        j = i;
        k = j;
        if(i + j + k == a && (i >= b || j >= b || k >= b))
            return 1;
        k = j + 1;
        if(i + j + k == a && (i >= b || j >= b || k >= b))
            return 1;
        j = i + 1;
        k = j;
        if(i + j + k == a && (i >= b || j >= b || k >= b))
            return 1;
    }
    return 0;
}


int main()
{
    int test, i;
    freopen ("test.in", "r", stdin);
    freopen ("test.out", "w", stdout);
    scanf("%d", &t);
    for(test = 1; test <= t; ++test) {
        sol = 0;
        scanf("%d %d %d", &n, &s, &p);
        for(i = 1; i <= n; ++i) {
            scanf("%d", &rez);
            if(normal(rez, p))
                ++sol;
            else if(s > 0 && surprinzator(rez, p)) {
                --s;
                ++sol;
            }
        }
        printf("Case #%d: %d\n", test, sol);
    }
    return 0;
}
