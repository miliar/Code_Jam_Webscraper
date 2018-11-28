#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

char word[6000][18];
char flag[6000];
int L, D, N;

int main()
{
    scanf("%d%d%d", &L, &D, &N);
    for (int i = 0; i < D; ++i)
    {
        scanf("%s", word[i]);
    }
    char pattern[1024];
    for (int i = 1; i <= N; ++i)
    {
        scanf("%s", pattern);
        memset(flag, 0, sizeof(flag));
        int pos = 0;
        for (int p = 0; p < L; p++)
        {
            int mask = 0;
            if (pattern[pos] == '(')
            {
                while (pattern[pos] != ')')
                {
                    mask |= 1 << (pattern[pos] - 'a');
                    ++pos;
                }
                ++pos;
            }
            else
            {
                mask = 1 << (pattern[pos] - 'a');
                ++pos;
            }
            for (int j = 0; j < D; ++j)
            {
                if (!flag[j] && !(mask & (1 << (word[j][p] - 'a'))))
                {
                    flag[j] = 1;
                }
            }
        }
        int count = 0;
        for (int j = 0; j < D; ++j)
        {
            if (!flag[j])
            {
                ++count;
            }
        }
        printf("Case #%d: %d\n", i, count);
    }
    return 0;
}
