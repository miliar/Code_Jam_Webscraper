#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

int T,n;
int a[1005];

int main()
{
    freopen("c.i2","r",stdin);
    freopen("c.o2","w",stdout);

    scanf("%d", &T);
    for (int it = 1; it <= T; it++)
    {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf("%d", &a[i]);
        int xorValue = 0;
        for (int i = 0; i < n; i++) xorValue ^= a[i];

        printf("Case #%d: ", it);
        if (xorValue > 0)
        {
            printf("NO\n");  continue;
        }

        sort(a,a + n);
        int ret = 0;
        for (int i = 1; i < n; i++) ret += a[i];
        printf("%d\n", ret);
    }
}
