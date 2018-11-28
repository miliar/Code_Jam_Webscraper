#include <cstdio>
#include <memory.h>

void fillMap(char gToNMap[], char gWords[], char nWords[]);

int main() 
{
    int t, n, s, p;
    scanf("%d", &t);
    for (int caseNum = 1; caseNum <= t; ++caseNum)
    {
        scanf("%d", &n);
        scanf("%d", &s);
        scanf("%d", &p);
        int result = 0;
        int tmp;
        for (int idx = 0; idx < n; ++idx)
        {
            scanf("%d", &tmp);
            if (tmp < p)
            {
                continue;
            }
            else if (tmp + 2 >= 3 * p)
            {
                ++result;
            }
            else if (s > 0)
            {
                if (tmp + 4 >= 3 * p)
                {
                    --s;
                    ++result;
                }
            }
        }
        printf("Case #%d: %d\n", caseNum, result);
    }
    return 0;
}

void fillMap(char gToNMap[], char gWords[], char nWords[]) 
{
    int ptr = 0;
    while (gWords[ptr] != '\0')
    {
        gToNMap[gWords[ptr] - 'a'] = nWords[ptr];
        ++ptr;
    }
}
