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

using namespace std;

int minCoin[128][128];
int pos[128];

int search(int start, int end)
{
    if (start == end - 1)
    {
        return 0;
    }
    if (minCoin[start][end] != -1)
    {
        return minCoin[start][end];
    }
    int mc = 0x7FFFFFFF;
    for (int i = start + 1; i < end; ++i)
    {
        int temp = search(start, i) + search(i, end) + pos[end] - pos[start] - 2;
        if (temp < mc)
        {
            mc = temp;
        }
    }
    minCoin[start][end] = mc;
    return mc;
}

int main()
{
    int numTestCase;
    scanf("%d", &numTestCase);
    for (int tc = 1; tc <= numTestCase; ++tc)
    {
        printf("Case #%d: ", tc);
        int P, Q;
        scanf("%d%d", &P, &Q);
        pos[0] = 0;
        pos[Q + 1] = P + 1;
        for (int i = 1; i <= Q; ++i)
        {
            scanf("%d", &pos[i]);
        }
        memset(minCoin, -1, sizeof(minCoin));
        int result = search(0, Q + 1);
        printf("%d\n", result);
    }
    return 0;
}
