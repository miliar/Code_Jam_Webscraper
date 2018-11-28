#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <list>
#include <iterator>
#include <map>
#include <set>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <cctype>

typedef long long int64;
typedef unsigned long long uint64;

using namespace std;

int main()
{
    int numTestCase;
    scanf("%d", &numTestCase);
    for (int tc = 1; tc <= numTestCase; ++tc)
    {
        printf("Case #%d: ", tc);
        char line[128];
        char map[128];
        memset(map, -1, sizeof(map));
        scanf("%s", line);
        int digit = 0;
        int i;
        for (i = 0; line[i]; ++i)
        {
            char c = line[i];
            if (i == 0)
            {
                map[c] = 1;
            }
            else if (map[c] == -1)
            {
                map[c] = digit;
                digit = (digit == 0 ? 2 : digit + 1);
            }
        }
        int base = (digit == 0 ? 2 : digit);
        --i;
        uint64 min = 0, mul = 1;
        while (i >= 0)
        {
            min += mul * map[line[i--]];
            mul *= base;
        }
        printf("%llu\n", min);
    }
    return 0;
}
