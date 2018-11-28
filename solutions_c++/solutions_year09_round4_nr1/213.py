#include <cstdio>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

int main()
{
    int tc;
    scanf("%d", &tc);
    for (int i = 0; i < tc; i++)
    {
        printf("Case #%d: ", i + 1);
        int n;
        char row[64];
        int end[64];
        scanf("%d", &n);
        for (int j = 0; j < n; j++)
        {
            scanf("%s", row);
            end[j] = -1;
            for (int k = 0; k < n; k++)
            {
                if (row[k] == '1')
                {
                    end[j] = k;
                }
            }
        }
        int swap = 0;
        for (int j = 0; j < n; j++)
        {
            if (end[j] > j)
            {
                int min = 0;
                for (int k = j + 1; k < n; k++)
                {
                    if (end[k] <= j)
                    {
                        min = k;
                        break;
                    }
                }
                swap += min - j;
                for (int k = min; k > j; k--)
                {
                    end[k] = end[k - 1];
                }
                end[j] = end[min];
            }
        }
        printf("%d\n", swap);
    }
    return 0;
}
