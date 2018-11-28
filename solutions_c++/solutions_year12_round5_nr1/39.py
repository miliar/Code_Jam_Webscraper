#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <algorithm>
using namespace std;

const int maxn = 1000 + 5;

int n, p[maxn], l[maxn], id[maxn];

bool cmp(int a, int b)
{
    if (p[a] * l[b] == p[b] * l[a])
        return a < b;
    else
        return p[a] * l[b] > p[b] * l[a];
}

int main()
{
    freopen("a2.in", "r", stdin);
    freopen("a2.out", "w", stdout);

    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);
        cin >> n;
        for (int i = 1; i <= n; ++i)
            cin >> l[i];
        for (int i = 1; i <= n; ++i)
            cin >> p[i];
        for (int i = 1; i <= n; ++i)
            id[i] = i;
        sort(id + 1, id + n + 1, cmp);
        for (int i = 1; i <= n; ++i)
            cout << id[i] - 1 << " ";
        printf("\n");
    }
    
    return 0;
}
