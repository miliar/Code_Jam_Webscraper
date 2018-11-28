#pragma comment(linker, "/STACK:40000000") 

#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>

using namespace std;

double a[1100];

double solve(int n)
{
    if (a[n] < 0) {

    }
    return a[n];
}

int main()
{
    freopen("i.txt", "r", stdin);
    freopen("o.txt", "w", stdout);

    int N;
    scanf("%d", &N);
    for (int I = 1; I <= N; ++I) {
        int n, res = 0;
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i) {
            int x;
            scanf("%d", &x);
            if (x != i) {
                ++res;
            }
        }
        printf("Case #%d: %d.000000\n", I, res);
    }

    return 0;
}
