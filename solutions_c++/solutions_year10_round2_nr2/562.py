#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <iterator>
#include <algorithm>
#include <functional>
#include <numeric>
#include <iomanip>

#include <cstdio>
#include <cstdlib>
#include <cstddef>
#include <cmath>
#include <cctype>
#include <ctime>

using namespace std;

int main(int argc, char *argv[])
{
    char bufline[10240];
    int ncase;
    scanf("%d", &ncase);
    for (int icase = 1; icase <= ncase; icase++)
    {
        int n,k,b,t;
        vector <double> x;
        vector <int>v;
        scanf("%d%d%d%d", &n,&k,&b,&t);
        for (int i = 0; i < n; i++)
        {
            int tmp;
            scanf("%d", &tmp);
            x.push_back(tmp);
        }
        for (int i = 0; i < n; i++)
        {
            int tmp;
            scanf("%d", &tmp);
            v.push_back(tmp);
        }
        vector <double> time(n);
        for (int i = 0; i < n; i++)
            time[i] = (b-x[i])/v[i];
        int ax = 0;
        int bx = 0;
        int can = 0;
        int ret = 0;
        for (int i = n - 1; i >= 0; i--)
        {
            if (time[i] <= t+0.000001)
            {
                ret += ax;
                bx++;
            }
            else
                ax++;
            if (bx >= k)
            {
                can = 1;
                break;
            }
        }
        if (can)
            printf("Case #%d: %d\n", icase, ret);
        else
            printf("Case #%d: IMPOSSIBLE\n", icase);
    }
    return 0;
}
