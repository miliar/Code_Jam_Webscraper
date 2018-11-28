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
        int n, k;
        scanf("%d", &n);
        scanf("%d", &k);
        int i = 0;
        for (i = 0; i < n; i++)
        {
            if ((k & 1) == 0)
                break;
            k = k >> 1;
        }
        printf("Case #%d: %s\n", icase, (i == n)?"ON":"OFF");
    }
    return 0;
}
