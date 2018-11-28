#include <cstdio>
#include <iostream>

#include <vector>
#include <list>
#include <string>

#include <algorithm>
#include <functional>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

static const int d[] = {
    1, 10, 100, 1000, 10000, 100000, 1000000
};

bool count_digits(int x, int y, int &n)
{
    while(x != 0 || y != 0) {
        if(x == 0 || y == 0) return false;
        x /= 10;
        y /= 10;
        ++n;
    }

    return true;
}

bool recycled(int x, int y)
{
    int n = 0;
    if(count_digits(x, y, n)) {
        for(int i = 1; i < n; ++i) {
            if(x % d[n - i] == y / d[i] && x / d[n - i] == y % d[i])
                return true;
        }
    }

    return false;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n;
    scanf("%d", &n);

    for(int i = 0; i < n; ++i) {
        int a, b;
        scanf("%d%d", &a, &b);

        int ans = 0;
        for(int x = a; x < b; ++x)
            for(int y = x + 1; y <= b; ++y)
                if(recycled(x, y))
                    ++ans;
        printf("Case #%d: %d\n", i + 1, ans);
    }

    return 0;
}
