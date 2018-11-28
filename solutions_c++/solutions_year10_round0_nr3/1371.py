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
    int ncase;
    scanf("%d", &ncase);
    for (int icase = 1; icase <= ncase; icase++)
    {
        long long R,k;
        int n;
        scanf("%I64d", &R);
        scanf("%I64d", &k);
        scanf("%d", &n);
        vector <long long> vi;
        for (int i = 0; i < n; i++)
        {
            long long t;
            scanf("%I64d", &t);
            vi.push_back(t);
        }
        long long money = 0;
        int ind = 0;
        for (int z = 0; z < n; z++)
            if (vi[z%n] <= k)
            {
                ind = z;
                break;
            }
        for (long long i = 0; i < R; i++)
        {
            long long tmp = 0;
            int z = ind;
            for (; z < ind+n; z++)
            {
                if (tmp + vi[z%n] <= k)
                    tmp += vi[z%n];
                else
                    break;
            }
            money += tmp;
            ind = z % n;
            z = ind;
            for (; z < ind+n; z++)
                if (vi[z%n] <= k)
                    break;
            ind = z % n;
        }
        printf("Case #%d: %I64d\n", icase, money);
    }
    return 0;
}
