#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <stack>

using namespace std;

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("in", "rt", stdin);
        freopen("out", "wt", stdout);
    #endif
    int testCount;
    cin >> testCount;
    for (int t = 1; t <= testCount; ++t)
    {
        int n;
        cin >> n;
        vector<int> a(n);
        int x = 0, sumAll = 0;
        for (int i = 0; i < n; ++i)
        {
            cin >> a[i];
            x ^= a[i];
            sumAll += a[i];
        }
        if (x != 0)
        {
            printf("Case #%d: NO\n", t);
            continue;
        }
        sort(a.begin(), a.end());
        printf("Case #%d: %d\n", t, sumAll - a[0]);
    }
    return 0;
}
