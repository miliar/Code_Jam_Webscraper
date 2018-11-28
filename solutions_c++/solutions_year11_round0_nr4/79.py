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

double E[1005];
int T,n,a[1005];
bool exist[1005];

int main()
{
    freopen("d.i2","r",stdin);
    freopen("d.o2","w",stdout);

    E[1] = 0;
    for (int i = 2; i <= 1000; i++)
    {
        E[i] = 1;
        for (int j = 2; j < i; j++) E[i] += E[j]/j;
        E[i] *= (1.0 * i/(i - 1));
    }

    scanf("%d", &T);
    for (int it = 1; it <= T; it++)
    {
        scanf("%d", &n);
        for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
        memset(exist,true,sizeof(exist));
        double ret = 0.0;
        for (int i = 1; i <= n; i++) if (exist[i])
        {
            int u = i;
            exist[u] = false;
            int L = 1;
            while (1)
            {
                u = a[u];  if (!exist[u]) break;
                L++;  exist[u] = false;
            }
            ret += E[L];
        }
        printf("Case #%d: %.6lf\n", it, ret);
    }
}
