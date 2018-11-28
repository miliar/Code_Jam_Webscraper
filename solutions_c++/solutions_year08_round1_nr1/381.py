#include <algorithm>
#include <iostream>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cctype>
#include <queue>
#include <cmath>
#include <list>
#include <set>
#include <map>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i=0;i<t;i++)
    {
        int f[1005], g[1005];
        int n;
        cin >> n;
        for (int i=0;i<n;i++)
            cin >> f[i];
        for (int i=0;i<n;i++)
            cin >> g[i];
        sort(f, f + n);
        sort(g, g + n, greater <int>());
        long long sum = 0;
        for (int i=0;i<n;i++)
            sum += f[i] * g[i];
        printf("Case #%d: %lld\n", i + 1, sum);
    }
	return 0;
}